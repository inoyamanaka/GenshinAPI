from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json

# Set up the Chrome WebDriver with Selenium
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
# service = ChromeService("path/to/chromedriver")  # Replace with the path to your chromedriver executable
driver = webdriver.Chrome(options=chrome_options)

url = 'https://wanderer.moe/genshin-impact/splash-art'

# Load the page with Selenium
driver.get(url)

# Wait for dynamic content to load (you may need to adjust the wait time)
driver.implicitly_wait(10)

# Get the updated page source after dynamic content has loaded
html = driver.page_source

# Close the WebDriver
driver.quit()

# Parse the updated HTML content with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
result = []


# Find all <a> tags with 'download' attribute
download_links = soup.find_all('a', attrs={'download': True, 'href': True})
# Sort the links based on the 'href' attribute
sorted_links = sorted(download_links, key=lambda x: x['href'])
# Extract and print the 'href' attribute from each <a> tag
for link in sorted_links:
    href = link['href']
    result.append(href)
    
    
print(len(sorted_links))
print(result)

# # Proses untuk mengubah data ke format yang diinginkan
final_result = {}
for url in result:
    # Mengambil nama karakter dari URL (asumsi bahwa nama karakter ada di URL)
    character_name = url.split('/')[-1].split('-')[0].capitalize()
    
    # Menghapus ekstensi file dan digit terakhir (jika ada)
    if character_name.endswith('.png'):
        character_name = character_name.rsplit('.', 1)[0]
    if character_name[-1].isdigit():
        character_name = character_name[:-1]
    
    # Menambahkan URL ke dalam daftar URL karakter
    if character_name in final_result:
        final_result[character_name].append(url)
    else:
        final_result[character_name] = [url]


# Save the result in a JSON file
with open('characters_img_urls.json', 'w') as json_file:
    json.dump(final_result, json_file, indent=2)

# Print the result
print(json.dumps(final_result, indent=2))