#Esse codigo retorna todos os links de uma pagina web

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#print(soup)
# Retrieve all of the anchor tags 
tags = soup('a') #'a' é o simbolo que representa links em uma pagina HTML
print(tags)
for tag in tags:
    print(tag.get('href', None)) 