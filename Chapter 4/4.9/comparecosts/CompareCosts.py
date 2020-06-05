''' Chapter 4.9 '''

p1_Weight, p1_Price = input("Enter weight and price for package 1: ")
p2_Weight, p2_Price = input("Enter weight and price for package 2: ")

p1_Cost = p1_Weight / p1_Price
p2_Cost = p2_Weight / p2_Price

if(p1_Cost < p2_Cost):
    print "Package 1 has the better price."
elif(p1_Cost == p2_Cost):
    print "The price is equal."
else:
    print "Package 2 has the better price."