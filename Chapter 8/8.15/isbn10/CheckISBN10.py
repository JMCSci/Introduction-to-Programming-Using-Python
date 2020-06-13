''' Chapter 8.15 '''

def main():
    isbn = input("Enter the first 9 digits of an ISBN-10 as a string: ")
    checkISBN(isbn)
                 
# checkISBN: Prints ISBN-10 number using 9 digits and a 10th digit checksum 
def checkISBN(isbn):
    size = len(isbn)
    i = 0
    value = 0
    
    while(i < size):
        value += int(isbn[i]) * (i + 1)
        i += 1
        
    value = value % 11
    
    if(value == 10):
        isbn = str(isbn + "X")
    else:
        isbn = isbn + str(value)
    print("The ISBN-10 number is",isbn)
                    
if __name__ == "__main__":
    main()