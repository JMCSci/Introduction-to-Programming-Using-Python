''' Chapter 10.5 '''

def main():
    numbers = input("Enter ten numbers: ")
    elements = numbers.split()
    list1 = [eval(x) for x in elements]
    list2 = checkDistinct(list1)
    printDistinct(list2)
    
def checkDistinct(list1):
    size = len(list1)
    list2 = []
    
    for i in range(0, size):
        flag = False
        for j in range(0, len(list2)):
            if(list1[i] == list2[j]):
                flag = True
                break
            else: 
                flag = False
        if(flag == False):
            list2.append(list1[i])
    
    return list2
    

def printDistinct(list2):
    print("The distinct numbers are: ", end = "")
    for i in list2:
        print("", end = str(i) + " ")
   

if __name__ == "__main__":
    main()