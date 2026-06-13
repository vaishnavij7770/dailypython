#same class same method ..............method overloading

# class python:
#     def add(self,a,b,c):
#         print(a+b+c)
#     def add(self,x,y,z=7):
#         print(x+y+z)

# p=python()
# p.add(2,3)
# p.add(1,2,6)

#diff class same method.....method overriding


class logic:
    def logic1(self,a,b):
        temp=a
        a=b
        b=temp
        print("after swap",a,b)

# l=logic()
# l.logic1(6,7)

class swap(logic):
    def logic1(self,a,b):
        super().logic1(a,b)
        print("before swap",a,b)

    def swap1(self):
        print("swapping completed")

s=swap()
s.logic1(5,6)
s.swap1()


class parent:
    def show1(self):
        print("im parent")

class child(parent):
    def show(self):
        super().show1()
        print("im child")

# p=parent()
# p.show1()        

c = child()
# c.show1()
c.show() 




