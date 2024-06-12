import re

#fname = open("regex_sum_42.txt")
#fname = open("x.txt")
fname = open("regex_sum_2025461.txt")

value = 0
lst = list()

value = 0
lst = list()

for line in fname:
    line = line.strip()
    x = re.findall('([0-9]+)', line)

    if not x : continue #testando se a lista esta vazia ou nao
    elif len(x) >=1:
        for i in range(len(x)) :
            lst.append(int(x[i]))
    
    
for i in range(len(lst)):
    value = value + lst[i]
    
print(value)
