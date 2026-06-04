def domain():
    print("fullstack python course")

domain()

base = domain()

def outer_fun():
    print("This is outer function")

    def inner_fun1():
        print("This is inner1 function")

    def inner_fun2():
        print("This is inner2 function")
    
    inner_fun1()
    inner_fun2()

outer_fun()

def greet():
    print("Hello, Python learner!")

greet()

msg = greet()


def calculator():
    print("This is the calculator function")
    print("num1=5, num2=3")


    def add(a, b):
        print("Addition:=", a + b)

    def subtract(a, b):
        print("Subtraction:=", a - b)

    def multiply(a, b):
        print("Multiplication: =", a * b)

    def divide(a, b):
        print("Division: =", a / b)

    add(5, 3)
    multiply(5, 3)
    subtract(5, 3)
    divide(5, 3)

calculator()




