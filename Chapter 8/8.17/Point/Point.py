''' Chapter 8.17 '''

import math

class Point:
    def __init__(self, x = 0.0, y = 0.0):
        self.__x = x
        self.__y = y
    
    # distance: Returns distance between two points
    def distance(self, Point):
        distance = math.sqrt(math.pow(Point.__x - self.__x, 2) + math.pow(Point.__y - self.__y, 2))
        return distance
    # nearBy: Returns boolean that checks if two points are near each other
    def nearBy(self, Point):
        distance = self.distance(Point)
        # Points are near each other if the distance is less than 5
        if(distance < 5):
            return True
        return False
    
    # This acts like overridden toString method in Java    
    def __str__(self):
        return "(" + str(self.__x) + ", " + str(self.__y) + ")"