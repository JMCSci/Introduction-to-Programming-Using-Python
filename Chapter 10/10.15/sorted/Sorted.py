''' Chapter 10.15 '''

def main():
    numbers = input("Enter list: ")
    elements = numbers.split()
    lst = [eval(x) for x in elements]
    isSorted(lst)

def isSorted(lst):
    size = len(lst)
    flag = True
    
    for i in lst:
        if(flag == False):
            break
        for j in range(0, size - 1):
            if(i <= lst[j + 1]):
                flag = True
            else:
                flag = False
                
    if(flag == True):
        print("The list is sorted")
    else:
        print("The list is not sorted")
        

if __name__ == "__main__":
    main()