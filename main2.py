#Instalar automaticamente chromedriver
from webdriver_manager.chrome import ChromeDriverManager
#Driver de selenium
from selenium import webdriver
#Servicio de webdriver
from selenium.webdriver.chrome.service import Service
#Para modificar las opciones de webdriver en chrome
from selenium.webdriver.chrome.options import Options

#Definir el tipo de busqueda del elemento
from selenium.webdriver.common.by import By


def iniciar_chrome():
    """Inicia chrome con los parámetros indicados y devuelve el driver"""

    #Instalamos la version de chromedriver que nos corresponde
    ruta = ChromeDriverManager(path=".\.chromedriver").install()
    #Opciones de CHROME:
    options = Options()#Instancia las opciones de chorme
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    options.add_argument(f"user_agent={user_agent}")#Define un user agent personalizado
    options.add_argument("--headless")#Para ejecutar chrome sin abrir la ventana
    #options.add_argument("--window-size=1000,1000")#Para configurar el alto y ancho de la ventana
    options.add_argument("--start-maximized") #Para maximizar la ventana de chrome(solo funciona si la anterior la tenemos comentada)
    options.add_argument("--disable-web-security")#Deshabilita la politica del mismo origen
    options.add_argument("--disable-extensions")#Deshabilita las extensiones de chrome
    options.add_argument("--disable-notifications")#Para bloquear las notificaciones de chrome
    options.add_argument("--ignore-certificate-errors")#Para ignorar el aviso de su conexion no es privada
    options.add_argument("--no-sandbox")#deshabilita el modo sandbox
    options.add_argument("--log-level=3")#Para que chromedriver no muestre nada en la terminal
    options.add_argument("--allow-running-insecure-content")#Desactiva el aviso de "Contenido no seguro"
    options.add_argument("--no-default-browser-check")#Evita el aviso de que chrome no es le navegador predeterminado
    options.add_argument("--no-first-run")#Para no usar proxy, sino conexiones directas
    options.add_argument("--no-proxy-server")#Para  no usar proxy , sino conexiones directas
    options.add_argument("--disable-blink-features=AutomationControlled")#Evita que nos detecte como bot

    #Parametros a omitir en el incio de chromedriver
    exp_opt = [
        "enable-automation",#Para que no muestre la notificacion
        "ignore-certificate-errors",#para ignorar errores de certificados
        "enable-logging"#para que no se muestre en la terminal "Devtools listening on...
    ]
    options.add_experimental_option("excludeSwitches",exp_opt)

    #Parametros que definen preferencias en chromdriver
    prefs = {
        "profile.default_content_setting_values.notifications": 2,#Notificaciones : 0 = preguntar, 1 = permitir , 2= no permitir
        "intl.accept_languages" : ["es-ES","es"],#Idioma
        "credentials_enable_service": False #Para evitar que chrome nos pregunte si queremos guardar la contraseña
    }

    options.add_experimental_option("prefs",prefs)

    #Instanciamos el servicio de chromedriver
    s = Service(ruta)

    #Instanciamos webdriver
    driver = webdriver.Chrome(service=s,options=options)#añadimos el argumento options
    #Devolvemos el driver
    return driver

#MAIN
if __name__ == "__main__":
    driver = iniciar_chrome()
    url = "https://learning.tokioschool.com/mod/videotime/view.php?id=17330"
    driver.get(url)
    #video = driver.find_element(By.CSS_SELECTOR,"canvas.chart-page unselectable i-no-scroll").text
    #url = driver.find_element(By.CSS_SELECTOR,"canvas.chart-page unselectable i-no-scroll").get_attribute("src")
    url = driver.find_element(By.CSS_SELECTOR,"video").get_attribute("src")
    print(url)
    driver.quit()
