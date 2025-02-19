# when uses property we don't need to paranthesis and method behave likes attributes. and vice versa
# in this non abstract method also can implement.


from abc import ABC, abstractmethod   

class Animal(ABC):  
    @property
    @abstractmethod
    def species(self):
        pass  
class Dog(Animal):
    # @property
    def species(self):
        return "Dog"

class Cat(Animal):
    # @property
    def species(self):
        return "Cat"

# dog = Animal()  # This will raise an error: Cannot instantiate abstract class

dog = Dog()
print(dog.species)  # Output: Dog

cat = Cat()
print(cat.species)  # Output: Cat  

print(cat.species())
