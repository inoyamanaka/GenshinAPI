import json
import os
import re
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession

def basic_soup_load(url, params):
    url = f"{url}{params}"
    print(url)
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

def get_char_assets(url, region, index):
    param = f"{region}?char={index}"
    soup = basic_soup_load(url=url, params=param)

    target_main = soup.find('div', class_='character__main')
    target_li_main = target_main.find('li', {'class': ['swiper-slide', 'swiper-slide-active']})
    target_person = target_li_main.find('img', class_='character__person').get('src')
    target_emblem = target_li_main.find('img', class_='character__icon').get('src')
    
    target_page = soup.find('ul', class_='character__page--render')
    target_li_page = target_page.find('li', {'class': ['swiper-slide', 'swiper-slide-thumb-active', 'swiper-slide-visible']})
    target_icon = target_li_page.find('img').get('src')
    target_name = target_li_page.find('p').text

    # print(target_li_page)
    return [target_person, target_emblem, target_icon, target_name]

kota = ['mondstadt', 'liyue', 'inazuma', 'sumeru', 'Fontaine']
base_url = f"https://genshin.hoyoverse.com/en/character/"

print(get_char_assets(url=base_url, region=kota[0], index=18))