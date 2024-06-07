
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fn = open(fname)


count = 0


for line in fn:
    if line.startswith("From "):
        aux = line.split()
        print(aux[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
