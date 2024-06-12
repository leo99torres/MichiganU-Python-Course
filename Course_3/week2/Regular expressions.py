#Regular expressions
import re

frase = "From leo99torres@usp.br é meu email"

buscador = re.findall('^From (\S+@\S+)', frase) #Retirando o email da frase

print(buscador)


email = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

buscador = re.findall('(\S+@\S+)', email) #Retirando o email da frase

print(buscador)

x = list()

fname = open("mbox-short.txt")

for line in fname :
    line = line.rstrip()
    value = re.findall("^X-DSPAM-Confidence: ([0-9.]+)", line)
    if len(value) != 1 : continue
    num = float(value[0])
    x.append(num)
    

print(max(x))

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)