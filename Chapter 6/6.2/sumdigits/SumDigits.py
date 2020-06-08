''' Chapter 6.2 '''

def main():
    n = int(input("Enter an integer value: "));
    value = sumDigits(n);
    print(value);

# sumDigits: Sums digits in an integer
def sumDigits(n):
    size = len(str(n))
    i = 0;
    result = 0;
    while(i < size):
        result += n % 10
        n = n // 10;
        i += 1;
    return result;
    

if __name__ == '__main__':
    main();