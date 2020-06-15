''' Chapter 10.3 '''

def main():
    numbers = input("Enter integers between 1 and 100: ")
    elements = numbers.split()
    list1 = [eval(x) for x in elements]
    list1 = sorted(list1)  # Sort list so that we can check sequentially
    countOccurances(list1)
    
def countOccurances(list1):
    size = len(list1)
    i = 0
    count = 0
    numberOccurences = []
    # is this number before, yes - continue; no -- count it
    while(i < size):
        count = 0   # reset count
        # set i equal to next index NOT equal to current i
        for j in range(i, size):    # count occurences
            if(list1[i] == list1[j]):
                count += 1
                if(i == size - 1):  # if you reach the end of the list in outer loop
                    printOccurences(list1, count, i)
                    i += 1
            elif(list1[i] != list1[j]):  # jump to next element
                printOccurences(list1, count, i)
                i = j
                break
        numberOccurences.append(count)
    return numberOccurences
 
def printOccurences(list1, count, index):
    if(count == 0 or count > 1):
        print(list1[index],"occurs",count,"times") 
    elif(count == 1):
        print(list1[index],"occurs",count,"time")
                
if __name__ == "__main__":
    main()
