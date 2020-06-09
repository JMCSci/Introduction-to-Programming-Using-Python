''' Chapter 7.1 '''

class Rectangle:
    def __init__(self, width = 1, height = 2):
        self.width = width
        self.height = height
        
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
        
    def getArea(self):
        area = self.width * self.height
        return area
     
    def getPerimeter(self):
        perimeter = self.width * 2 + self.height * 2
        return perimeter   