''' Chapter 7.6 '''

import math

class QuadraticEquation: 
    def __init__(self, a = 0.0, b = 0.0, c = 0.0):
        self.__a = a
        self.__b = b 
        self.__c = c
        
    def getA(self):
        return self.__a
    
    def getB(self):
        return self.__b 
    
    def getC(self):
        return self.__a
    
    def solve(self):
        if(self.getDiscriminant() > 0):
            root1 = self.getRoot1()
            root2 = self.getRoot2()
            print("Root 1 =",root1)
            print("Root 2 =",root2)
        elif(self.getDiscriminant() == 0):
            root = self.getRoot1()
            print("Root =",root)
            print("Roots are identical")
        else:
            print("The equation has no roots")
            
    def getDiscriminant(self):
        discriminant = math.pow(self.__b, 2) - 4 * (self.__a * self.__c)
        return discriminant
    
    def getRoot1(self):
        if(self.getDiscriminant() > 0):
            r1 = ((-(self.__b)) + (math.sqrt(math.pow(self.__b, 2) - 4 * 
                                          (self.__a * self.__c)))) / (2 * self.__a)
            return r1
        else:
            return 0
                                    
    def getRoot2(self):
        if(self.getDiscriminant() > 0):
            r2 = ((-(self.__b)) - (math.sqrt(math.pow(self.__b, 2) - 4 * 
                                          (self.__a * self.__c)))) / (2 * self.__a)
            return r2
        else:
            return 0 