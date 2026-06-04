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