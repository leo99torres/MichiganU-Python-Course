hrs = input("Enter Hours:")
h = float(hrs)

rph = input("Enter rate per hour:")
r = float(rph)

if h <= 40 :
    total = h*r
else : 
    total = (40*r)+(h-40)*(r * 1.5) 

print(total)