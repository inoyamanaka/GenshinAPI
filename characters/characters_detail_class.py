import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json


class GenshinCharacterScraper:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def scrape_paimon_moe(self, character_name):
        result_material_1 = []
        result_material_2 = []
        char_name = character_name
        
        if character_name == 'Childe':
            char_name = 'tartaglia'
        
        html = requests.get(f'https://paimon.moe/characters/{char_name.lower()}').text
        soup = BeautifulSoup(html, "lxml")

        # ... (your existing scraping code for paimon.moe)
        # MATERIAL TALENT
        material = soup.find_all('div', class_='text-gray-200 rounded-xl border border-gray-200 border-opacity-25 p-4 flex svelte-ti79zj')

        # Loop through each div element
        for div_element in material:
            img_tags = div_element.findAll('img')
            for img_tag in img_tags:
                
                alt_attribute = img_tag['alt']
                src_attribute = 'https://paimon.moe' + img_tag['src']
                
                # Print or use the extracted values as needed
                result_material_1.append({"name":alt_attribute, "image":src_attribute})
                
        # MATERIAL ASCENSION
        material_asc =  soup.find_all('div', class_='text-gray-200 rounded-xl border border-gray-200 border-opacity-25 p-4 svelte-ti79zj')
        for div_element in material_asc:
            img_tags = div_element.findAll('img')
            for img_tag in img_tags:
                
                alt_attribute = img_tag['alt']
                src_attribute = 'https://paimon.moe' + img_tag['src']
                
                # Print or use the extracted values as needed
                result_material_2.append({"name":alt_attribute, "image":src_attribute})

        return result_material_1, result_material_2

    def scrape_genshin_wiki(self, character_name):
        char_name = character_name.replace(' ', '_')
        if character_name == 'Childe':
            char_name = 'Tartaglia'
        if character_name == 'Ayaka':
            char_name = "Kamisato_Ayaka"
        if character_name == 'Ayato':
            char_name = "Kamisato_Ayato"
        if character_name == 'Itto':
            char_name = "Arataki_Itto"
        if character_name == 'Kazuha':
            char_name = "Kaedehara_Kazuha"
        if character_name == 'Kokomi':
            char_name = 'Sangonomiya_Kokomi'
        if character_name == 'Raiden':
            char_name = 'Raiden_Shogun'
        if character_name == 'Heizou':
            char_name = 'Shikanoin_Heizou'
        if character_name == 'Sara':
            char_name = 'Kujou_Sara'
            
        
            
       
        list_img_char = []

        img_char_1 = ''
        img_char_2 = ''
        img_char_3 = ''
        img_char_nbg = ''

        html_2 = requests.get(f'https://genshin-impact.fandom.com/wiki/{char_name.title()}').text
        soup_2 = BeautifulSoup(html_2, "lxml")
        
        
        html_nobg = requests.get(f"https://genshinbuild.com/en/{char_name.lower().replace('_', '-')}").text
        soup_nobg = BeautifulSoup(html_nobg, "lxml")
        try:
            img_char_nobg = soup_nobg.find_all('div', id='pers')[0].find_all('img')[1]['src']
        except:
            img_char_nobg = soup_nobg.find_all('section', id='pers')[0].find_all('img')[1]['src']
     

        # ... (your existing scraping code for genshin wiki)
        img_char = soup_2.find_all('div', class_='wds-tab__content')

        img_char_1 = img_char[0].find('a')['href']
        img_char_2 = img_char[1].find('a')['href']
        img_char_3 = img_char[2].find('a')['href']
        # img_char_nbg = f'https://cdn.wanderer.moe/genshin-impact/splash-art/{char_name.lower()}-nobg.png'

        list_img_char.append({
                            "img_card":img_char_1,
                            "img_wish":img_char_2,
                            "img_in_game":img_char_3,
                            "img_char_nbg":img_char_nobg})
                

        return list_img_char

    def scrape_character_info(self, character_name):
        char_name = character_name
        if character_name == 'Childe':
            char_name = 'Tartaglia'
        if character_name == 'Raiden':
            char_name = 'Raiden_Shogun'
        if character_name == 'Sara':
            char_name = 'Kujou_Sara'
            
        html_2 = requests.get(f'https://genshin-impact.fandom.com/wiki/{char_name.title()}').text
        soup_2 = BeautifulSoup(html_2, "lxml")
        
        detail = soup_2.find_all('tr')
        nation = soup_2.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color')
        information = []
        
        rarity = ''
        weapon = ''
        element = ''
        model_type = ''
        try:
            rarity = detail[1].find('img', class_='lazyload')['alt']
            weapon = detail[1].find('a')['title']
            element = detail[3].findAll('a')[1].get_text()
            
        except:
            rarity = detail[1].find('img', class_='lazyload')['alt']
            weapon = detail[1].find('a')['title']
            element = detail[1].findAll('a')[2]['title']    

        # ---------------------------------------------------------------------------------------------------
        real_name = ''
        constellation = ''
        region = ''
        affiliation = ''

        img_namecard_1 = ''
        img_namecard_2 = ''
        img_namecard_3 = ''

        information = []
        list_img_namecard = []

        first_col = nation[0].find('h3').get_text()

        if first_col != "Real Name":
            real_name = ''
            constellation = nation[1].find('div', class_='pi-data-value').a.get_text()
            region = nation[2].find('div', class_='pi-data-value').a.get_text()
            try:
                affiliation = nation[3].find('div', class_='pi-data-value').a.get_text()
            except:
                affiliation = nation[3].find('div', class_='pi-data-value pi-font').get_text()

            
            namecard = f"https://genshin-impact.fandom.com/{nation[5].find_all('a')[1]['href']}"
            # print(nation[5].find_all('a')[1]['href'])
            if nation[5].find_all('a')[1]['href'] == '#cite_note-Howto-2':
                namecard = f"https://genshin-impact.fandom.com/{nation[4].find_all('a')[1]['href']}"

            
            html_3 = requests.get(namecard).text
            soup_3 = BeautifulSoup(html_3, "lxml")
            
            # namedcard = soup_3.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color')
            img_namecard = soup_3.find_all('div', class_='wds-tab__content')
            
            img_namecard_1 = img_namecard[0].find('a')['href']
            img_namecard_2 = img_namecard[1].find('a')['href']
            img_namecard_3 = img_namecard[2].find('a')['href']
            
            list_img_namecard.append({
                                "img_namecard_1":img_namecard_1,
                                "img_namecard_2":img_namecard_2,
                                "img_namecard_3":img_namecard_3})
            
        else :
            real_name = nation[0].find('div', class_='pi-data-value pi-font').get_text()
            constellation = nation[2].find('div', class_='pi-data-value').a.get_text()
            region = nation[3].find('div', class_='pi-data-value').a.get_text()
            affiliation = nation[4].find('div', class_='pi-data-value').a.get_text()
            
            namecard = f"https://genshin-impact.fandom.com/{nation[6].find_all('a')[1]['href']}"
            html_3 = requests.get(namecard).text
            soup_3 = BeautifulSoup(html_3, "lxml")
            
            # namedcard = soup_3.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color')
            img_namecard = soup_3.find_all('div', class_='wds-tab__content')
            img_namecard_1 = img_namecard[0].find('a')['href']
            img_namecard_2 = img_namecard[1].find('a')['href']
            img_namecard_3 = img_namecard[2].find('a')['href']
            
            list_img_namecard.append({
                                "img_namecard_1":img_namecard_1,
                                "img_namecard_2":img_namecard_2,
                                "img_namecard_3":img_namecard_3})
            # print(img_namecard_1)
            
        information.append({"real_name":real_name,
                            "rarity":rarity,
                            "weapon":weapon,
                            "constellation":constellation,
                            "region":region,
                            "affiliation":affiliation,
                            "element":element,
                            "img_namecard":list_img_namecard,
                            })

        return information

    def save_to_json(self, data, filename):
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=2)


# # Example of how to use the class
# scraper = GenshinCharacterScraper()


# character_name = 'Xiangling'  # Replace with the desired character name
# result_material_1, result_material_2 = scraper.scrape_paimon_moe(character_name)
# list_img_char = scraper.scrape_genshin_wiki(character_name)
# information = scraper.scrape_character_info(character_name)

# scraper.save_to_json(information, 'characters_material.json')
