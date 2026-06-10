#default constructor

class abc:
    def show(self):
        print("im show method")

    def __init__(self):
        print("im constructor")
a = abc()       #constructor will be called automatically when we create an object of the class
a.show()    
# a.__init__()