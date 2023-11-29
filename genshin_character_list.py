import json
from bs4 import BeautifulSoup
import requests

all_characters = []

html = requests.get('https://genshin.gg/').text
soup = BeautifulSoup(html, "lxml")

char_list = soup.find('div', class_='character-list')
character_info_new = char_list.find_all('a', class_='character-portrait character-new')
character_info_old = char_list.find_all('a', class_='character-portrait')

for character in character_info_new:
    img_tags = character.find('img')
    alt_attribute = img_tags.get('alt')
    all_characters.append({'character_name': alt_attribute})

for character in character_info_old:
    img_tags = character.find('img')
    alt_attribute = img_tags.get('alt')
    all_characters.append({'character_name': alt_attribute})

json_result = json.dumps(all_characters, indent=2)
print(json_result)
