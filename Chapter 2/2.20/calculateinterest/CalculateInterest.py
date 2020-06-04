'''
Chapter 2.20

Created on Jun 4, 2020

@author: jasonmoreau
'''

balance, annualInterestRate = input("Enter balance and interest rate (e.g., 3 for 30%): ")
interest = balance * annualInterestRate / 1200
print "The interest is", format(interest, ".5f")