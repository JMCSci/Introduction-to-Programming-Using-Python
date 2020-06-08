''' Chapter 6.4 '''

def main():
    number = int(input("Enter an integer: "));
    value = reverse(number);
    print(value);
    
    


def reverse(number):
    reverse = "";
    size = len(str(number));
    i = 0;
    
    while(i < size):
        temp = number % 10;
        number = number // 10;
        reverse += str(temp);
        i += 1;
    reverseAsInteger = int(reverse);
    return reverseAsInteger;
    


if __name__ == '__main__':
    main();
