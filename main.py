import json
from fastapi import FastAPI
import requests
import uvicorn

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
    
    for character_data in content:
        print(character_data["list_img_char"][0]["img_char_nbg"])
        new_json = {
            "name": character_data["name"],
            "element": character_data["character_info"][0]["element"],
            "img_namecard": character_data["character_info"][0]["img_namecard"][0]["img_namecard_2"],
            "img_in_game": character_data["list_img_char"][0]["img_in_game"]
        }
        new_json_array.append(new_json)
    # Mengubah array objek Python menjadi string JSON
    # new_json_str = json.dumps(new_json_array, indent=2)
    response_data = {"data": new_json_array}
    return response_data

@app.get("/characters/{name}")
def get_detail_character(name: str):    
    url = f"https://genshin.jmp.blue/characters/{name}"
    response = requests.get(url)

@app.get("/regions")
def get_char_regions():    
    file = open('characters_data_combine.json')
    content = json.load(file) 
    new_json_array = []
    
    for region_data in content:
        print(region_data["list_img_char"][0]["img_char_nbg"])
        new_json = {
            "name": region_data["name"],
            "element": region_data["character_info"][0]["element"],
            "img_namecard": region_data["character_info"][0]["img_namecard"][0]["img_namecard_2"],
            "img_in_game": region_data["list_img_char"][0]["img_in_game"]
        }
        new_json_array.append(new_json)
    # Mengubah array objek Python menjadi string JSON
    # new_json_str = json.dumps(new_json_array, indent=2)
    response_data = {"data": new_json_array}
    return response_data

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
