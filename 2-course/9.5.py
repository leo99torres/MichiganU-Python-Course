#Top 10 most common words in a file

fhand = open("romeo.txt")

count = dict()

for line in fhand :
    words = line.split()
    for word in words : 
        count[word] = count.get(word, 0) + 1

#print(count.items())

lista = list()

for k,v in count.items() :
    lista.append((v,k))

#print(lista)

lista = sorted(lista, reverse = True)

print(lista[0:10])
