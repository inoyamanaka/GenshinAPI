import json
import os
import re
from bs4 import BeautifulSoup
import requests
url = "https://genshin.hoyoverse.com/en/character/mondstadt"
# html = requests.get().content
# soup = BeautifulSoup(html, "html.parser")
# tables = soup.find_all("li", class_=["swiper-slide", "swiper-slide-active"])

# print(soup)

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# target_div = soup.find('div', class_="character__main")  # Replace 'my-div' with the actual div ID
# li_count = len(target_div.find_all('li'))

# print("Number of <li> tags within the specific <div>: ", li_count)
print(soup)