# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



#Definir el tipo de busqueda del elemento
from selenium.webdriver.common.by import By
from vimeo_downloader import Vimeo
import time

url = []
url2 = []
section = []
video = []
modulo=[]



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://learning.tokioschool.com/course/view.php?id=74")
driver.maximize_window()
driver.find_element(By.ID,"username").send_keys("david.costa1")
driver.find_element(By.ID,"password").send_keys("Moretekila.3")
driver.find_element(By.CSS_SELECTOR,"button.btn-primary").click()
etapas = driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/div/div/section/div/div/div/div/div[2]")

for element in etapas.find_elements(By.CSS_SELECTOR,"div.col-xs-12"):
    for a in element.find_elements(By.CSS_SELECTOR,"div.thumbnail"):
        modulo.append(a.find_element(By.TAG_NAME,"a").get_attribute("href"))
print(modulo)

for element in modulo:
    driver.get(element)
    #bloque 2
    modulos = driver.find_element(By.CSS_SELECTOR, "ul.flexsectionswithgrid-level-1")
    # print(modulos.text)

    for mod in modulos.find_elements(By.CSS_SELECTOR, "li.main"):  # Los section son los modulos desplegables
        if mod.get_attribute("class") == "section main":
            mod.click()
            time.sleep(1)

    for b in modulos.find_elements(By.CSS_SELECTOR, "li.modtype_videotime"):
        #print(b.get_attribute("id"))
        #bueno
        for a in b.find_elements(By.CSS_SELECTOR, "div.activityinstance"):
            for c in a.find_elements(By.TAG_NAME, "a"):
                print(c.get_attribute("href"))
                url.append(c.get_attribute("href"))
for element in url:
    driver.get(element)
    time.sleep(2)
    for a in driver.find_elements(By.TAG_NAME, "iframe"):
        if len(a.get_attribute("src")) > 40:
            video.append(a.get_attribute("src")[:40])
            print(a.get_attribute("src")[:40])
        else:
            print("espacio en blanco")
    time.sleep(1)

    # embedded_on is  the URL of site video is embedded on without query parameters.
numero = 0
while numero <= len(url):
    v = Vimeo(video[numero], url[numero])
    stream = v.streams  # List of available streams of different quality
    # >> [Stream(240p), Stream(360p), Stream(540p), Stream(720p), Stream(1080p)]

    # Download best stream
    ruta = str(video[numero][31:])
    stream[-1].download(download_directory='video', filename= ruta)
    numero += 1


'''
    # Download video of particular quality, example '540p'
    for s in stream:
        if s.quality == '540p':
            s.download(download_directory='video',filename=video[numero])
            numero +=1
            break
    else:  # If loop never breaks
        print("Quality not found")
'''

