from datetime import datetime
import requests
from bs4 import BeautifulSoup
import json

page = requests.get("https://republika.co.id/")

obj = BeautifulSoup(page.text, 'html.parser')

print('Menampilkan objek html')
print('===================')
print(obj)

print('\nMenampilkan title browser dengan tag')
print('=============================')
print(obj.title)

print('\nMenampilkan title browser tanpa tag')
print('============================')
print(obj.title.text)

print('\nMenampilkan semua tag h2')
print('=====================')
print(obj.find_all('h2'))

print('\nMenampilkan semua teks h2')
print('======================')
for publish in obj.find_all('h2'):
    print(publish.text)

print('\nMenampilkan semua teks headline')
print('=================================')
for publish in obj.find_all('div', class_='conten1'):
    print(publish.find('h2').text)

print('\nMenampilkan kategori')
print('========================')
for publish in obj.find_all('div', class_='teaser_conten1_center'):
    print(publish.find('a').text)

print('\nMenampilkan waktu publish')
print('========================')
for publish in obj.find_all('div', class_='date'):
    print(publish.text)

print('\nMenampilkan waktu scrapping')
print('=======================')
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =  ", current_time)

# Deklarasi list kosong
data = []
# Lokasi file json
f = open('E:\Kuliah\SEMESTER 2\Proyek Pengembangan perangkat lunak dekstop\Pertemuan 6\Web scrapping 1\headline.json', 'w')
for publish in obj.find_all('div', class_='conten1'):
    # append headline ke variable data
    data.append({"judul": publish.find('h2').text, "kategori": publish.find('a').text, "waktu_publish": publish.find(
        'div', class_='date').text, "waktu_scraping": now.strftime("%Y-%m-%d %H:%M:%S")})
# dump list dictionary menjadi json
jdumps = json.dumps(data, indent=2)
f.writelines(jdumps)
f.close()
