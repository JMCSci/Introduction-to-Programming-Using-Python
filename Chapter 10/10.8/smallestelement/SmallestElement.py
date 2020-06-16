''' Chapter 10.8 '''

def main():
    number = input("Enter numbers: ")
    elements = number.split()
    lst = [eval(x) for x in elements]
    index = indexOfSmallestElement(lst)
    print("The smallest element is located at index",index)

def indexOfSmallestElement(lst):
    size = len(lst)
    index = 0
    min = lst[0]
    
    for i in range(0, size):
        if(lst[i] < min):
            min = lst[i]
            index = i

    return index

if __name__ == "__main__":
    main()