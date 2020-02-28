import math
# kas ir cmath? vai var importet atseviskus modulus?
# vai pirms katras sin darbibas jaraksta math.darbiba?

# vizualizacija SUM bloks

print('\n\n\t   500 \n') # ar \t taulaciju nocentre
print('\t -------- \n')
print('\t \\                (k+1)   k   (2k-1)\n') #pakapes
print("\t  \\          (-1)^     *x^ *2^\n") #dalas augsa
print(" f(x) =\t   |      ----------------------------   = (sin(sqrt(x)))^2\n") #dalas vidus
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

print('Izmantojot series summu: ')
print('\n\n')

# iemacities py4e ciklus

# REKURENCES reizinataja vizualizacijas bloks

print("\nRekurences reizinatajs:\n\n");

print("           (-4)*x\n");
print(" R = -------------------- \n");
print("        (2*k)*(2*k-1)\n");
print("\n");
