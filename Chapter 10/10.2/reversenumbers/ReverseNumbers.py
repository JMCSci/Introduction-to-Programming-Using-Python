''' Chapter 10.2 '''

def main():
    numbers = input("Enter numbers: ")
    elements = numbers.split()
    listOfNumbers = [eval(x) for x in elements]
    displayReverse(listOfNumbers)


def displayReverse(listOfNumbers):
    for i in range(len(listOfNumbers) - 1, -1 , -1):
        print(listOfNumbers[i])
            

if __name__ == "__main__":
    main()