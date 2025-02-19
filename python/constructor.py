# default constructor

class Student:
    def __init__(self):  # initialize the created instance  and new is used to define new instance
        self.s1="hii"
        self.s2="hello"
    
s1=Student()
print(s1.s1)

# parametrized 
class Student:
    def __init__(self,s1,s2):
        self.s1=s1
        self.s2=s2

    def display(self):
        print(self.s1)
    
s1=Student("hii","simmi")
s1.display()



# constructor with default values
class Stu:
    def __init__(self,s1="simmi",s2="jain"):
        self.s1 = s1
        self.s2 = s2
    
    def display(self):
        print(f"s1:{self.s1} s2: {self.s2}")

s1 = Stu()
s1.display()

# copy constructor
class Book:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def display(self):
        print(f"{self.m1}")

s1 = Book("book title","book author")
s2 = Book(s1.m1,s1.m2)
s2.display()

# Private constructor
# you want to restrict the creation of multiple objects of a class




class A:
    __a = None  

    def __new__(cls):
        if cls.__a is None:
            cls.__a = super().__new__(cls)  # 
            print(cls.__a)  
            return cls.__a
        
    def __init__(self):
        print("HII")  # ✅ This will execute on every object creation

# Creating objects
obj1 = A()
obj2 = A()

print(obj1 is obj2)  # ✅ True (Both refer to the same instance)
