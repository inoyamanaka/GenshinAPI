import requests

url = "https://genshin.jmp.blue/"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Jika respons berupa JSON
    print(data)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")