# Composition -> Has a relationship

# In composition, one class contains an instance of another class as a member (or field). 
# we can call object of parent class into child class.
# use when need to avoid deep inheritance
# You can reuse functionalities without inheritance.
# Avoids deep inheritance trees and keeps class responsibilities clear.

#but in inheritance it;s have clear is-a and hirearchical relationship
# using of inheritance can be possible polymorphism
# for overriding
# tight coupling
# no flexibity with dynamically changes

class Component:
    def __init__(self):
        print("Parent class Constructor")

    def m1(self):
        return "parent class method m1"
    
class Child:
    def __init__(self):
        self.Component=None

    def m2(self):
        self.obj1=Component()
        self.obj2=Child()

        print("THis is m2 method")
        return self.obj1.m1()
        # return self.obj2
        

component = Component()
print(component.m1())

c2= Child()
print(c2.m2())



class Myclass:
    def __init__(self):
        print("THis is my parent class constructor")

    def m1(self,*args):
        for i in args:
            print(f"{i}")
        return 
    
class Child:
    def __init__(self):
        print("This is child class constructor")
        self.c1 = Myclass()

    def m2(self,a,b):
        self.c1.m1(a,b)
        return a+b
    
c2 = Child()
print(c2.m2(2,3))
