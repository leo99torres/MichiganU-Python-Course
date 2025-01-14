
fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    line = line.upper()
    line = line.rstrip() #removes the \n added by the function print()
    print(line)


