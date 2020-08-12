# objects

class Panini:
    x = 0
    
    def __init__(self):
        print('Class made')
    
    def pn(self):
        self.x = self.x + 1
        print('So far', self.x)
        
    def __del__(self):
        print('Class ended', self.x)


an = Panini()
an.pn()
an.pn()
print('Type before', type(an))
an = 42

print('Type after', type(an))
print('an contains:', an)
