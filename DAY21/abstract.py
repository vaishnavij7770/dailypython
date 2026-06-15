#abstraction in python

# from abc import ABC, abstractmethod

# class polygon(ABC):
#     @abstractmethod
#     def sides(self):
#         pass

# class triangle(polygon):
#     def sides(self):
#         print("Triangle have 3 sides")

# class square(polygon):
#     def sides(self):
#         print("square have 4 sides")

# t = triangle()
# t.sides()

# s = square()
# s.sides()
        
#ABC means abstract base class
#ABC cannot make object
from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def milege(self):
        pass

    def add(self):
        print("this is add")

class car(vehicle):
    def milege(self):
        # super().milege()
        # super().add()
        print("16")

class scooter(vehicle):
    def milege(self):
        print("30")

c = car()
c.milege()

s = scooter()
s.milege()