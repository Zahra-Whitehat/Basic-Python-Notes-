class Animal:
    hight = 100
    weight = 100
    heartbit = 70
    def thisMethod(self):
        return "this is an animal"
    def createName(self, name):
        self.name = name
    def displayName(self):
        return self.name
    def saying(self):
        print("hello %s" % self.name)
        
class Solid:
    width = 5
    def density(self,Density):
        self.Density = Density
        
class Mamal(Animal):
    pass

class Reptar(Animal,Solid):
    hight = 1500


class Bird(Animal):
    def __init__(self):
        print("this is initialization class")
        

    
Animal_1 = Animal()
Animal_2 = Animal()
print(Animal_1.hight)
Animal_1.createName('Aligator')
Animal_1.saying()
print(Animal_2.hight)
Animal_2.createName('Giraff')
print(Animal_2.displayName())

Obj1 = Mamal()
Obj2 = Reptar()
Obj3 = Bird()

print(Mamal.heartbit)
print(Obj2.heartbit, Obj2.hight, Obj2.width)
