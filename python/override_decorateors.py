class Car:
    def __init__(self,brand,model):  # constructor , first call when object created
        self.brand= brand
        self.__model= model
    
    def carname(self):
        return f"{self.brand}{self.__model}"
    
    @staticmethod
    def method():
        return "THis is static method"
    
    @property       # when want to that method can't be changed
    def method2(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

c1 = Car("Toyota","Modal")
c1.model = "city"   # this should be not working how to do chnages 
print(c1.model)
print(c1.method2)

