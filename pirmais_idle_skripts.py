x = 10

if x > 0 :
    print('x is positive')

if x < 200:
    print(x)
print(x*x)

for i in range(5):
    print(i)

vaards='Maris'
uzvaards='Terauds'

#printf("Vards %s", vaards)  ta butu C valoda

print("Vards %s"%(vaards))
print("Vards, Uzvards: %s %s %d"%(vaards,uzvaards,x))

print("%d * %d = %d"%(x,x,x*x))

b = x*x
print("%d * %d = %d"%(x,x,b))

c = x**5 #pow(x,5) rezultats double
print("%d ^ %d = %d"%(x,5,c))
