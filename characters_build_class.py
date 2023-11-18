import json
import os
import re
from bs4 import BeautifulSoup
import requests

class CharacterScraper:
    def __init__(self):
        pass

    def scrape_data(self, url):
        # Scrape data from the Google Sheets link
        html = requests.get(url).text
        soup = BeautifulSoup(html, "lxml")
        tables = soup.find_all("table")
        index = 0

        for table in tables:
            # Save data to a text file
            with open(f"characters_data/char_{index}.txt", "w", encoding="utf-8") as txt_file:
                txt_file.write("\n".join([",".join([td.text.strip() for td in row.find_all("td")]) for row in table.find_all("tr")]))
            index += 1

      

    def scrape_characters(self, file_path):
        result = []
        pattern = re.compile(r'\d+\.')
        found = False
        name = ''
        role = ''
        weapon = ''
        artifact = ''
        mainstat = ''
        substat = ''
        talent_priority = ''
        index = 0
        # Read data from the specified text file
        file = open(file_path, "r")
        content = file.read()

        # Process and scrape character information
        lines = content.split('\n')
     
        for line in lines:
            print(line)
            if ',ROLE,EQUIPMENT,ARTIFACT STATS,TALENT PRIORITY,ABILITY TIPS' in line:
                index = 0
                found = True
                print('------------------------------------------------------------------')
                elements = line.split(',')
                name = elements[1].replace(" ", "_").strip('"')

            # print(found)
            if found == True:
                # print(index)
                if index == 2:
                    # print('cek')
                    elements = line.split(',')
                    role = elements[2].replace('âœ©', '').strip('"')
             
                    weapon = elements[3].replace('âœ©', '').replace("[R5]", "").replace('"', '').replace('*', '').strip('"')
                    weapon = re.split(pattern, weapon)
                    weapon = [item.strip() for item in weapon if item]

                    artifact = elements[4].replace('âœ©', '').replace("[R5]", "").replace('"', '').replace('*', '').strip('"')
                    artifact = re.split(pattern, artifact)
                    artifact = [item.strip() for item in artifact if item]

                    mainstat = elements[5].replace('"', '').strip('"')
                    substat = elements[6].replace('"', '').replace('*', '').strip('"')
                    substat = re.split(pattern, substat)
                    substat = [item.strip() for item in substat if item]
           

                    result.append({"name": name.capitalize(),
                                "role": role,
                                # 'recommended_weapon': weapon,
                                'recommended_artifact': artifact,
                                'mainstat': mainstat,
                                'substat': substat,
                                })
            index += 1
        return result


def is_folder_empty(folder_path):
    # Mengecek apakah folder kosong atau tidak
    return not any(os.listdir(folder_path))


# Example of how to use the class
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRq-sQxkvdbvaJtQAGG6iVz2q2UN9FCKZ8Mkyis87QHFptcOU3ViLh0_PJyMxFSgwJZrd10kbYpQFl1/pubhtml#'
character_build_list = []
scraper = CharacterScraper()    

if is_folder_empty("characters_data"):
    make_txt = scraper.scrape_data(url)
        
for i in range (0, 7):     
    file_path = f'characters_data/char_{i+3}.txt'
    scrap_data_to_json = scraper.scrape_characters(file_path)
    character_build_list.append({f"{i}":scrap_data_to_json})


print(character_build_list)
with open('output.json', 'w') as json_file:
    json.dump(character_build_list, json_file, indent=2)
