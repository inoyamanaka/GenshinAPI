import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json

# Set up the Chrome WebDriver with Selenium
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
driver = webdriver.Chrome(options=chrome_options)

# ---------------------------------------------------------------------------------------------------
#                                        PAIMON MOE
# ---------------------------------------------------------------------------------------------------


html = requests.get('https://paimon.moe/characters/neuvillette').text
soup = BeautifulSoup(html, "lxml")

result_material_1 = []
result_material_2 = []


material_boss = ''
material_boss_img = ''

material_book = ''
material_book_img = ''

material_ascension = ''
material_ascension_img = ''


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

# ---------------------------------------------------------------------------------------------------
#                                        GENSHIN WIKI FANDOM
# ---------------------------------------------------------------------------------------------------
html_2 = requests.get('https://genshin-impact.fandom.com/wiki/Yoimiya').text
soup_2 = BeautifulSoup(html_2, "lxml")

img_char_1 = ''
img_char_2 = ''
img_char_3 = ''
list_img_char = []

nation = soup_2.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color')
img_char = soup_2.find_all('div', class_='wds-tab__content')

img_char_1 = img_char[0].find('a')['href']
img_char_2 = img_char[1].find('a')['href']
img_char_3 = img_char[2].find('a')['href']

list_img_char.append({
                    "img_card":img_char_1,
                    "img_wish":img_char_2,
                    "img_in_game":img_char_3})

# ---------------------------------------------------------------------------------------------------

detail = soup_2.find_all('tr')
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
    affiliation = nation[3].find('div', class_='pi-data-value').a.get_text()
    
    namecard = f"https://genshin-impact.fandom.com/{nation[5].find_all('a')[1]['href']}"
    html_3 = requests.get(namecard).text
    soup_3 = BeautifulSoup(html_3, "lxml")
    
    namedcard = soup_3.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color')
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
    
    namedcard = soup_3.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color')
    img_namecard = soup_3.find_all('div', class_='wds-tab__content')
    img_namecard_1 = img_namecard[0].find('a')['href']
    img_namecard_2 = img_namecard[1].find('a')['href']
    img_namecard_3 = img_namecard[2].find('a')['href']
    
information.append({"real_name":real_name,
                    "rarity":rarity,
                    "weapon":weapon,
                    "constellation":constellation,
                    "region":region,
                    "affiliation":affiliation,
                    "element":element,
                    "img_namecard":list_img_namecard,
                    "img_character":list_img_char,
                    "talentMaterial": result_material_1,
                    "talentAsencsion": result_material_2})
    
# Save the result in a JSON file
with open('characters_material.json', 'w') as json_file:
    json.dump(information , json_file, indent=2)