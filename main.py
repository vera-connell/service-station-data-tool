import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.caltex.co.nz/find-a-station/")
page = BeautifulSoup(response.content,"html.parser")

stationHeadings = []

for element in page.find_all(class_="locator-result__heading"):
  print(element.text)
  stationHeadings.append(element.text)

for x in stationHeadings:
  print(x)

#display status code of html request

print("response status code:" + str(response.status_code))




