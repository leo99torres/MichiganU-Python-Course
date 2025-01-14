def computepay(h, r):

    if h > 40:
        total = (h-40)*(r*1.5) + 40*r
    else:
        total = h*r
    return total 


hrs = input("Enter Hours:")
rph = input("Enter the rate per hour:")

try:
    h = float(hrs)
    r = float(rph)
except:
    print("Enter valid numbers")
    quit()



p = computepay(h, r)
print("Pay", p)