from datetime import datetime
from selenium import webdriver
import json

PATH = "E:\Kuliah\SEMESTER 2\Proyek Pengembangan perangkat lunak dekstop\Pertemuan 6\Web scrapping 2\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.billboard.com/charts/billboard-korea-100/")

x = datetime.now()

billboard = []


for song in driver.find_elements_by_class_name("o-chart-results-list-row"):
    print(song.text)
    for img in song.find_elements_by_class_name("c-lazy-image__img"):

        billboard.append(
            {"Ranking": song.text.split("\n")[0],
             "Judul": song.text.split("\n")[1],
             "Penyanyi": song.text.split("\n")[2],
             "weeks_on_chart": song.text.split("\n")[5],
             "waktu_scraping": x.strftime("%Y-%m-%d pukul %H:%M:%S"),
             "Image": img.get_attribute("src")
             }
        )

scrap = open("scrap.json", "w")
json.dump(billboard, scrap, indent=6)
scrap.close()
driver.quit()
