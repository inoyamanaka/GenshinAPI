from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def read_item():
    url = "https://genshin.jmp.blue/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()  # Jika respons berupa JSON
        print(data)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        
    return data


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

    if response.status_code == 200:
        response_data = response.json()
        
        # Menggabungkan hasil respons
        data = {"data": response_data, "card": f"{url}/card", 
                'constellation-1':f"{url}/constellation-1",
                'constellation-2':f"{url}/constellation-2",
                'constellation-3':f"{url}/constellation-3",
                'constellation-4':f"{url}/constellation-4",
                'constellation-5':f"{url}/constellation-5",
                'constellation-6':f"{url}/constellation-6",
                'talent-burst':f"{url}/talent-burst",
                'talent-skill':f"{url}/talent-skill",
                'talent-na':f"{url}/talent-na",
                "talent-passive-0":f"{url}/talent-passive-0",
                "talent-passive-1":f"{url}/talent-passive-1",
                "talent-passive-2":f"{url}/talent-passive-2"}
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        
    return data