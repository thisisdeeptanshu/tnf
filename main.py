# sc-1xf18x6-0 haVRLx AssetsSearchView--assets nft containers
# sc-1xf18x6-0 sc-1twd32i-0 sc-1wwz3hp-0 cIOCCU kKpYwv kuGBEl nft locations container


import os
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

locationsContainer = []
names = []
driver = webdriver.Chrome("chromedriver.exe")

driver.get("https://www.opensea.io")
time.sleep(2)
allElems = driver.find_elements(By.XPATH, "//div[@class='sc-7qr9y8-0 iUvoJs']")
for i in range(len(allElems)):
    if allElems[i].text[len(allElems[i].text) - 1] != "%":
        try:
            float(allElems[i].text)
        except:
            print(allElems[i].text)
            names.append(allElems[i].text)
            locationsContainer.append(allElems[i].find_element(By.XPATH, "../../..").get_attribute("href"))
            

for i in range (len(locationsContainer)):
    os.mkdir(names[i])
    os.chdir(names[i])

    driver.get(locationsContainer[i])
    time.sleep(5)

    nfts = driver.find_element(By.XPATH, "//div[@class='sc-1xf18x6-0 haVRLx AssetsSearchView--assets']")
    j = 0
    for nft in nfts.find_elements(By.TAG_NAME, "img"):
        nft.screenshot(f"{i}_{j}.png")
        j += 1
    
    os.chdir("..")

driver.close()