'''
Chapter 3.4 

Created on Jun 4, 2020

@author: jasonmoreau
'''

from math import tan

PI =  3.14159

side = input("Enter the side: ")
area = (5 * side ** 2) / (4 * tan(PI/5))
print "The area of the pentagon is", area