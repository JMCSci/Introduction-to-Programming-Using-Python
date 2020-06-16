''' Chapter 10.7 '''

import random

def main():
    list1 = []
    generateList(list1)
    list1.sort()
    counts = countNumbers(list1)
    printCounts(counts)
    
def generateList(list1):
    for i in range(0, 1000):
        list1.append(random.randrange(10))
    
def countNumbers(list1):
    counts = []
    
    for i in range(0,10):
        counts.append(list1.count(i))

    return counts

def printCounts(counts):
    size = len(counts)
    
    for i in range(size):
        print(i, "occurs",counts[i],"times")
        
if __name__ == "__main__":
    main()