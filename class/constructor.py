class factory:
    def __init__(self,material,cost,zip):
        self.material  = material
        self.cost =cost
        self.zip = zip
        
    def show(self):
        print(f"your factory has {self.material} bag and \n  cost is {self.cost}\n it has {self.zip} zip")
    @classmethod
    def hello(cls):
        print("welocome to the world robo 2.0")
    @staticmethod
    def static():
        print("chitti the rorbot memeory 1 terabyte memeory 1tb")
obj = factory("pure leather",2000,2)
obj2 = factory("nylonsilk",3000,3)
obj.show()
obj2.show()
obj.static()
obj2.hello()
