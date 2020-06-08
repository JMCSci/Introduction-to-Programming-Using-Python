''' Chapter 6.5 '''

def main():
    num1, num2, num3 = input("Enter three numbers: ").split(', ');
    displaySortedNumbers(num1, num2, num3);

# displaySortedNumbers: Sorts three numbers [works like a bubble sort]
def displaySortedNumbers(num1, num2, num3):
    if(num1 > num2):
        temp = num2;
        num2 = num1;
        num1 = temp;
    if(num1 > num3):
        temp = num3;
        num3 = num1;
        num1 = temp;
    if(num2 > num3):
        temp = num3;
        num3 = num2;
        num2 = temp;
    print(num1, num2, num3);
    

if __name__ == '__main__':
    main();