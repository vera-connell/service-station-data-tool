import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.caltex.co.nz/find-a-station/")
soup = BeautifulSoup(response.content,"html.parser")

#display status code of html request and page title

print("response status code:" + str(response.status_code))

print(soup.title.text)

#select an element

h1 = soup.find('h1')

print(soup.text)



