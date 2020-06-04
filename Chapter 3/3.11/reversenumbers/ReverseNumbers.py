''' Chapter 3.11 '''

number = input("Enter an integer: ")

thousands = number / 1000 
hundreds = number / 100 % 10
tens = number / 10 % 10
ones = number % 10

reverse = str(ones) + str(tens) + str(hundreds) + str(thousands)

print "The number reverse is: ", reverse