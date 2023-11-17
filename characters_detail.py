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

html = requests.get('https://paimon.moe/characters/furina').text
soup = BeautifulSoup(html, "lxml")



result_material_1 = []
material_1 = []
result_material_2 = []
material_2 = []

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
        # print("Alt:", alt_attribute)
        # print("Src:", f'https://paimon.moe/{src_attribute}')

material_1.append({"talentMaterial": result_material_1})
        
# MATERIAL ASCENSION
material_asc =  soup.find_all('div', class_='text-gray-200 rounded-xl border border-gray-200 border-opacity-25 p-4 svelte-ti79zj')
for div_element in material_asc:
    img_tags = div_element.findAll('img')
    for img_tag in img_tags:
        
        alt_attribute = img_tag['alt']
        src_attribute = 'https://paimon.moe' + img_tag['src']
        
        # Print or use the extracted values as needed
        result_material_2.append({"name":alt_attribute, "image":src_attribute})
    
material_2.append({"talentAsencsion": result_material_2})

# STAT LEVEL
stat_level =  soup.find_all('div', class_='px-4 svelte-ti79zj')
for div_element in stat_level:
    td_tags = div_element.find_all('td')
    for td_tag in td_tags:
        print(td_tag.text)
    # print(td_tags)
    
# print(stat_level)






final_result = material_1 + material_2

# Save the result in a JSON file
with open('characters_material.json', 'w') as json_file:
    json.dump(final_result , json_file, indent=2)

# Print the result
# print(json.dumps(final_result, indent=2))
# Load the page with Selenium
# driver.get(url)

# # Wait for dynamic content to load (you may need to adjust the wait time)
# driver.implicitly_wait(10)

# # Get the updated page source after dynamic content has loaded
# html = driver.page_source

# # Close the WebDriver
# driver.quit()

# Parse the updated HTML content with BeautifulSoup
# soup = BeautifulSoup(html, 'html.parser')
# result = []

# Talen + Boss
# text-gray-200 rounded-xl border border-gray-200 border-opacity-25 p-4 flex svelte-ti79zj

# Material ascensioin
# text-gray-200 rounded-xl border border-gray-200 border-opacity-25 p-4 svelte-ti79zj

# Stats
# px-4 svelte-ti79zj

# NA
# py-4 rounded-xl bg-item flex flex-col mb-4 svelte-ynrzzr

# Elemental
# py-4 rounded-xl bg-item flex flex-col mb-4 svelte-ynrzzr

# Pasif
# py-4 rounded-xl bg-item flex flex-col mb-2

# Constellations
# py-4 rounded-xl bg-item flex flex-col mb-2
