"""
Write a program to read through the mbox-short.txt and figure out the distribution 
by hour of the day for each of the messages. You can pull the hour out from the 
'From ' line by finding the time and then splitting the string a second time using a colon.
"""

name = input("Enter a file:")
if len(name) < 1:
    handle = open("mbox-short.txt")
else:
    handle = open(name)
#handle = open("mbox-short.txt")

dicionario = dict()
lst = list()

for line in handle:
    if line.startswith("From "):
        aux = line.split()
        time = aux[5].split(":")
        dicionario[time[0]] = dicionario.get(time[0], 0) + 1

lst = sorted(dicionario.items())
for k,v in lst:
    print(k, v,)


        