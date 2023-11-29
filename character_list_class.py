import json
from bs4 import BeautifulSoup
import requests

class GenshinCharacterListScraper:
    def __init__(self, url):
        self.url = url
        self.all_characters = []

    def _get_soup(self):
        html = requests.get(self.url).text
        soup = BeautifulSoup(html, 'lxml')
        return soup

    def scrape_characters(self):
        soup = self._get_soup()

        char_list = soup.find('div', class_='character-list')
        character_info_new = char_list.find_all('a', class_='character-portrait character-new')
        character_info_old = char_list.find_all('a', class_='character-portrait')

        for character in character_info_new:
            img_tags = character.find('img')
            alt_attribute = img_tags.get('alt')
            self.all_characters.append({'character_name': alt_attribute})

        for character in character_info_old:
            img_tags = character.find('img')
            alt_attribute = img_tags.get('alt')
            self.all_characters.append({'character_name': alt_attribute})

    def save_to_json(self, filename='characters.json'):
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(self.all_characters, json_file, ensure_ascii=False, indent=2)
        print(f"JSON file created: {filename}")

# Example usage:
url = 'https://genshin.gg/'
scraper = GenshinCharacterListScraper(url)
scraper.scrape_characters()
# scraper.save_to_json()
