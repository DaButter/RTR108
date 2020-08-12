# Part 3 - Multiple instances of the same class sitting in different variables

class Panini:
    x = 0
    name = ""
    
    def __init__(self, z):
        self.name = z
        print(self.name, "made")
    
    def party(self):
        self.x = self.x + 1
        print(self.name, "count", self.x)
        
s = Panini("variable s")
s.party()

j = Panini("variable j")
j.party()
s.party()

print("\nAre variables 's' and 'j' equal: ", s is j)
print("'s' is:", type(s), "type")
print("'j' is:", type(j), "type")
