'''
Chapter 2.13

Created on Jun 4, 2020

@author: jasonmoreau
'''

value = input("Enter a four digit integer: ")
thousands = value / 1000  
hundreds = value / 100 % 10
tens = value / 10 % 100 % 10
ones = value % 10
print(thousands)
print(hundreds)
print(tens) 
print(ones)

