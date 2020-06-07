''' Chapter 5.11 '''

numberOfStudents = int(input("Enter number of students: "))

highScore = 0
secondHighestScore = 0

for i in range(0, numberOfStudents):
    currentScore = int(input("Enter score: "));
    if(highScore == 0):
        highScore = currentScore; 
    if(currentScore > highScore):
        secondHighestScore = highScore;
        highScore = currentScore;   

print("The highest score is", highScore);
print("The second highest score is", secondHighestScore);
        