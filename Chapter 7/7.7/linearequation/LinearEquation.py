''' Chapter 7.7 '''

class LinearEquation:
    def __init__ (self, a = 0.0, b = 0.0, c = 0.0, d = 0.0, e = 0.0, f = 0.0):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
        
        
    def getA(self):
        return self.__a
    
    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c
    
    def getD(self):
        return self.__d
    
    def getE(self):
        return self.__e
    
    def getF(self):
        return self.__f
    
    # isSolvable: Checks denominator to see if equation can be solved -- returns a boolean
    def isSolvable(self):
        denominator = (self.__a * self.__d) - (self.__b * self.__c)
        if(denominator != 0):
            return True
        return False
    
    # getX: Solves and returns x
    def getX(self):
        x = (self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)
        return x
        
    # getY: Solves and returns y
    def getY(self):
        y = (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)
        return y
    # solve: Solves 2 x 2 system of linear equation
    def solve(self):
        value = self.isSolvable() 
        if(value == True):
            x = self.getX()
            y = self.getY()
            print("x is", x, "and y is", y)
        else:
            print("The equation has no solution") 