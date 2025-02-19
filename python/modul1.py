def m1():
    return "m1 method"

class New:
    def display(self):
        # print("hii")
        return "hii"
    
    def display1(self):
        return "HII"
    
    @staticmethod
    def display2():
        return "Static method"


n1 = New()
print(n1.display())
print(n1.display2())


