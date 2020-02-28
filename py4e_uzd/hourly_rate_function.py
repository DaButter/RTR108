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
