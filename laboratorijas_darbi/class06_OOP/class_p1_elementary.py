class Panini:
    x = 0
    
    def pn(self):
        self.x = self.x + 1
        print("So far", self.x)
        
an = Panini()
an.pn()
Panini.pn(an)

print ("Type", type(an))
print ("Dir ", dir(an))


# with dir() and type()
x = list()
print ("Type", type(x))
print ("Dir ", dir(x))

# dir() with a String
y = 'Hello there'
print ("Dir ", dir(y))
