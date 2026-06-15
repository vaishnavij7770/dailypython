#abstraction in python

from abc import ABC, abstractmethod

class polygon(ABC):
    @abstractmethod
    def sides(self):
        pass

class triangle(polygon):
    def sides(self):
        print("Triangle have 3 sides")

class square(polygon):
    def sides(self):
        print("square have 4 sides")

t = triangle()
t.sides()

s = square()
s.sides()
        