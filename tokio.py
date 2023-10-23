# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#Modulo para gestionar nuestro SO
import os

from selenium.common import NoSuchElementException
#Definir el tipo de busqueda del elemento
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from vimeo_downloader import Vimeo
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#lista para guardar urls
personal= [] #URL de los menus
cursos = {}#URL de los cursos
modulos = [] #URL de los modulos de los cursos
enlaceModulos = [] #URL de los modulos de un curso.
nombreCarpetas = [] #URl de las carpetas de los apartados de los modulos
urlDocumentos = []

driver.get("https://learning.tokioschool.com/my")
driver.maximize_window()

#Options instance
op = Options()

#Iniciamos sesión en la página web
driver.find_element(By.ID,"username").send_keys("david.costa1")
driver.find_element(By.ID,"password").send_keys("Moretekila.3")

#Pulsamos en entrar
driver.find_element(By.CSS_SELECTOR,"button.btn-primary").click()
time.sleep(1)


#Pulsamos en cursos
contenedor = driver.find_element(By.CSS_SELECTOR,"div.row")
for element in contenedor.find_elements(By.TAG_NAME,"a"):
    personal.append(element.get_attribute("href"))
#print(personal)

#Ingresamos en mis cursos para conseguir las urls de los cursos
driver.get(personal[0])
pagina = driver.find_element(By.CSS_SELECTOR,"div.itop_course_overview-box")
time.sleep(1)

#Creamos un diccionario con el titulo del curso y la página
for element in pagina.find_elements(By.CSS_SELECTOR,"div.enrolled"):
        for curso in element.find_elements(By.CSS_SELECTOR,"a.itop_course_overview-linkbox"):
            cursos[curso.find_element(By.TAG_NAME, "h6").text] = curso.get_attribute("href")
#print(cursos.keys())
#En "cursos" tenemos un diccionario con el nombre del curso y la url


#ruta de carpeta
rutaCarpeta = "/Users/d.rodriguez/Desktop/Cursos Tokio/"

#Crear carpeta
if os.path.exists(rutaCarpeta):
    print("La carpeta {} ya existe.".format(rutaCarpeta))
else:
    os.mkdir(rutaCarpeta)

#Vamos a crear las carpetas de cada curso
for element in cursos.keys():
    element = element.replace(":","")
    if os.path.exists("{}{}".format(rutaCarpeta,element)):
        print("Carpeta ya existe")
    else:
        os.mkdir("{}{}".format(rutaCarpeta,element))
        print("Carpeta Creada {}{}".format(rutaCarpeta,element))

for element in cursos.keys():
    element = element.replace(":", "")
    os.chdir(rutaCarpeta + element)#Nos movemos a la carpeta de cada curso
    #print(os.getcwd())
    time.sleep(1)

#Cogemos los enlaces de los cursos para acceder a ellos
for element in cursos.values():
    driver.get(element)
    print(element)
    time.sleep(1)
    try:
        temas = driver.find_element(By.CSS_SELECTOR, "div.thumbnails")
        time.sleep(1)
        try:
            for enlace in temas.find_elements(By.CSS_SELECTOR,"div.thumbnail"):
                enlaceModulos.append(enlace.find_element(By.TAG_NAME,"a").get_attribute("href"))
                print(enlace.find_element(By.TAG_NAME,"h4").text)

        except:
            print("No tiene enlace")


    except NoSuchElementException as e:
        print("No tiene modulos")

print(enlaceModulos) #Tenemos los enlaces de cada modulo dentro de cada curso(Los que podemos tener ya que tenemos que cursar el curso para obtener todos)
'''
#Ahora vamos a recorre cada modulo para desplegar sus temas
for element in enlaceModulos:
    driver.get(element)
    try:
        apartados = driver.find_element(By.CSS_SELECTOR, "ul.flexsectionswithgrid-level-1")
        try:
            for mod in apartados.find_elements(By.CSS_SELECTOR, "li.main"):  # Los section son los modulos desplegables
                if mod.get_attribute("class") == "section main":
                    mod.click()
                    time.sleep(1)
            try:
                for documentos in apartados.find_elements(By.TAG_NAME, "a"):
                    if documentos.get_attribute("class") == "accordion-toggle":
                        nombreCarpetas.append(documentos.text)
                    else:
                        urlDocumentos[documentos.find_element(By.CSS_SELECTOR,"span.instancename").text] = documentos.get_attribute("href")
            except:
                pass
        except:
            pass
    except:
        pass
print(nombreCarpetas)
print("--------------------")
print(urlDocumentos)


'''