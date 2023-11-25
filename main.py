import json
from fastapi import FastAPI
import requests
import uvicorn
from collections import defaultdict

app = FastAPI()

@app.get("/")
def read_item():
    file = open('characters_data_combine.json')
    content = json.load(file)        
    return content


@app.get("/characters")
def get_character():
    file = open('characters_data_combine.json')
    content = json.load(file) 
    new_json_array = []
    grouped_data = defaultdict(list)
    
    for character_data in content:
        # print(character_data["region"])
        region = character_data["character_info"][0]["region"]
        new_json = {
            "name": character_data["name"],
            "element": character_data["character_info"][0]["element"],
            "img_namecard": character_data["character_info"][0]["img_namecard"][0]["img_namecard_2"],
            "img_in_game": character_data["list_img_char"][0]["img_char_nbg"]
        }
        new_json_array.append(new_json)
        grouped_data[region].append(new_json)
        
    response_data = {"data": [list(value) for value in grouped_data.values()]}
    return response_data

@app.get("/characters/{name}")
def get_detail_character(name: str):    
    file = open('characters_data_combine.json')
    content = json.load(file) 
    
    sorted_data = sorted(content, key=lambda x: x["name"].lower())
    print(sorted_data)
    low, high = 0, len(sorted_data) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_character = sorted_data[mid]["name"].lower()

        if mid_character == name.lower():
            return sorted_data[mid]
        elif mid_character < name.lower():
            low = mid + 1
        else:
            high = mid - 1

    return None

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
