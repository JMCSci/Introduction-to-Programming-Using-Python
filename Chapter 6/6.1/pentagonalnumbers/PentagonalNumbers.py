def main():
    global count;       # declare global variable
    count = 0;          # initialize global variable
    n = int(input("Enter a value for n: "));
    value = getPentagonalNumber(n);
    print("Pentagonal number of", n, "is", format(value, ".0f"));
    
    
    # First 100 eontagonal numbers
    print("\nFirst 100 pentagonal numbers")
    print("------------------------------------------------------------")

    for i in range(0, 100):
        value = getPentagonalNumber(i);
        printNumbers(value);
        count += 1;
    
def getPentagonalNumber(n):
    result = 0;
    for i in range(1, n + 1):
        result = i * (3 * i - 1) / 2;    
    return result;   

def printNumbers(value):
    if(count % 11):
        print(format(value, ".0f"), end = " ");
    else: 
        print();    

if __name__ == '__main__':
    main();