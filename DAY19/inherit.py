class Parent:
    print("Parent class")
    
    def display(self):
        print("im display method of parent class")
# p = Parent()
class Child(Parent):
    print("Child class")

c = Child()
c.display()

