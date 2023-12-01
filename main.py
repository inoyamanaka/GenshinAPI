import json
from fastapi import FastAPI
import requests
import uvicorn
from collections import defaultdict

from characters.app.domain.entities.characters_entity import CharacterEntity

app = FastAPI()

@app.get("/")
def read_item():
    file = open('characters/all_character_data.json')
    content = json.load(file)        
    return content

@app.get("/characters")
def get_character():
    file = open('characters/all_character_data.json')
    content = json.load(file) 
    character_entities = []
    grouped_data = defaultdict(list)
     
    for character_data in content:
        index = 0
        # print(character_data)
        region = character_data["region"]
        # Determine the index based on the region
        if region == "Mondstadt":
            index = 0
        elif region == "Liyue" or region == "Snezhnaya":
            index = 1
        elif region == "Inazuma":
            index = 2
        elif region == "Sumeru":
            index = 3
        elif region == "Fontaine":
            index = 4
        character_entity = CharacterEntity(
            name=character_data["character_name"],
            element=character_data["element"],
            img_in_game=character_data["char_image"][0]["img_char_nbg"],
            img_namecard=character_data["img_namecard"][0]["img_namecard_2"]
        )
        character_entities.append(character_entity)
        
        # Optionally, you can also group the characters by region using your defaultdict
        grouped_data[index].append(character_entity)
    
    # Convert the grouped data to a format suitable for the response
    sorted_grouped_data = sorted(grouped_data.items(), key=lambda x: x[0])
    response_data = {"data": [group for index, group in sorted_grouped_data]}
    return response_data

@app.get("/characters/{name}")
def get_detail_character(name: str):    
    file = open('characters/all_character_data.json')
    content = json.load(file) 
    
    sorted_data = sorted(content, key=lambda x: x["character_name"].lower())
    print(sorted_data)
    low, high = 0, len(sorted_data) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_character = sorted_data[mid]["character_name"].lower()

        if mid_character == name.lower():
            return sorted_data[mid]
        elif mid_character < name.lower():
            low = mid + 1
        else:
            high = mid - 1

    return None


# SCHEDULE
@app.get("/schedule")
def get_material_schedule():
    character_schedule = open('artefacts/datasources/character_material_schedule.json')
    character_content = json.load(character_schedule)
    
    weapon_schedule = open('artefacts/datasources/weapon_ascension_schedule.json')
    weapon_content= json.load(weapon_schedule)
    
    response_data = {"character_schedule": character_content, "weapon_schedule":weapon_content}
    return response_data

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
