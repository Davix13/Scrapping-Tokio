import requests
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
#Definir el tipo de busqueda del elemento
from selenium.webdriver.common.by import By
from vimeo_downloader import Vimeo
import time

url= []
video = []
section = []
driver = webdriver.Chrome()
driver.get("https://learning.tokioschool.com/course/view.php?id=74&section=12")
driver.maximize_window()
driver.find_element(By.ID,"username").send_keys("david.costa1")
driver.find_element(By.ID,"password").send_keys("Moretekila.3")
driver.find_element(By.CSS_SELECTOR,"button.btn-primary").click()
modulos = driver.find_element(By.CSS_SELECTOR,"ul.flexsectionswithgrid-level-1")
#print(modulos.text)

for mod in modulos.find_elements(By.CSS_SELECTOR,"li.main"):#Los section son los modulos desplegables
    if mod.get_attribute("class") == "section main":
        section.append(mod.get_attribute("id"))
        print(mod.get_attribute("id"))
    else:
        print("Documento pdf")
time.sleep(2)
print("-------------------------")
for element in section:
    driver.find_element(By.ID,element).click()
    time.sleep(2)

for element in modulos.find_elements(By.CSS_SELECTOR,"li.modtype_videotime"):
    #print(element.get_attribute("id"))
    for a in element.find_elements(By.CSS_SELECTOR, "div.activityinstance"):
        for b in a.find_elements(By.TAG_NAME,"a"):
            #print(b.get_attribute("href"))
            url.append(b.get_attribute("href"))
#print(url)

for element in url:
    driver.get(element)
    time.sleep(5)
    for a in driver.find_elements(By.TAG_NAME,"iframe"):
        video.append(a.get_attribute("src")[:40])
print(video)





