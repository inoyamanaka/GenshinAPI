from bs4 import BeautifulSoup
import csv
import requests
import json

from characters_detail_class import GenshinCharacterScraper
    
# Program to read the entire file using read() function
file = open('output.json')
content = json.load(file)

# Import scrapper
scraper = GenshinCharacterScraper()
character_data_list = []


# element, element, index
# print(content[1]['1'][0]['recommended_weapon']) 

for h in range (0, 7):
    for i in range (0, len(content[h][f'{h}'])):
        print(content[h][f'{h}'][i]['name'])
        character_name = content[h][f'{h}'][i]['name']
        character_role = content[h][f'{h}'][i]['role']
        try:
            recommended_weapon = content[h][f'{h}'][i]['recommended_weapon']
        except:
            recommended_weapon = ''
        recommended_artifact = content[h][f'{h}'][i]['recommended_artifact']
        arte_mainstat = content[h][f'{h}'][i]['mainstat']
        arte_substat = content[h][f'{h}'][i]['substat']
        
        
        result_material_1, result_material_2 = scraper.scrape_paimon_moe(character_name)
        list_img_char = scraper.scrape_genshin_wiki(character_name)
        information = scraper.scrape_character_info(character_name)
        # print(information)
        # Create a dictionary for each character's information
        character_data = {
            "name": character_name,
            "role": character_role,
            "character_info": information,
            "recommended_weapon":recommended_weapon,
            "recommended_artifact":recommended_artifact,
            "arte_mainstat":arte_mainstat,
            "arte_substat":arte_substat,
            "material_1": result_material_1,
            "material_2": result_material_2,
        }
        
        # Append the dictionary to the list
        character_data_list.append(character_data)
    
# Save the list of character data to a JSON file
with open('characters_data_combine.json', 'w') as json_file:
    json.dump(character_data_list, json_file, indent=2)
