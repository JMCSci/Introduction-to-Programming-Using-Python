''' Chapter 5.7 '''

from math import sin, cos, radians

print("Degree", format("Sin", ">8s"), format("Cos", ">9s"));

degree = 0;

while(degree <= 360):
    print(format(degree, "<5.0f"), format(sin(radians(degree)), ">12.4f"), format(cos(radians(degree)), ">9.4f"));
    degree += 10;