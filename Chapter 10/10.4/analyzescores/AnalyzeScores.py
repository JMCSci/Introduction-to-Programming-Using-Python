''' Chapter 10.4 '''

def main():
    scores = input("Enter scores: ")
    elements = scores.split()
    list1 = [eval(x) for x in elements]
    average = averageScore(list1)
    lessThanAverage, equalToAverage, greaterThanAverage = aroundAverage(list1, average)
    print("There are", lessThanAverage,"numbers less than the average")
    print("There are", equalToAverage,"numbers equal to the average")
    print("There are", greaterThanAverage,"numbers greater than the average")
    
def averageScore(list1):
    sum = 0.0
    size = len(list1)
    
    for i in list1:
        sum += i

    average = sum / size
    return average

def aroundAverage(list1, average):
    size = len(list1)
    lessThanAverage = 0
    equalToAverage = 0
    greaterThanAverage = 0
    
    for i in range(0, size):
        if(list1[i] < average):
            lessThanAverage += 1
        elif(list1[i] == average):
            equalToAverage += 1 
        else:
            greaterThanAverage += 1
    
    return lessThanAverage, equalToAverage, greaterThanAverage


if __name__ == "__main__":
    main()