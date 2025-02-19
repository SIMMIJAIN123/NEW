from abc import ABC,abstractmethod   # abc->abstract base class
class Animal():    # Base class

    @abstractmethod     # Decorateors  , there is no  need to defined implementation of method 
    def m1(self):
        pass

class Child(Animal):
    def m2(self):
        return "Animal"
    
d1=Child()    # instance of the Child class
print(d1.m2())



# in abstract base class can be define abstract method and implementation defined in subclass.