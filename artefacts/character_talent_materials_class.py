import json
from bs4 import BeautifulSoup
import requests

class CharacterTalentsMaterials:
    def __init__(self, url):
        self.url = url
        self.material_list = []
        self.days_list = []
        self.characters_list = []
        self.schedule_data_list = []

    def scrape_schedule(self):
        html = requests.get(self.url).text
        soup = BeautifulSoup(html, 'lxml')

        body = soup.find('div', class_='gear-list').find('div', class_='rt-tbody')

        for list_apa in body:
            material = list_apa.find('img', class_='table-image potion')['alt']
            material_img = list_apa.find('img', class_='table-image potion')['src']
            self.material_list.append({"name":material,"material_img":material_img})

            days = list_apa.find_all('div', class_='rt-td')[1].text
            self.days_list.append(days)

            characters_list_row = []
            try:
                for i in range(0, len(list_apa.find('div', class_='rt-td wrap-row').find_all('a', class_='character-portrait'))):
                    character_img = list_apa.find('div', class_='rt-td wrap-row').find_all('a', class_='character-portrait')[i].find_all('img')[0]['src']
                    element_img = list_apa.find('div', class_='rt-td wrap-row').find_all('a', class_='character-portrait')[i].find_all('img')[1]['src']
                    characters_list_row.append({"char_img": character_img, "char_elemental": element_img})

            except:
                print('-')
                continue
            
            self.characters_list.append(characters_list_row)

    def generate_schedule_data(self):
        for i in range(0, len(self.material_list)):
            characters_data_list = []
            # for j in range(0, len(self.characters_list[i])):
            characters_data_list.append(self.characters_list[i])
                # print(characters_data_list[j])
            schedule_data = {"material": self.material_list[i], "days": self.days_list[i], "character_list": characters_data_list}
            self.schedule_data_list.append(schedule_data)

    def save_to_json(self, filename='character_material_schedule.json'):
        with open(f'artefacts/datasources/{filename}', 'w', encoding='utf-8') as json_file:
            json.dump(self.schedule_data_list, json_file, ensure_ascii=False, indent=2)


