#default constructor

class abc:
    def show(self):
        print("im show method")

    def __init__(self):
        print("im constructor")
a = abc()       #constructor will be called automatically when we create an object of the class
a.show()    
# a.__init__()

#parameterized constructor
class xyz:
    id=0
    name=""

    def __init__(self,id,name):
        self.id=id
        self.name=name
        print(id,name)

b = xyz(101,"abc")
print(b.id)
print(b.name)

 
