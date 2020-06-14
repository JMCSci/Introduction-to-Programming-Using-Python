''' Chapter 8.18 '''

import math

class Circle2D:
    def __init__(self, x = 0.0, y = 0.0, radius = 0.0):
        self.__x = x
        self.__y = y
        self.__radius = radius
        
    
    def getPerimeter(self):
        perimeter = 2 * math.pi * self.__radius
        return perimeter
    
    
    def getArea(self):
        area = math.pi * math.pow(self.__radius, 2)
        return area
    
    def containsPoint(self, x, y):
        # distance between the two points is less than the radius
        distance = math.sqrt(math.pow(x - self.__x,2) + math.pow(y - self.__y, 2))
        if(distance < self.__radius):
            return True
        return False
    
    def contains(self, Circle2D):
        # if distance of points is less than than self.radius
        distance = math.sqrt(math.pow(Circle2D.getX() - self.__x,2) + math.pow(Circle2D.getY() - self.__y, 2))
        # if radius is less self.radius
        if(Circle2D.getPerimeter() < self.getPerimeter()):
            if(distance < self.__radius):
                return True
            else:
                return False
        return False
    
    def overlaps(self, Circle2D):
        if(self.containsPoint(Circle2D.getX(), Circle2D.getY()) == True):
            return True
        return False
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getRadius(self):
        return self.__radius
    
    
    def setX(self, value):
        self.__x = value
    
    def setY(self, value):
        self.__y = value
        
    def setRadius(self, value):
        self.__radius = value
    