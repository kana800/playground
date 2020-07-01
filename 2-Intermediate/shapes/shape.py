'''
Shape Area and Perimeter Classes - Create an abstract class called Shape and then inherit from it other shapes like diamond, rectangle, circle, triangle etc. 
Then have each class override the area and perimeter functionality to handle each shape type.
'''

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass



class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return float(pi*(self.radius)**2)

    def perimeter(self):
        return float(2*pi*self.radius)


class Square(Shape):

    def __init__(self,length):
        self.length = length

    def area(self):
        return float(self.length * self.length)

    def perimeter(self):
        return float(4 * self.length)


class Rectangle(Shape):
    
    def __init__(self,length,width):
        self.length = length
        self.width  = width

    

    def area(self):
        return float(2 * self.length * self.width)

    def perimeter(self):
        return float(2*(self.length+self.width))


class Triangle(Shape):

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        pass

    def perimeter(self):
        pass



















