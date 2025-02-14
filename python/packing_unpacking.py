def func1(*arg):  # packing
    for i in arg:
        print(i)

l1=[1,2,3,4]
func1(*l1)  # unpacking



def func2(a,b,c):
    return a,b,c

l2=[1,2,3]
print(func2(*l2))   # unpacking

