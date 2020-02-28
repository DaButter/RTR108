def computepay(h,r):
    if h>40:
        samaksa = 40*r+(h-40)*1.5*r
    else:
        samaksa = h*r
    return samaksa

hrs = input("Enter Hours:")
h = float(hrs)

pph = input("Hourly rate:")
r = float(pph)


p = computepay(h,r)
print("Pay",p)

# defineta funkcija kapnajumam
def kapinajums(x,y,z):
    if z=1:
        apr = x**2+2*x*y+y**2
    elif z=2:
        apr = (x+y)**3
    elif z=3:
        apr = x**3+3*x**2*y+3*x*y**2+y**3
    elif z=4:
        apr = x**4+4*x**3*y+6*x**2*y**2+4*x*y**3+y**4

    return apr

aprs = input(" 1 for (x+y)^2; 2 for (random); 3 for (x+y)^3; 4 for (x+y)^4")
z = float(aprs)

xs = input("x:")
x = float(xs)

ys = input("y:")
y = float(ys)

print("PASCAL DONE:",apr)


        # 1 PASCAL
        # 1 1
        # 1 2 1 [2]
        # 1 3 3 1 [3]
        # 1 4 6 4 1 [4] 
        # 1 5 9 9 5 1 [5] 
        # 1 6 14 18 14 6 1
    
