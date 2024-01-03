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
modulos = {} #URL de los modulos de los cursos
nombreModulos = []#Nombre de los modulos
enlaceModulos = [] #URL de los modulos de un curso.
carpetasUnidades = []#Nombre de las carpetas de cada Curso
cabeceras=[]#Cabeceras de los cursos
nombreCarpetas = [] #URl de las carpetas de los apartados de los modulos
urlDocumentos = []
diccionarioCarpetas = {}
cabecera = None

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
#En cursos tenemos un diccionario con el nombre del curso y la url


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

course = cursos.items()

#Entramos en cada curso para extraer las url de los modulos
for clave,valor in course:
    clave = clave.replace(":", "")
    os.chdir(rutaCarpeta + clave)#Nos movemos a la carpeta de cada curso
    print(os.getcwd())
    time.sleep(1)
    driver.get(valor)
    #print(valor)
    time.sleep(1)
    try:
        temas = driver.find_element(By.CSS_SELECTOR, "div.thumbnails")
        time.sleep(1)
        try:
            for enlace in temas.find_elements(By.CSS_SELECTOR,"div.thumbnail"):
                #print(enlace.find_element(By.TAG_NAME,"a").get_attribute("href"))
                enlace = enlace.find_element(By.TAG_NAME,"a").get_attribute("href")
                if enlaceModulos.count(enlace) < 1:
                    enlaceModulos.append(enlace)
                    #print(enlace)
                    if len(enlace) < 55:#Eliminamos los enlaces que no son section
                        enlaceModulos.remove(enlace)
                        print("Se ha eliminado {}".format(enlace))
                    else:
                        print("Enlace correcto {}".format(enlace))
                else:
                    print("Ya existe")
        except:
            print("No tiene enlace")


    except NoSuchElementException as e:
        javaEnlace = driver.find_element(By.CSS_SELECTOR,"section.grid-unidades")
        for link in javaEnlace.find_elements(By.CSS_SELECTOR,"div.grid-item"):
            link = link.find_element(By.TAG_NAME,"a").get_attribute("href")
            enlaceModulos.append(link)
            print(link)

#print(len(enlaceModulos))

#Entramos en cada modulo para extraer el nombre del mismo

for element in enlaceModulos:
    driver.get(element)
    time.sleep(1)
    try:
        cabecera = driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/header/div/div/div/div[1]/div/div/div/h1").text
        os.chdir(rutaCarpeta + cabecera)
        #print(cabecera)
        print(os.getcwd())
        if cabecera in cabeceras:
            print("Ya existe: {}".format(cabecera))
        else:
            cabeceras.append(cabecera)
            #print("Agregamos {} a la lista".format(cabecera))


        nombre = driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div/div/section/div/div/div/div/ul/li/div/div/div/div/div/table/thead/tr/th[4]/h1/strong/span").text
        print("nombre:{}".format(nombre))
        carpetasUnidades.append(nombre)
        if os.path.exists("{}{}/{}".format(rutaCarpeta, cabecera,nombre)):
            print("Carpeta ya existe: {}".format(nombre))
        else:
            os.mkdir("{}{}/{}".format(rutaCarpeta, cabecera,nombre))
            print("Carpeta Creada {}{}/{}".format(rutaCarpeta, cabecera,nombre))

    except:
        try:
            titulo = driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div/div/section/div/div/div/div/ul/li/div/div/div/ul[1]/li/div/div/div[2]/div/div/div/p/strong/span/span").text
            print("titulo:{}".format(titulo))
            titulo = titulo.replace(":","-")
            carpetasUnidades.append(titulo)
            if os.path.exists("{}{}/{}".format(rutaCarpeta,cabecera,titulo)):
                print("Carpeta :{}{}/{} existe".format(rutaCarpeta,cabecera,titulo))
            else:
                os.mkdir("{}{}/{}".format(rutaCarpeta, cabecera, titulo))
                print("Carpeta Creada {}{}/{}".format(rutaCarpeta, cabecera, titulo))

        except:
            try:
                title = driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div/div/section/div/div/div/div/ul/li/div/div/div/div/div/table/thead/tr/th[3]/h1/span/strong/span").text
                print("title:{}".format(title))
                carpetasUnidades.append(title)
                if os.path.exists("{}{}/{}".format(rutaCarpeta, cabecera, title)):
                    print("Carpeta ya existe")
                else:
                    os.mkdir("{}{}/{}".format(rutaCarpeta, cabecera, title))
                    print("Carpeta Creada {}{}/{}".format(rutaCarpeta, cabecera, title))
            except:
                try:
                    java = driver.find_element(By.CSS_SELECTOR,"h2.auto").text
                    java = java.replace("¿","")
                    java = java.replace("?", "")
                    print("Java : {}".format(java))
                    cabecera = driver.find_element(By.XPATH,"/html/body/main/header/nav/a[1]/span/span[2]").text
                    os.chdir(rutaCarpeta + cabecera)
                    if os.path.exists("{}{}/{}".format(rutaCarpeta,cabecera,java)):
                        print("Carpeta {} ya existe".format(java))
                    else:
                        os.mkdir("{}{}/{}".format(rutaCarpeta,cabecera,java))
                        print("Carpeta creada {}{}/{}".format(rutaCarpeta,cabecera,java))
                except:
                    print("No tiene cabecera")

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

                else:
                    print("Error de despliegue")
                url = mod.find_element(By.TAG_NAME,"a")
                print(url)
        except:
            print("Error de try")
    except:
        print("Error de try")