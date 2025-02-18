class car:
    def __init__(self,brand,model):  # constructor , first call when object created
        self.brand= brand
        self.model= model
    
    def carname(self):
        return f"{self.brand} {self.model}"


mycar = car("Toyota","corolla")
print(mycar.brand)
print(mycar.carname())

my_new_car = car("TATA","SAfari")
print(my_new_car.model)