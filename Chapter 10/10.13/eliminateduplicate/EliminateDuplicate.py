''' Chapter 10.13 '''

def main():
    numbers = input("Enter ten numbers: ")
    elements = numbers.split()
    lst = [eval(x) for x in elements]
    eliminateDuplicates(lst)

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
    
    print("The distinct numbers are: ", end = "")
    for i in lst2:
        print("", end = str(i) + " ")

if __name__ == "__main__":
    main()