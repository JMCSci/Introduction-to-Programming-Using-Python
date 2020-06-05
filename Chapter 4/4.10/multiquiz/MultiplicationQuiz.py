''' Chapter 4.10 '''

import random 

x = random.randint(0, 99);
y = random.randint(0, 99);

randomProduct = x * y;

myProduct = input(str(x) + " * " + str(y) + " = ");

if(myProduct == randomProduct):
    print "Correct!";
else:
    print "Incorrect.";
    print "The answer is", randomProduct;