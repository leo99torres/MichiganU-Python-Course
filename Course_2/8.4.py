fname = input("Enter file name: ")

fh = open(fname)

lst = list()

for line in fh:
    aux = line.split()

    for i in aux :
        #print("A lista na iteraçao: ", i, lst,)
        if i not in lst :
            lst.append(i)

lst.sort()
print(lst)