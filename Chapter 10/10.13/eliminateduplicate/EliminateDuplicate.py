''' Chapter 10.13 '''

def main():
    numbers = input("Enter ten numbers: ")
    elements = numbers.split()
    lst = [eval(x) for x in elements]
    eliminateDuplicates(lst)

# 1 2 3 2 1 6 3 4 5 2

def eliminateDuplicates(lst):
    size = len(lst)
    lst2 = []
    for i in lst:
        count = 0
        for j in range(0, size):
            if(i == lst[j]):
                count += 1
        if(count < 2):
            lst2.append(i)
                                  
    print(lst2)

if __name__ == "__main__":
    main()