''' Chapter 8.8 '''

def main():
    binaryString = input("Enter a binary string: ")
    binaryToDecimal(binaryString)

def binaryToDecimal(binaryString):
    size = len(binaryString)
    i = size - 1
    position = 0
    decimalValue = 0;
    
    while(i >= 0):
        decimalValue += int(binaryString[i]) * 2 ** position
        i -= 1
        position += 1
    print("Decimal value is",decimalValue)

if __name__ == "__main__":
    main()