'''
Created on Jun 4, 2020

Chapter 2.19 

@author: jasonmoreau
'''

investmentAmount = input("Enter investment amount: ")
annualInterestRate = input("Enter annual interest rate: ")
numberOfYears = input("Enter number of years: ")

numberOfMonths = numberOfYears * 12
# Convert percentage to a decimal
annualInterestRate = annualInterestRate / 100
monthlyInterestRate = annualInterestRate / 12
futureInvestmentValue = (investmentAmount * (1 + monthlyInterestRate) ** numberOfMonths)

print "Accumulated value is:", format(futureInvestmentValue, '.2f')