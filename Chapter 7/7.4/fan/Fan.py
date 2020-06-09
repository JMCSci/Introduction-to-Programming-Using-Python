''' Chapter 7.4 '''

class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    
    def __init__(self, speed = SLOW, on = False, radius = 5.0, color = "Blue"):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color
             
    def getSpeed(self):
        return self.__speed
    
    def getOn(self):
        return self.__on
    
    def getRadius(self):
        return self.__radius
    
    def getColor(self):
        return self.__color
    
    def setSpeed(self, speed):
        self.__speed = speed
        
    def setOn(self, on):
        self.__on = on
    
    def setRadius(self, radius):
        self.__radius = radius
        