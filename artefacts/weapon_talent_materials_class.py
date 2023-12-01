import json
from bs4 import BeautifulSoup
import requests

class WeaponAscensionMaterials:
    def __init__(self, url, output_filename='schedule_weapon.json'):
        self.url = url
        self.output_filename = output_filename
        self.material_list = []
        self.days_list = []
        self.schedule_data_list = []

    def scrape_material_schedule(self):
        html = requests.get(self.url).text
        soup = BeautifulSoup(html, 'lxml')

        body = soup.find_all('div', class_='gear-list')[2].find('div', class_='rt-tbody')

        for list_apa in body:
            material = list_apa.find('img', class_='table-image potion')['alt']
            material_img = list_apa.find('img', class_='table-image potion')['src']

            self.material_list.append({"name": material, "material_img": material_img})

            days = list_apa.find_all('div', class_='rt-td')[1].text
            self.days_list.append(days)

    def generate_schedule_data(self):
        for i in range(0, len(self.material_list)):
            schedule_data = {"material": self.material_list[i], "days": self.days_list[i]}
            self.schedule_data_list.append(schedule_data)

    def save_to_json(self,filename='weapon_ascension_schedule.json'):
        with open(f'artefacts/datasources/{filename}', 'w', encoding='utf-8') as json_file:
            json.dump(self.schedule_data_list, json_file, ensure_ascii=False, indent=2)


