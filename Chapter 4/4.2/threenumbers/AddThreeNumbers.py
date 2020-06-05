''' Chapter 4.2 '''

import random

x = random.randint(0,9)
y = random.randint(0,9)
z = random.randint(0,9)

randomSum = x + y + z 

mySum = input(str(x) + " + " + str(y) + " + " + str(z) + " = ")

if(mySum == randomSum):
    print "Correct!"
else:
    print "Incorrect."
    print "The answer is", randomSum