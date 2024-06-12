import urllib
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
import os

DEST = "src/assets/realms"
Path(DEST).mkdir(parents=True, exist_ok=True)

browser = webdriver.Chrome()
browser.get('https://deadbydaylight.fandom.com/wiki/Realms')
headlines = browser.find_elements(By.CLASS_NAME, "mw-headline")
names = [hl.get_attribute('id') for hl in headlines]
names = names[names.index('Realms_&_Maps') + 1: names.index("Recurring_Structures")]
print(names)
for name in names:
    browser.get(f"https://deadbydaylight.fandom.com/wiki/{name}")
    img = browser.find_element(By.XPATH, '//a[contains(@href,"RealmKeyArt")]')
    src = img.get_attribute('href')
    file = name+".png"
    urllib.request.urlretrieve(src, file)
    os.rename(file, DEST+"/"+file)