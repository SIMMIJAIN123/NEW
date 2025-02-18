class car:
    def __init__(self,brand,model):  # constructor , first call when object created
        self.__brand= brand
        self.__model= model
    
    def getname(self):
        return self.__brand + "!"
    
    def carname(self):
        return f"{self.__brand}{self.__model}"
    
  

# class ElectricCar(car):
#     def __init__(self,brand,model,battery_size):
#         super().__init__(brand,model)
#         self.battery_size=battery_size


mycar = car("Toyota","corolla")
# print(mycar.__model) # no working because varibale is private
print(mycar.getname())


# ecar = ElectricCar("Tesla","Modal","85")
# print(ecar.brand)
# print(ecar.carname())

