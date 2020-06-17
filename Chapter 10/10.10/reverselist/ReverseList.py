''' Chapter 10.10 '''

def main():
    numbers = input("Enter numbers: ");
    elements = numbers.split()
    lst = [eval(x) for x in elements]
    reverse(lst)
    
def reverse(lst):
    size = len(lst) - 1
    reverseList = []
    
    for i in range(size, -1, -1):
        reverseList.append(lst[i])
    
    print(reverseList)

if __name__ == "__main__":
    main()