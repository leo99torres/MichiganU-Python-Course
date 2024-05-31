#name = input("Enter file:")
#if len(name) < 1:
#    name = "mbox-short.txt"
handle = open("mbox-short.txt")

dicionario = dict()

#dicionario["chave"] = 1

#print(dicionario.items())


for line in handle:
    #line = line.rstrip() 
    #print(line)
    if line.startswith("From "):
        chave = line.split()
        #print(chave)
        #quit()
        if chave[1] in dicionario:
            dicionario[chave[1]] = dicionario[chave[1]]+1
            #print("O email", chave[1], "apareceu", dicionario[chave[1]], "vezes\n")
            #print(dicionario.items(), "\n")

        else:
            #print("Achou o email",chave[1], "pela primeira vez\n")
            dicionario[chave[1]] = 1
            #print(dicionario.items(), "\n")


#print(dicionario.items())

email = None
valorMax = None

for key, value in dicionario.items():
    if email is None or value > valorMax:
        valorMax = value
        email = key

print(email, valorMax)

