''' Chapter 6.3 '''

def main():
    global number;
    global reversed;
    number = int(input("Enter an integer: "));
    reversed = reverse(number);
    palindrome = isPalindrome(number);
    print(palindrome);

# reverse: Reverses an integer -- returns integer
def reverse(number):
    size = len(str(number))
    i = 0;
    reverseNumber = "";
    while(i < size):
        temp = number % 10;
        reverseNumber += str(temp);
        number = number // 10; 
        i += 1;
    numberAsInteger =  int(reverseNumber);
    return numberAsInteger;

# isPalindrome: Checks to see if integer is a palindrome -- returns boolean
def isPalindrome(number):
    if(number == reversed):
        return True;
    return False;

if __name__ == '__main__':
    main();