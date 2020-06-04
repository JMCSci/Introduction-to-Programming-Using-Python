''' Chapter 3.2 '''

from math import sin, radians, acos, cos

RADIUS = 6371.01

x1, y1 = input("Enter point 1 (latitude and longitude) in degrees: ")
x2, y2 = input("Enter point 2 (latitude and longitude) in degrees: ")
# Convert points to radians
x1 = radians(x1)
x2 = radians(x2)
y1 = radians(y1)
y2 = radians(y2)
distance = (RADIUS * acos(sin(x1) * sin(x2) + cos(x1) 
    * cos(x2) * cos(y1 - y2)))
print "The distance between the two points is", distance, "km"