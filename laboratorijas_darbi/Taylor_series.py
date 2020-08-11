import math

# vizualizacija SUM bloks

print('\n\n\t   500 \n') # ar \t taulaciju nocentre
print('\t -------- \n')
print('\t \\                (k+1)   k   (2k-1)') #pakapes
print("\t  \\          (-1)^     *x^ *2^") #dalas augsa
print(" f(x) =\t   |      ----------------------------   = (sin(sqrt(x)))^2") #dalas vidus
print("  \t  /\t           (2*k)!"); #dalas apaksa
print("\n\t /\n")
print("\t -------- \n")
print("\t   k=1\n\n")

# ievades BLOCK

xx = input('Ievadiet x vertibu, kurai velaties aprekinat (sin(sqrt(x))^2:')
x = float(xx)

# MATH izvades BLOCK

print('Izmantojot math: ',math.sin(math.sqrt(x))*math.sin(math.sqrt(x)))
#pakapes izmantosana
print('izmantojot math ar **2: ',math.sin(math.sqrt(x))**2)
print('\n') # pievienot ari sin(sqrt(X))^2 kur vizualize x

# SUM darbibas block

print('Izmantojot series summu: \n')

a=x
Sum=a
k=1

while k<501:
    k+=1
    a=a*(-4)*x/((2*k)*(2*k-1)) # a*R
    Sum = Sum + a; # SUM

    if k==499:
        print('Rinda nr.%d. | X=%.5Lg | a=%.5Le | SUM=%.5Lf | \n'%(k,x,a,Sum))
    if k==500:
        print('Rinda nr.%d. | X=%.5Lg | a=%.5Le | SUM=%.5Lg | \n'%(k,x,a,Sum))

    

# REKURENCES reizinataja vizualizacijas bloks

print("\nRekurences reizinatajs:\n\n");

print("           (-4)*x");
print(" R = -------------------- ");
print("        (2*k)*(2*k-1)");
print("\n");
