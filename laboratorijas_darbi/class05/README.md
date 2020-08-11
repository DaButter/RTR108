<!-- https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax -->
# Laboratorijas darba Nr.1 atskaite - series

## Teorija

Funkcijas vērtību var aprēķināt divejādi - vienkārši aprēķinot, izmantojot matemātikas bibliotēkas. Vai arī izmantojot vienkāršas darbības (reizināšanu, dalīšanu, atņemšanu, saskaitīšanu) atbilstošajā Teilora rindā. Rindas summa ir atbilstošās funkcijas vērtība.

### Kods
```
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

### Rezultāts
```

	   500 

	 -------- 

	 \                (k+1)   k   (2k-1)
	  \          (-1)^     *x^ *2^
 f(x) =	   |      ----------------------------   = (sin(sqrt(x)))^2
  	  /	           (2*k)!

	 /

	 -------- 

	   k=1


Ievadiet x vertibu, kurai velaties aprekinat (sin(sqrt(x))^2:3
Izmantojot math:  0.9742215979209138
izmantojot math ar **2:  0.9742215979209138


Izmantojot series summu: 

Rinda nr.499. | X=3 | a=0.00000e+00 | SUM=0.97422 | 

Rinda nr.500. | X=3 | a=-0.00000e+00 | SUM=0.97422 | 


Rekurences reizinatajs:


           (-4)*x
 R = -------------------- 
        (2*k)*(2*k-1)



```

### Analīze

Programma korekti aprekina (sin(sqrt(x)))^2 vertibu gan pec math. iebuvetas funkcijas, gan sastadot ciklus un rekinot ar rindu metodi.
Programma tika salidzinata ar ieprieks C valoda rakstito.
Atskiribas no C valodas:
1. printf vieta raksta print
2. cikla ietilpstoso nedefine ar {}, bet pirms cikla izmanto : un lieto TAB


### Dotās funkcijas sin(sqrt(x))^2 grafiks

![Funkcijas grafiks](https://github.com/DaButter/RTR105/blob/master/darbi/1ld_series/graph_image.png)
