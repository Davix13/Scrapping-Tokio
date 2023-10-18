#importing required Libraries

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from vimeo_downloader import Vimeo
import timeit
import urllib
from selenium.webdriver.common.by import By

#declaring variables
#Output_file=r"C:\Users\d.rodriguez\PycharmProjects\Proyecto\video_urls.xlsx"
#xls_content=[]
genres=['fashion portrait']
url='https://learning.tokioschool.com/mod/videotime/view.php?id=17330'
path = r'C:\Users\d.rodriguez\PycharmProjects\Proyecto\chromediver\.wdm\drivers\chromedriver\win32\111.0.5563\chromedriver.exe'

#loading genre using webdriver
def loadpage(driver,genre):
    driver.get(url+genre) #load the url
    driver.find_element(By.ID, "username").send_keys("david.costa1")
    driver.find_element(By.ID, "password").send_keys("Moretekila.3")
    driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()

    sleep(10) # wait for 10 secs so that website loads properly

    # scrolling the page for 2 minutes
    starttime = timeit.default_timer()
    i=0
    while i<=10:
        driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
        sleep(0.5)
        i= round(timeit.default_timer() - starttime)

    # extract the images from the page
    extractingImages(driver,genre)
def extractingImages(driver,genre):
    print(f"Extracting {genre} Video URL after 10 secs....")
    sleep(10) # let it load the post properly
    images = driver.find_elements(By.TAG_NAME,'source')
    for image in images:
        src=image.get_attribute('src')
        vlink=src.split(".sd.mp4")[0].replace("https://player.vimeo.com/external/","https://player.vimeo.com/video/")
        temp={}
        temp['Genre']=(url+genre).split('/')[-1].replace("%20"," ").upper()
        temp['Image URL']=vlink
        #xls_content.append(temp)
        download_vimeo(vlink,url,genre)

def download_vimeo(vimeo_url,embedded_on,genre):
    v = Vimeo(vimeo_url, embedded_on)
    stream = v.streams # List of available streams of different quality
    # >> [Stream(240p), Stream(360p), Stream(540p), Stream(720p), Stream(1080p)]

    filename=urllib.parse.unquote(genre)+"-"+vimeo_url.split('/')[-1]
    # Download best stream
    stream[-1].download(download_directory = 'video', filename = filename)




if __name__ =="__main__":

    #setting web driver
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    driver = webdriver.Chrome(options=options,executable_path = path)

    # looping through each keyword
    for genre in genres:
        genre=urllib.parse.quote(genre)
        loadpage(driver,genre)

    driver.close()
    xls_data = pd.DataFrame(xls_content)
    xls_data.to_excel(Output_file, engine='xlsxwriter', index=False)

