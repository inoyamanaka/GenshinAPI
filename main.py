import json
from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def read_item():
    file = open('characters_data_combine.json')
    content = json.load(file)        
    return content


@app.get("/characters")
def get_character():
    url = "https://genshin.jmp.blue/characters"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()  # Jika respons berupa JSON
        print(data)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        
    return data

@app.get("/characters/{name}")
def get_detail_character(name: str):    
    url = f"https://genshin.jmp.blue/characters/{name}"
    response = requests.get(url)

