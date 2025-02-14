def decorateor(func):
    def wrapper():
        print("HII")
        func()
        print("Bye")

    return wrapper
def hello():
    print("I am hello function")

h1=decorateor(hello)
h1()


def decorateors(func):
    def func1():
        print("THis is first function")
        func()
        print("This is last function")

    return func1
def hello():
    print("THis is hello function")

h1=decorateors(hello)
h1()