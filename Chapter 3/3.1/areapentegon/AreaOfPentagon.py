''' Chapter 3.1 '''

import math

PI = 3.14159

length = input("Enter the length from the center to a vertex: ")
side = 2 * length * math.sin(PI/5)
area = (3 * math.sqrt(3) * side ** 2) / 2
print "The area of the pentagon is ", format(area, ".2f")