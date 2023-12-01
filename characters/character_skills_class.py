import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests

class GenshinCharacterInfo:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.character_data = {}

    def _get_soup(self, character):
        print(character.lower())
        html = requests.get(f'https://genshin.gg/characters/{character.lower()}').text
        soup = BeautifulSoup(html, "lxml")
        return soup

    def get_skills(self, character):
        soup = self._get_soup(character)
        output = soup.find_all('div', class_='character-skill')

        skills_data = []
        for index in range(len(output)):
            skill_data = {
                'type': output[index].find('div', class_='character-skill-header').find('h3').text,
                'image_url': output[index].find('img', class_='character-skill-icon')['src'],
                'name': output[index].find('div', class_='character-skill-body').find('h4').text,
                'description': output[index].find('div', class_='character-skill-body').find('div', class_='character-skill-description').text
            }
            skills_data.append(skill_data)

        # self.character_data['skills'] = skills_data
        
        return skills_data

    def get_best_teams(self,character):
        soup = self._get_soup(character)

        team_list = []
        teams = soup.find_all('div', class_='character-team')
        for team in teams:
            team_data = {
                'team_name': team.find('div', class_='character-team-name').text,
                'characters': []
            }
            for i in range(0, 8, 2):
                character_name = team.find('div', class_='character-team-characters').find_all('img')[i]['src']
                element_name = team.find('div', class_='character-team-characters').find_all('img')[i + 1]['src']

                character_data = {
                    'name': character_name,
                    'element': element_name
                }

                team_data['characters'].append(character_data)

            team_list.append(team_data)

        # self.character_data['best_teams'] = team_list
        
        return team_list

    def get_best_weapons_and_artifacts(self,character):
        soup = self._get_soup(character)
        weapon_data = []
        artifact_data = []
        weapons = soup.find_all('div', class_='character-build-section')
        weapon_item_count = len(weapons[0].find_all('div', class_='character-build-weapon'))
        artifact_item_count = len(weapons[1].find_all('div', class_='character-build-weapon'))

        for i in range(0, weapon_item_count):
            weapon_info = {
                'image_url': weapons[0].find_all('div', class_='character-build-weapon')[i].find('img')['src'],
                'name': weapons[0].find_all('div', class_='character-build-weapon')[i].find('img')['alt']
            }
            weapon_data.append(weapon_info)

        for i in range(0, artifact_item_count):
            artifact_set = len((weapons[1].find_all('div', class_='character-build-weapon')[i].find_all('img')))
            artifact_set_data = []
            for j in range(0, artifact_set):
                artifact_info = {
                    'image_url': weapons[1].find_all('div', class_='character-build-weapon')[i].find_all('img')[j]['src'],
                    'name': weapons[1].find_all('div', class_='character-build-weapon')[i].find_all('img')[j]['alt'],
                    'amount': weapons[1].find_all('div', class_='character-build-weapon')[i].find_all('div', class_='character-build-weapon-count')[j].text
                }
                artifact_set_data.append(artifact_info)
            artifact_data.append({'artifacts': artifact_set_data})
        
        return weapon_data, artifact_data

    def get_substats(self,character):
        soup = self._get_soup(character)
        stat_priority = []
        stat = soup.find_all('div', class_='character-stats')
        for i in range(0, len(stat[0].find_all('div', class_='character-stats-item'))):
            priority = stat[0].find_all('div', class_='character-stats-item')[i].text
            stat_priority.append(priority)

        self.character_data['stat_priority'] = stat_priority

        return stat_priority
    
    def to_json(self):
        return json.dumps(self.character_data, indent=2)


# Example usage:
# yoimiya_info = GenshinCharacterInfo('https://genshin.gg/characters/yoimiya/')
# yoimiya_info.get_skills()
# yoimiya_info.get_best_teams()
# yoimiya_info.get_best_weapons_and_artifacts()
# yoimiya_info.get_substats()

# # Convert to JSON
# yoimiya_json = yoimiya_info.to_json()
# print(yoimiya_json)
