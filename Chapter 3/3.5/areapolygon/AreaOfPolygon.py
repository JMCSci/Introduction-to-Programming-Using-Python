''' Chapter 3.5 '''

from math import tan

PI = 3.14159

n = input("Enter the number of sides: ")
side = input("Enter the side: ")
area = (n * side ** 2) / (4 * tan(PI/n))
print "The area of the polygon is", area