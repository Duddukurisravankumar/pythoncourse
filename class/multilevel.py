class animal:
    def __init__(self,name,spice):
        self.name=name
        self.spice=type
class animal2(animal):
    def __init__(self, name,spice,area,age):
        super().__init__(name,spice)
        self.area =area
        self.age=age
class animal3(animal2):
    def __init__(self, name, spice, area, age,generation):
        super().__init__(name, spice, area, age)
        self.generation=generation
obj = animal3("lion","extent","forest",20,"yearler")
obj2= animal("panther","extent")