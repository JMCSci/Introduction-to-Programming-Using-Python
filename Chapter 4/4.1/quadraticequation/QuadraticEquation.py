''' Chapter 4.1 '''

from math import sqrt

a, b, c = input("Enter a, b, c: ")
discriminant = (b ** 2) - (4 * a  * c)

if(discriminant > 0):
    r1 = (-b + (sqrt(b ** 2 - (4 * a * c)))) / (2 * a)
    r2 = (-b - (sqrt(b ** 2 - (4 * a * c)))) / (2 * a)
    print "The roots are", r1, "and", r2
elif(discriminant == 0):
    r1 = (-b + (sqrt(b ** 2 - (4 * a * c)))) / (2 * a)
    r2 = (-b - (sqrt(b ** 2 - (4 * a * c)))) / (2 * a)
    print "The root is", r1
else:
    print "The equation has no real roots"