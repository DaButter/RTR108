# Part 3-Inheritance

class Panini:
    x = 0
    name = ""
    
    def __init__(self, nam):
        self.name = nam
        print(self.name, "made")
    
    def pn(self):
        self.x = self.x + 1
        print(self.name, "count", self.x)
        
class paninini(Panini):
    points = 0
    def pan(self):
        self.points = self.points + 7
        self.pn()
        print(self.name, "selfpoints", self.points)


s = Panini("Variable s")
s.pn()

j = paninini("Variable j")
j.pn()
j.pan()
