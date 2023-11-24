import json
import os
import re
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession

def basic_soup_load(url, params='mondstadt?char=0'):
    url = f"{url}{params}"
    # print(url)
    session = HTMLSession()
    response = session.get(url)
    response.html.render()
    response.close()
    
    soup = BeautifulSoup(response.html.html, 'html.parser')

    return soup

def get_chars_limit(url, region):
    soup = basic_soup_load(url=url, params=region)
    target_div = soup.find('div', 'character__main')

    li_count = round(len(target_div.find_all('li', class_='swiper-slide'))/2)
    return li_count

def get_char_assets(url, region, char_index):
    param = f"{region}?char={char_index}"
    soup = basic_soup_load(url=url, params=param)

    target_main = soup.find('div', class_='character__main')
    target_li_main = target_main.find('li', class_='swiper-slide-active')
    target_person = target_li_main.find('img', class_='character__person').get('src')
    target_emblem = target_li_main.find('img', class_='character__icon').get('src')
    
    target_page = soup.find('ul', class_='character__page--render')
    target_li_page = target_page.find('li', class_='swiper-slide-thumb-active')
    target_icon = target_li_page.find('img').get('src')
    target_name = target_li_page.find('p').text

    # print(target_li_page)
    return [target_person, target_emblem, target_icon, target_name]

def get_region_list(url):
    soup = basic_soup_load(url=url, params='mondstadt')
    target_side = soup.find('ul', class_='character__sidebar')
    target_li_region = target_side.findAll('li', class_='character__city')
    count_region = round(len(target_li_region)-1)
    region_list = [target_li_region[x].find('a').get('href')[14:] for x in range(count_region)]
    # for x in range(count_region):
    #     print(target_li_region[x].find('a').get('href'))
    #     print(target_li_region[x].find('a').text)
    
    return region_list

def main():    
    base_url = f"https://genshin.hoyoverse.com/en/character/"
    regions = get_region_list(url=base_url)

    result = []

    for x in range(len(regions)):
        limit_char = get_chars_limit(url=base_url, region=regions[x])
        print(limit_char)
        result.append(
            {
                "id":f"{x}",
                "region": f"{regions[x]}",
                "characters": []
            }
        )
        for y in range(limit_char):
            get_data = get_char_assets(url=base_url, region=regions[x], char_index=y)

            result[x]['characters'].append(
                {
                    "id": f"{y}",
                    "name": f"{get_data[3]}",
                    "char_img": f"{get_data[0]}",
                    "emblem_icon": f"{get_data[1]}",
                    "char_icon": f"{get_data[2]}"
                }
            )
            print(f"Character add: {get_data[3]}")

    with open('characters_regions.json', 'w') as json_file:
        json.dump(result, json_file, indent=2)

main()