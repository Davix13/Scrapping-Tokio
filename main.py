#Instalar automaticamente chromedriver
from webdriver_manager.chrome import ChromeDriverManager
#Driver de selenium
from selenium import webdriver
#Servicio de webdriver
from selenium.webdriver.chrome.service import Service
#Para modificar las opciones de webdriver en chrome
from selenium.webdriver.chrome.options import Options
#BEAUTIFULSOUP
from bs4 import BeautifulSoup


#Instalamos la version de chromedriver correspondiente .Nos devuelve la ruta completa al ejecutarlo
ruta_chromedriver = ChromeDriverManager(path=".\.chromedriver").install()
#Instanciamos el servicio de chromedriver
s = Service(ruta_chromedriver)
#Instanciamos webdriver de selenium con Chrome
driver = webdriver.Chrome(service=s)
#Url de la petición
url = "https://es.tradingview.com/chart/"
#Abrimos la página
driver.get(url)
#Preparamos la sopa
soup= BeautifulSoup(driver.page_source,"html.parser")
