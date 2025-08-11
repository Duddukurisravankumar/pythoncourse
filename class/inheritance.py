"""class human:
    name1= "sravan"
class human1:
    name2 = "kumar"
class human2(human,human1):
    name3= "duddukuri"
obj = human2()
print(obj.name1)
print(obj.name2,obj.name3)"""

#example
class animal:
    def __init__(self,name):
        self.name= name    
    def show(self):
        print(f"hello your name is {self.name},{self.age}")
class human(animal):
    def __init__(self, name,age):
        super().__init__(name)
        self.age =age
obg = human("ravan",23)
ong = animal("adnasknakfn")
print(obg.name)
obg.show()
print(ong.name)