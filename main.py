import json
from fastapi import FastAPI
import requests
import uvicorn
from collections import defaultdict

from app.domain.entities.characters_entity import CharacterEntity



app = FastAPI()

@app.get("/")
def read_item():
    file = open('all_character_data.json')
    content = json.load(file)        
    return content


@app.get("/characters")
def get_character():
    file = open('all_character_data.json')
    content = json.load(file) 
    character_entities = []
    
    
        
    for character_data in content:
        print(character_data)
        region = character_data["region"]
        character_entity = CharacterEntity(
            name=character_data["character_name"],
            element=character_data["element"],
            img_in_game=character_data["char_image"][0]["img_char_nbg"],
            img_namecard=character_data["img_namecard"][0]["img_namecard_2"]
        )
        character_entities.append(character_entity)
        
    # Optionally, you can also group the characters by region using your defaultdict
    grouped_data = defaultdict(list)
    for character_entity in character_entities:
        grouped_data[character_entity.region].append(character_entity)
        
    # Convert the grouped data to a format suitable for the response
    response_data = {"data": {region: [character.__dict__ for character in characters] for region, characters in grouped_data.items()}}
    return response_data

@app.get("/characters/{name}")
def get_detail_character(name: str):    
    file = open('all_character_data.json')
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

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
