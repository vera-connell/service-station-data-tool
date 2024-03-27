import time
import os.path
#import requests
#from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#Config for Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")

#Extract Paths for chrome and set them appropriately

homedir = os.path.expanduser("~")
chrome_options.binary_location = f"{homedir}/chrome/linux-123.0.6312.86/chrome-linux64/chrome"
webdriver_service = Service(f"{homedir}/chromedriver/linux-125.0.6381.0/chromedriver-linux64/chromedriver")

#Select browser

browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

#Request a page & print the description

browser.get("https://www.caltex.co.nz/find-a-station/")
description = browser.find_element(By.NAME, "description").get_attribute("content")
print(f"{description}")

#response = requests.get("https://www.caltex.co.nz/find-a-station/")
#soup = BeautifulSoup(response.content,"html.parser")

#display status code of html request and page title

#print("response status code:" + str(response.status_code))

#print(soup.title.text)

#select an element

#h1 = soup.find('h1')

#print(soup.text)



