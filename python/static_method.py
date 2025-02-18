class Car:
    def __init__(self,brand,model):  # constructor , first call when object created
        self.brand= brand
        self.model= model
    
    def carname(self):
        return f"{self.brand}{self.model}"
    
    @staticmethod
    def method():
        return "THis is static method"

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

print(Car.method())