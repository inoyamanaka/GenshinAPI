import json
from bs4 import BeautifulSoup
import requests


html = requests.get(f'https://genshin.gg/characters/yoimiya/').text
soup = BeautifulSoup(html, "lxml")

# Save variable

# GET SKILLS AND CONSTELLATIONS
output = soup.find_all('div', class_='character-skill')

for index in range (0, len(output)):
    type_skill = output[index].find('div', class_='character-skill-header').find('h3').text
    skill_img =  output[index].find('img', class_='character-skill-icon')['src']
    skill_name = output[index].find('div', class_='character-skill-body').find('h4').text
    skill_description = output[index].find('div', class_='character-skill-body').find('div', class_='character-skill-description').text


# GET BEST TEAMS
team_list = []
teams = soup.find_all('div', class_='character-team')
for team in teams:
    team_data = {
        'team_name': team.find('div', class_='character-team-name').text,
        'characters': []
    }
    # print(team.find('div', class_='character-team-name').text)
    for i in range (0, 8, 2):
        character_name = team.find('div', class_='character-team-characters').find_all('img')[i]['src']
        element_name = team.find('div', class_='character-team-characters').find_all('img')[i + 1]['src']
        
        character_data = {
                'name': character_name,
                'element': element_name
            }
        
        team_data['characters'].append(character_data)
        
    team_list.append(team_data)


# GET BEST WEAPONS AND ARTEFACTS
weapon_data = []
artifact_data = []
weapons = soup.find_all('div', class_='character-build-section')
weapon_item_count = len(weapons[0].find_all('div', class_='character-build-weapon'))
artifact_item_count = len(weapons[1].find_all('div', class_='character-build-weapon'))

for i in range (0, weapon_item_count):
    weapon_info = {
        'image_url': weapons[0].find_all('div', class_='character-build-weapon')[i].find('img')['src'],
        'name': weapons[0].find_all('div', class_='character-build-weapon')[i].find('img')['alt']
    }
    weapon_data.append(weapon_info)

for i in range (0, artifact_item_count):
    artifact_set = len((weapons[1].find_all('div', class_='character-build-weapon')[i].find_all('img')))
    artifact_set_data = []
    for j in range (0, artifact_set):
        artifact_info = {
            'image_url': weapons[1].find_all('div', class_='character-build-weapon')[i].find_all('img')[j]['src'],
            'name': weapons[1].find_all('div', class_='character-build-weapon')[i].find_all('img')[j]['alt'],
            'amount': weapons[1].find_all('div', class_='character-build-weapon')[i].find_all('div', class_='character-build-weapon-count')[j].text
        }
        artifact_set_data.append(artifact_info)
    artifact_data.append({'artifacts': artifact_set_data})

# GET SUBSTATS
stat_priority = []
stat = soup.find_all('div', class_='character-stats')
for i in range (0, len(stat[0].find_all('div', class_='character-stats-item'))):
    priority = stat[0].find_all('div', class_='character-stats-item')[i].text
    stat_priority.append(priority)

stat_priority = {"stat_priority":stat_priority}
