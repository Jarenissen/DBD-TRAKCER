import urllib
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
import os

DEST = "src/assets/maps"
Path(DEST).mkdir(parents=True, exist_ok=True)

def try_get(t):
    try:
        return t.find_element(By.TAG_NAME, "center").find_element(By.TAG_NAME, "a").get_attribute("href")
    except:
        return None

browser = webdriver.Chrome()
browser.get('https://deadbydaylight.fandom.com/wiki/Realms')
tables = browser.find_elements(By.CLASS_NAME, "wikitable")
names = [[n.find_element(By.TAG_NAME, "a").get_attribute("href") for n in t.find_elements(By.TAG_NAME, "center")] for t in tables]
flat = [x for xs in names for x in xs]

for link in flat:
    browser.get(link)

    img = browser.find_element(By.CLASS_NAME, "infoboxtable").find_element(By.CLASS_NAME, "image")
    src = img.get_attribute('href')
    file = link.split("/")[-1]+".png"
    urllib.request.urlretrieve(src, file)
    os.rename(file, DEST+"/"+file)