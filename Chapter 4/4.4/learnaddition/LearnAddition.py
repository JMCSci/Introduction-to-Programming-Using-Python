''' Chapter 4.4 '''

import random 

x = random.randint(0, 99)
y = random.randint(0, 99)

randomSum = x + y 

mySum = input(str(x) + " + " + str(y) + " = ")

if(mySum == randomSum):
    print "Correct!"
else: 
    print "Incorrect."
    print "The answer is", randomSum