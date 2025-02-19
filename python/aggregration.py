# Aggregration also used for Has-A relationship between objects.

# In this both object are independent of each other s1 and s2 meand if one object die another doesn't matter.

class Myclass:
    def __init__(self,pay):
        print("HII")
        self.pay=pay
    
    def m1(self):
        print("THis is m1 method")
        return self.pay

class Child:
    def __init__(self,s1):
        print("Child class")
        self.obj=s1
    
    def m2(self):
        print("THis is m2 method")
        return self.obj.m1()
    
# Here s1 is not the part of the relationship and is unidirectional  can be pass s1 object to s2 but not s2 object can pass in s1
s1 = Myclass(1500) 
s2= Child(s1)
print(s2.m2())
