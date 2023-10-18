#Módulos de terceros
import undetected_chromedriver as uc

def iniciar_webdriver(headless=False,pos="maximizada"):

    """
    Inicia un navegador de Chrome y devuelve el objeto webdriver instaciado.
    pos: indica la posicion del navegador en la pantalla ("maximizada\izquierda\derecha)
    """
    options = uc.ChromeOptions()
    #desactivamos el guardado de credenciales
    options.add_argument("--password-store=basic")
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service":False,
            "profile.password_manager_enabled":False,
        },
    )
    #Iniciamos el driver
    driver = uc.Chrome(
        options=options,
        headless=headless,
        log_level=3,
    )
    #posicionamos la ventana segun corresponda
    if not headless:
        #Maximizamos la ventan
        driver.maximize_window()
        if pos != "maximizada":
            #obtenemos la resolucion de la ventana
            ancho, alto = driver.get_window_size().values()
            if pos == "izquierda":
                #posicionamos la ventana en la mitad izquierda dela pantalla
                driver.set_window_rect(x=0,y=0,width=ancho//2,height=alto)
            elif pos == "derecha":
                driver.set_window_rect(x=ancho//2,y=0,width=ancho//2,height=alto)
    return driver


