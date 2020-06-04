'''
Chapter 2.14

Created on Jun 4, 2020

@author: jasonmoreau

'''

import math

x1, y1, x2, y2, x3, y3 = input("Enter three points for a triangle: ")

area = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
area = math.fabs(area)
print "The area of the triangle is", area
