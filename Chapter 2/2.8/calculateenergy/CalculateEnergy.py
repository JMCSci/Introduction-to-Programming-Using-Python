'''
Chapter 2.8

Created on Jun 3, 2020

@author: jasonmoreau
'''

m = input("Enter the amount of water in kilograms: ")
initialTemperature = input("Enter the initial temperature: ")
finalTemperature = input("Enter the final temperature: ")
q = m * (finalTemperature - initialTemperature) * 4184
print "The energy needed is", q
