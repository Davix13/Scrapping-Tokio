import requests
from bs4 import BeautifulSoup
from vimeo_downloader import Vimeo

# URL del video
url = 'https://learning.tokioschool.com/mod/videotime/view.php?id=18502'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Accept-Language': 'es-ES,es;q=0.9',
    'Referer': 'https://learning.tokioschool.com/',
    'Accept': 'video/mp4',
    'Range': 'bytes=0-',
}

mis_cookies = {"__cf_bm": "Fr5EDSKcA1uLNgbwWIZ8ZTfJVpmbeATTvfCLNqFjh_A-1707299366-1-ARW7LBPkdTMD4XtvD5eRtm4bEhovVVodSr/DcGl8PdWCDl5ruVUxvpJJuQ7/UBnSPDSpVqYtlKyXi2VKhgeFj+k="}

# Realiza la solicitud a la página del video
response = requests.get(url, headers=headers, cookies=mis_cookies)

# Verifica si la solicitud fue exitosa (código de respuesta 200)
if response.status_code == 200:
    # Parsea el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encuentra la etiqueta script con datos JSON
    script_tag = soup.find('script', type='application/ld+json')

    # Verifica si se encontró la etiqueta script
    if script_tag:
        # Extrae el contenido JSON de la etiqueta script
        json_data = script_tag.string

        # Parsea la cadena JSON
        video_info = json.loads(json_data)

        # Obtiene la URL del video
        video_embed_url = video_info.get('embedUrl')

        if video_embed_url:
            try:
                # Intenta descargar el video con vimeo_downloader
                vimeo = Vimeo(video_embed_url, url)
                video_stream = vimeo.streams.get_by_resolution('720p')  # Puedes cambiar la resolución según tus preferencias
                video_stream.download(download_directory='.', filename='video')

                print('Descarga exitosa.')
            except Exception as e:
                print(f'Error al intentar descargar el video: {e}')
        else:
            print('No se pudo obtener la URL del video.')

    else:
        print('No se encontró la etiqueta script con datos JSON en la página.')

else:
    print('La solicitud HTTP no fue exitosa. Código de respuesta:', response.status_code)
