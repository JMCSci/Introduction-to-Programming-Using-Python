''' Chapter 5.8 '''

import math
from math import sqrt

number = 0; 

print(format("Number", ">2s"), format("Square Root", ">17s"));

while(number <= 20):
    print(format(number, "<2.0f"), format(sqrt(number), "16.4f"));
    number += 2;