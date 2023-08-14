#!/usr/bin/python
import json, os
import urllib.request
import urllib.parse
from datetime import datetime

url = "https://api.jikan.moe/v4/anime?q="

def getAnime(query):
    response = urllib.request.urlopen(url + urllib.parse.quote(query))
    data = response.read()
    return json.loads(data.decode("utf-8"))

def calculate_weeks(date_string):
    date_format = "%Y-%m-%d"
    start_date = datetime.strptime(date_string, date_format)
    current_date = datetime.now()
    weeks = (current_date - start_date).days // 7
    return weeks

inputAnime = str(input("Anime: "))

listAnime = getAnime(inputAnime)

os.system("clear")

for i, anime in enumerate(listAnime["data"]):
	print(f"{str(i+1)}.", anime["title"], "(", anime["type"], ")")

print("-"*20)
try:
	inputAnimeID = int(input("Anime: "))
except:
	print("-"*20)
	print("Input not valid")
	exit()

try:
	i = listAnime["data"][inputAnimeID-1]
except:
	print("-"*20)
	print("Anime not found")
	exit()

duration = i["duration"]
episodes = i["episodes"]

if episodes == None:
	episodes = calculate_weeks(i["aired"]["from"][:10])

minutes = int(duration[:2])*episodes

os.system("clear")
print("-"*20)
print("📛 Title:", i["title"])
print("-"*20)
print("🔥 Episodes:", episodes)
print("⏰ Duration:", duration)
print("-"*20)
print("=> 😲 Total minutes:", minutes)
print("=> 😵 Total hours:", "{:.2f}".format(minutes/60))
print("=> 💀 Total days (psycho mode) [24 at day]:", "{:.2f}".format(minutes/1440))
print("=> 🫠 Total days (less psycho mode) [6h at day]:", "{:.2f}".format(minutes/1440*4))
print("=> 😋 Total days (normal mode) [3h at day]:", "{:.2f}".format(minutes/1440*8))
