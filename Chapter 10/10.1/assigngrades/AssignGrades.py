''' Chapter 10.1 '''

def main():
    scores = input("Enter scores: ")
    elements = scores.split()
    listOfGrades = [eval(x) for x in elements]
    grades(listOfGrades)
      
def grades(listOfGrades):
    best = max(listOfGrades)
    
    for i in range(0, len(listOfGrades)):
        if(listOfGrades[i] >= best - 10):
            print("Student",i, "score is",listOfGrades[i],"and the grade is A")
        elif(listOfGrades[i] >= best - 20):
            print("Student",i, "score is",listOfGrades[i],"and the grade is B")
        elif(listOfGrades[i] >= best - 30):
            print("Student",i, "score is",listOfGrades[i],"and the grade is C")
        elif(listOfGrades[i] >= best - 40):
            print("Student",i, "score is",listOfGrades[i],"and the grade is D")
        else:
            print("Student",i, "score is",listOfGrades[i],"and the grade is F")
        
if __name__ == "__main__":
    main()