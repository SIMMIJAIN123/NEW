class Car:
    total_car=0
    def __init__(self,brand,model):  # constructor , first call when object created
        self.__brand= brand
        self.__model= model
        Car.total_car+=1
    
    def getname(self):
        return self.__brand + "!"
    
    def carname(self):
        return f"{self.__brand} {self.__model}"
    
    def newmethod(self):
        return "This is encapsulation method"
    
  

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

    def newmethod(self):
        return "This is encapsulation method one subclass"



obj1 = Car("Toyota","corolla")
print(obj1.newmethod())


obj2 = ElectricCar("Tesla","Modal","85")
print(obj2.newmethod())

print(Car.total_car) # how much object are created 

