import requests
from bs4 import BeautifulSoup
response = requests.get("https://bulbapedia.bulbagarden.net/wiki/Wartortle_(Pok%C3%A9mon)")
page = BeautifulSoup(response.content,"html.parser")
title = page.find("title")
print(title)

movesResponse = requests.get("https://bulbapedia.bulbagarden.net/wiki/Wartortle_(Pok%C3%A9mon)#Learnset")
movesInfo = BeautifulSoup(response.content,"html.parser")
learnset = movesInfo.find_all(text=True)
print(learnset)
