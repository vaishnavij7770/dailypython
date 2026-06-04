def display(func):
    def inner():
        print("i got wrapped")
    func()
    return inner

@display
def show1():
    print("i am show1")

def show2():
    print("i am show2")

show1()
show2()