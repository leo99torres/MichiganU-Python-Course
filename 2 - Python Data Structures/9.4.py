name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open("mbox-short.txt")

dicionario = dict()

for line in handle:
    if line.startswith("From "):
        chave = line.split()
        dicionario[chave[1]] = dicionario.get(chave[1], 0) + 1
        
email = None
valorMax = None

for key, value in dicionario.items():
    if email is None or value > valorMax:
        valorMax = value
        email = key

print(email, valorMax)