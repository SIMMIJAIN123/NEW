def func1(*args):
    for arg in args:
        print(arg)
func1(1,2,3)


def func2(*args):
    return args

l1=[1,2,3,4,5]
print(func2(l1))




# Kwargs
def func4(**kwargs):
    for key,val in kwargs.items():
        print(key,val)
func4(a="simmi",b="hii")

