# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

count = 0
soma = 0

for line in fh:
    if line.startswith("X-DSPAM-Confidence: "):
        count = count + 1.0
        x = line.find("0")
        soma = soma + float(line[x:])


media = soma / count

print("Average spam confidence:", media)