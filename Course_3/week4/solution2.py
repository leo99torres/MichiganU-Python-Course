import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

count = int(input('Enter count:'))
position = int(input('Enter position:'))

#site = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
site = "http://py4e-data.dr-chuck.net/known_by_Tamara.html"
print("Retrieving:", site)

html = urllib.request.urlopen(site).read()


while count > 0:
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')    
    x = tags[position-1].get('href', None)
    print("Retrieving:", x)
    count = count - 1
    #print("Count ", count)
    html = urllib.request.urlopen(x).read()








