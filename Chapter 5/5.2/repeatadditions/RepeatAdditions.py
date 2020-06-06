''' Chapter 5.2 '''

import time
import random

numberOfQuestions = 10;
totalCorrect = 0;

# Start time
startTime = time.time()

for i in range(0, numberOfQuestions):
    x, y = random.randint(1,15), random.randint(1, 15)
    questionSum = x + y;

    myAnswer = input("What is " + str(x) + " + " + str(y) + " = ")
    if(myAnswer == questionSum):
        totalCorrect += 1
        print "Correct!\n"
    else: 
        print "Incorrect."
        print "The correct answer is", questionSum, "\n"

# End time
endTime = time.time();
# Calculate time
totalTime = endTime - startTime
        
print "Total correct:", totalCorrect, "out of", numberOfQuestions
print "Test time:", format(totalTime, ".2f"), "seconds"