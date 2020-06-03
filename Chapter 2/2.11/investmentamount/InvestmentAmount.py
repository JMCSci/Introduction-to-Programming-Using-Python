'''
Chapter 2.11

Created on Jun 3, 2020

@author: jasonmoreau
'''

finalAccountValue = input("Enter the final account value: ")
annualInterestRate = input("Enter annual interest rate in percent: ")
years = input("Enter number of years: ")
numberOfMonths = years * 12
monthlyInterestRate = (annualInterestRate / 100) / 12
initialDepositValue = finalAccountValue / (1 + monthlyInterestRate) ** numberOfMonths
print "Initial deposit value is", initialDepositValue