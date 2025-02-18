class car:
    def __init__(self,brand,model):  # constructor , first call when object created
        self.brand= brand
        self.model= model
    
    def carname(self):
        return f"{self.brand}{self.model}"

class ElectricCar(car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size





mycar = car("Toyota","corolla")
ecar = ElectricCar("Tesla","Modal","85")
print(ecar.brand)
print(ecar.carname())

