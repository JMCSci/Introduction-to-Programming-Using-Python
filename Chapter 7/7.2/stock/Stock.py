''' Chapter 7.2 '''

class Stock:
    def __init__(self, symbol = "", name = "", previousClosingPrice = 0, currentPrice = 0):
        self.__symbol = symbol
        self.__name = name
        self.previousClosingPrice = previousClosingPrice
        self.currentPrice = currentPrice
        
    def getName(self):
        return self.__name
    
    def getSymbol(self):
        return self.__symbol
    
    def getPreviousClosingPrice(self):
        return self.previousClosingPrice
    
    def getCurrentPrice(self):
        return self.currentPrice
    
    def setPreviousClosingPrice(self, previousClosingPrice):
        self.previousClosingPrice = previousClosingPrice
        
    def setCurrentPrice(self, currentPrice):
        self.currentPrice = currentPrice
        
    def getChangePercent(self):
        changePercent = (self.currentPrice - self.previousClosingPrice) / self.currentPrice
        changePercent = changePercent
        return changePercent