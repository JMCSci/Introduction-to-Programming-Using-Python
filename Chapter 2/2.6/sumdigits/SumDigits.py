'''
Chapter 2.6

Created on Jun 3, 2020

@author: jasonmoreau
'''

num = input("Enter a number between 0 and 1000: ")

thousands = num // 1000
hundreds = num // 100 % 10
tens = num // 10 % 10
ones = num % 10
sumValues = thousands + hundreds + tens + ones

print sumValues 