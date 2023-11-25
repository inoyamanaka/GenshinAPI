from bs4 import BeautifulSoup
import requests


html = requests.get(f'https://genshin.gg/characters/yoimiya/').text
soup = BeautifulSoup(html, "lxml")


# GET SKILLS AND CONSTELLATIONS
# output = soup.find_all('div', class_='character-skill')

# for index in range (0, len(output)):
#     type_skill = output[index].find('div', class_='character-skill-header').find('h3').text
#     skill_img =  output[index].find('img', class_='character-skill-icon')['src']
#     skill_name = output[index].find('div', class_='character-skill-body').find('h4').text
#     skill_description = output[index].find('div', class_='character-skill-body').find('div', class_='character-skill-description').text


#     # print(len(output))
#     print(type_skill)
#     print(skill_img)
#     print(skill_name)
#     print(skill_description)
    
#     print('===================================================')



# GET BEST TEAMS
# teams = soup.find_all('div', class_='character-team')
# for team in teams:
    
#     print(team.find('div', class_='character-team-name').text)
#     for i in range (0, 4):
#         print(team.find('div', class_='character-team-characters').find_all('img')[i]['src'])
        
 
# GET BEST WEAPONS AND ARTEFACTS
weapons = soup.find_all('div', class_='character-build-section')
weapon_item_count = len(weapons[0].find_all('div', class_='character-build-weapon'))
artifact_item_count = len(weapons[1].find_all('div', class_='character-build-weapon'))

for i in range (0, weapon_item_count):
    print(weapons[0].find_all('div', class_='character-build-weapon')[i].find('img')['src'])
    print(weapons[0].find_all('div', class_='character-build-weapon')[i].find('img')['alt'])

for i in range (0, artifact_item_count):
    print('===================================================')
    
    artifact_set = len((weapons[1].find_all('div', class_='character-build-weapon')[i].find_all('img')))
    for j in range (0, artifact_set):
        print(weapons[1].find_all('div', class_='character-build-weapon')[i].find_all('img')[j]['src'])
        print(weapons[1].find_all('div', class_='character-build-weapon')[i].find_all('img')[j]['alt'])
        print(weapons[1].find_all('div', class_='character-build-weapon')[i].find_all('div', class_='character-build-weapon-count')[j].text)
    

# GET SUBSTATS
# stat = soup.find_all('div', class_='character-stats')
# for i in range (0, len(stat[0].find_all('div', class_='character-stats-item'))):
#     print(stat[0].find_all('div', class_='character-stats-item')[i].text)