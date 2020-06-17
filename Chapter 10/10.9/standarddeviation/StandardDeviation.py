''' Chapter 10.9 '''

import math

# 1.9 2.5 3.7 2 1 6 3 4 5 2

def main():
    numbers = input("Enter numbers: ")
    elements = numbers.split()
    lst = [eval(x) for x in elements]
    mean = findMean(lst)
    print("The mean is",format(mean, ".2f"))
    sdeviation = deviation(lst, mean)
    print("The standard deviation is",format(sdeviation, ".5f"))

def findMean(lst):
    size = len(lst)
    sum = 0
    
    for i in lst:
        sum += i
    average = sum / size
    return average


def deviation(lst, mean):
    n = len(lst)
    sum = 0
    
    for i in lst:
        sum += math.pow(i - mean, 2)
    deviation = math.sqrt(sum / (n - 1))
    return deviation
        
    


if __name__ == "__main__":
    main()