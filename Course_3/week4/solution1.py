import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#html = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_42.html").read()
html = urllib.request.urlopen(" http://py4e-data.dr-chuck.net/comments_2025463.html").read()

soup = BeautifulSoup(html, 'html.parser')

#print(soup)
count = 0
sum = 0
tags = soup('span')
for tag in tags:
   sum = sum + int(tag.contents[0])
   count = count + 1


print("Count ", count)
print("Sum ", sum)
   