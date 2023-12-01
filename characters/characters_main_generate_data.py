from bs4 import BeautifulSoup
import csv
import requests
import json
from character_list_class import GenshinCharacterListScraper
from character_skills_class import GenshinCharacterInfo
from characters_detail_class import GenshinCharacterScraper
import asyncio


all_character_data = []
# GET LIST OF ALL CHARACTERS
character_list = GenshinCharacterListScraper('https://genshin.gg/')
character_list.scrape_characters()
# character_list.save_to_json()

file = open('characters.json')
character_list_result = json.load(file) 

# SCRAPPING DATA PART-1
scraper = GenshinCharacterScraper()
char_info = GenshinCharacterInfo()

character_data_list = []

for i in range (0, len(character_list_result)):
    try:
        name = character_list_result[i]['character_name']
        result_material_1, result_material_2 = scraper.scrape_paimon_moe(character_list_result[i]['character_name'])
        information =  scraper.scrape_character_info(character_list_result[i]['character_name'])
        char_image = scraper.scrape_genshin_wiki(character_list_result[i]['character_name'])
        
        # char_info.get_skills()
        # char_info.get_best_teams()
        # char_info.get_best_weapons_and_artifacts()
        # char_info.get_substats()
        
        # character_data['images'] = scraper.scrape_genshin_wiki(character_list_result[i]['character_name'])
        # character_data['information'] = scraper.scrape_character_info(character_list_result[i]['character_name'])
        
        character_data = {
            'character_name': name ,
            "element": information[0]["element"],
            "rarity": information[0]["rarity"],
            "weapon": information[0]["weapon"],
            "constellation": information[0]["constellation"],
            "region": information[0]["region"],
            "affiliation": information[0]["affiliation"],
            "img_namecard": information[0]["img_namecard"],
            "char_image": char_image,
            'material': result_material_1+result_material_2,  
            "best_weapon": char_info.get_best_weapons_and_artifacts(name.replace(' ', ''))[0],
            "best_artefact": char_info.get_best_weapons_and_artifacts(name.replace(' ', ''))[1],
            "best_team": char_info.get_best_teams(name.replace(' ', '')),
            "stat_priority": char_info.get_substats(name.replace(' ', '')),
            'skills': char_info.get_skills(name.replace(' ', ''))
        }
        all_character_data.append(character_data)
        
        
        print('==================================================================================')
    except Exception as error:
        print(error)
        continue
    
    
# SCRAPPING DATA PART-2

    
# Menyimpan semua data ke dalam file JSON
output_file_path = 'all_character_data.json'
with open(output_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(all_character_data, json_file, ensure_ascii=False, indent=2)

print(f"Data karakter berhasil disimpan ke dalam file: {output_file_path}")
# element, element, index
# print(character_list_result[1]) 

# for h in range (0, 7):
#     for i in range (0, len(content[h][f'{h}'])):
#         print(content[h][f'{h}'][i]['name'])
#         character_name = content[h][f'{h}'][i]['name']
#         character_role = content[h][f'{h}'][i]['role']
#         try:
#             recommended_weapon = content[h][f'{h}'][i]['recommended_weapon']
#         except:
#             recommended_weapon = ''
#         recommended_artifact = content[h][f'{h}'][i]['recommended_artifact']
#         arte_mainstat = content[h][f'{h}'][i]['mainstat']
#         arte_substat = content[h][f'{h}'][i]['substat']
        
        
#         result_material_1, result_material_2 = scraper.scrape_paimon_moe(character_name)
#         list_img_char = scraper.scrape_genshin_wiki(character_name)
#         information = scraper.scrape_character_info(character_name)
#         # print(information)
#         # Create a dictionary for each character's information
#         character_data = {
#             "name": character_name,
#             "role": character_role,
#             "list_img_char":list_img_char,
#             "character_info": information,
#             "recommended_weapon":recommended_weapon,
#             "recommended_artifact":recommended_artifact,
#             "arte_mainstat":arte_mainstat,
#             "arte_substat":arte_substat,
#             "material_1": result_material_1,
#             "material_2": result_material_2,
#         }
        
#         # Append the dictionary to the list
#         character_data_list.append(character_data)
    
# # Save the list of character data to a JSON file
# with open('characters_data_combine.json', 'w') as json_file:
#     json.dump(character_data_list, json_file, indent=2)
