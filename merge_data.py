import json

# Baca data dari file pertama
with open('output.json', 'r') as file:
    data1 = json.load(file)

# Baca data dari file kedua
with open('characters_img_urls.json', 'r') as file:
    data2 = json.load(file)

# Gabungkan data berdasarkan nama karakter
for entry in data1:
    character_name = entry['name'].capitalize()
    if character_name in data2:
        entry['image_urls'] = data2[character_name]

# Simpan hasil gabungan ke dalam file JSON
with open('combined_data.json', 'w') as json_file:
    json.dump(data1, json_file, indent=2)

# Tampilkan hasil gabungan
print(json.dumps(data1, indent=2))
