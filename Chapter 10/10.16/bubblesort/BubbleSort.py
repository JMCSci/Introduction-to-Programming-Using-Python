''' Chapter 10.16 '''

def main():
    numbers = input("Enter 10 numbers: ")
    elements = numbers.split()
    lst = [eval(x) for x in elements]
    print("Unsorted list:",lst)
    bubbleSort(lst)
    print("Sorted list:",lst)

def bubbleSort(lst):
    temp = 0
    size = len(lst)
    
    for i in range(0, size - 1):
        for j in range(0, size - 1):
            if(lst[j] > lst[j + 1]):
                temp = lst[j + 1]
                lst[j + 1] = lst[j]
                lst[j] = temp
    
if __name__ == "__main__":
    main()