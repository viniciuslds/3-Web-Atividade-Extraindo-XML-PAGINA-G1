from typing import Text
import requests
import csv
import re


url = 'https://g1.globo.com/rss/g1'

url_final = url
response = requests.get(url_final)
response.status_code
response.content

#Extraindo dados do xml
from xml.etree import ElementTree
conteudo = ElementTree.fromstring(response.content)
type(conteudo)
conteudo.tag
conteudo.find('channel').findtext('title')
canais = conteudo.find('channel')
noticias = list(canais)
len(noticias)
noticias = noticias[40:]
noticias
#print(noticias)
def chr_remove(y, to_remove):
    new_string = y
    for x in to_remove:
        new_string = new_string.replace(x, '')
    return new_string
for noticia in noticias:
    y = noticia.findtext('title')
    titulo = "Titulo: " + chr_remove(y, ":;")
    link = "Link: " + noticia.findtext('link')
    c = csv.writer(open("MEUARQUIVO.csv", "a") )
    c.writerow([titulo ,";"+ link] )
