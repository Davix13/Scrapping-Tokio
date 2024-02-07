import requests


url = 'https://player.vimeo.com/video/875981475'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'es-ES,es;q=0.9',
    'Referer': 'https://learning.tokioschool.com/',  # Cambia esto a la URL de la página desde la cual proviene la solicitud
    'Accept': 'video/mp4',
    'Range': 'bytes=0-',
}

mis_cookies={"__cf_bm":"Fr5EDSKcA1uLNgbwWIZ8ZTfJVpmbeATTvfCLNqFjh_A-1707299366-1-ARW7LBPkdTMD4XtvD5eRtm4bEhovVVodSr/DcGl8PdWCDl5ruVUxvpJJuQ7/UBnSPDSpVqYtlKyXi2VKhgeFj+k="}

response = requests.get(url, headers=headers,cookies=mis_cookies)
print(response.status_code)


# Guarda el contenido HTML en un archivo de texto
with open('pagina.html', 'w', encoding='utf-8') as archivo:
    archivo.write(response.text)

print('Contenido HTML guardado en "pagina.html"')



