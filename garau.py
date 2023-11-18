import json
import re
import csv
import pandas as pd
from bs4 import BeautifulSoup
import requests

html = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vRq-sQxkvdbvaJtQAGG6iVz2q2UN9FCKZ8Mkyis87QHFptcOU3ViLh0_PJyMxFSgwJZrd10kbYpQFl1/pubhtml#').text
soup = BeautifulSoup(html, "lxml")
tables = soup.find_all("table")
index = 0

for table in tables:
    # Baca data dari tabel dan simpan dalam format CSV
    with open(f"{index}.csv", "w", encoding="utf-8", newline="") as csv_file:
        wr = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        wr.writerows([[td.text for td in row.find_all("td")] for row in table.find_all("tr")])
    index += 1


file = open("characters_data/char_9.txt", "r")
content = file.read()


text = f"""
{content}
"""

# Pisahkan teks menjadi baris-baris
lines = text.split('\n')

current_character = None
found = False
index = 0
result = []

# Membuat pola ekspresi reguler untuk mencocokkan angka yang diikuti oleh tanda titik '.'
pattern = re.compile(r'\d+\.')

name = ''
role = ''
weapon = ''
artifact = ''
mainstat = ''
substat = ''
talent_priority = ''


for line in lines:
    # print('------element----------------')
    print(line)
    # print('-----------------------')
    if ',ROLE,EQUIPMENT,ARTIFACT STATS,TALENT PRIORITY,ABILITY TIPS' in line:
        index = 0
        found = True
        print('------------------------------------------------------------------')
        elements = line.split(',')

        # Mengambil kata pertama dan kedua
        name = elements[1].replace(" ", "_").strip('"')
        # Split the string by underscores, capitalize each word, and join them back
        

    if found:
        # Proses atau cetak elemen atau indeks setelahnya
        if index == 2:
            elements = line.split(',')
            
            # cleaning role
            # print(line)
            role = elements[2].replace('âœ©', '').strip('"')
            
            # cleaning weapon
           
            
            weapon = elements[3].replace('âœ©', '').replace("[R5]", "").replace('"', '').replace('*', '').strip('"')
            weapon = re.split(pattern, weapon)
            weapon = [item.strip() for item in weapon if item]   
            
            # cleaning artifact
            artifact = elements[4].replace('âœ©', '').replace("[R5]", "").replace('"', '').replace('*', '').strip('"')
            artifact = re.split(pattern, artifact)
            artifact = [item.strip() for item in artifact if item]  
            
            # cleaning artifact stat
            mainstat = elements[5].replace('"', '').strip('"')
            
            # cleaning artifact stat 2
            substat = elements[6].replace('"', '').replace('*', '').strip('"')
            substat = re.split(pattern, substat)
            substat = [item.strip() for item in substat if item] 
            
            # talent priority
            # talent_priority = elements[7].replace('"', '').replace('*', '').strip('"')
            # talent_priority = re.split(pattern, talent_priority)
            # talent_priority = [item.strip() for item in talent_priority if item] 
            
            result.append({"name": name.capitalize(),
                        "role":role,
                        'recommended_weapon': weapon,
                        'recommended_artifact': artifact,
                        'mainstat':mainstat,
                        'substat':substat,
                        # 'talent_priority':talent_priority
                        })
 
    index += 1
# Menyimpan hasil ke dalam file JSON
with open('output.json', 'w') as json_file:
    json.dump(result, json_file, indent=2)