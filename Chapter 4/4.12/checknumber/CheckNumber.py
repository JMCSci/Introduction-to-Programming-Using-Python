''' Chapter 4.12 '''

number = input("Enter a number: ")

print "Is", str(number), "divisible by 5 and 6?", number % 5 == 0 and number % 6 == 0
print "Is", str(number), "divisible by 5 or 6?", number % 5 == 0 or number % 6 == 0
print "Is", str(number), "divisible by 5 or 6, but not both?", not (number % 5 == 0 and number % 6 == 0)