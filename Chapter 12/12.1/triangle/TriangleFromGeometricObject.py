''' Chapter 12.1 '''

from GeometricObject import GeometricObject
import math

class Triangle(GeometricObject):
    def __init__(self, side1 = 1.0, side2 = 1.0, side3 = 1.0):
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
    
    def getSide1(self):
        return self.side1
    
    def getSide2(self):
        return self.side2
    
    def getSide3(self):
        return self.side3
    
    def getArea(self):
        p = self.getPerimeter()
        area = math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))
        return area
    
    def getPerimeter(self):
        perimeter = (self.side1 + self.side2 + self.side) / 2
        return perimeter 
    
    def __str__(self):
        return "Triangle: side1 = " + str(self.__side1) + " side2 = " + \
            str(self.__side2) + " side3 = " + str(self.__side3) + " color = " + \
            str(self.getColor()) + " filled = " + str(self.isFilled())