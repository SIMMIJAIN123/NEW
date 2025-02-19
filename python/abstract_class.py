from abc import ABC,abstractmethod   # abc->abstract base class      Used to create a abstract class  , Ensures all child classes implement required methods.
class Animal(ABC):    # Base class

    @abstractmethod     # Decorateors  , there is no  need to defined implementation of method , forcing to create a subclass for implmentation of abstract method
    def m1(self):
        pass

class Child(Animal):
    def m2(self):    # concrete method
        return "Animal"
    
d1=Child()    # instance of the Child class
print(d1.m2())



# in abstract base class can be define abstract method and implementation defined in subclass.