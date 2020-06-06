''' Chapter 5.1 '''

value = 1;
count = 0;
positive = 0;
negative = 0;
valueSum = 0.0;

while(value != 0):
    value = input("Enter an integer, the input ends if it is 0: ");
    valueSum += value;
    if(value > 0):
        positive += 1;
    elif(value < 0):
        negative += 1;
    if(value != 0):
        count += 1;

average = valueSum / count;
print "\nThe number of positives is", positive;
print "The number if negatives is", negative;
print "The total is", valueSum;
print "The average is", average