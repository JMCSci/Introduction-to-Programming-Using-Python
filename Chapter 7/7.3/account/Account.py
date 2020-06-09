''' Chapter 7.3 '''

class Account:
    def __init__(self, accountID = 0, balance = 100.0, annualInterestRate = 0.0):
        self.__accountID = accountID
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate
        
    def getId(self):
        return self.__accountID
    
    def getBalance(self):
        return self.__balance
        
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
        
    def setId(self, accountID):
        self.__accountID = accountID
        
    def setBalance(self, balance):
        self.__balance = balance
        
    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate
        
    def getMonthlyInterestRate(self):
        monthlyInterestRate = self.__annualInterestRate / 12
        return monthlyInterestRate
    
    def getMonthlyInterest(self):
        self.__balance = self.getMonthlyInterestRate() * self.__balance
        return self.__balance
    
    def withdraw(self, amount):
        self.__balance = self.__balance - amount
        
    def deposit(self, amount):
        self.__balance = self.__balance + amount
    