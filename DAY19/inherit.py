#single inheritance

class Parent:
    print("Parent class")
    
    def display(self):
        print("im display method of parent class")
# p = Parent()
class Child(Parent):
    print("Child class")

c = Child()
c.display()

#multilevel inheritance

class GrandParent:
    print("GrandParent class")
    
class Parent2(GrandParent):
    print("Parent class")

class Child2(Parent2):
    print("Child class")


c = Child2()

#multiple inheritance
class Father:
    print("Father class")

class Mother:
    print("Mother class")

class Child3(Father, Mother):
    print("Child class")

c = Child3()

#hierarchical inheritance
class Parent3:
    print("Parent class")
class Child4(Parent3):
    print("Child1 class")
class Child5(Parent3):
    print("Child2 class")

c4 = Child4()
c5 = Child5()

#hybrid inheritance
class A:
    print("Class A")
class B:
    print("Class B")
class C(A, B):
    print("Class C")
class D(C):
    print("Class D")
d = D()
