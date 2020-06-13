''' Chapter 8.16 '''

def main():
    isbn = input("Enter the first 12 digits of an ISBN-13 as a string: ")
    checkISBN(isbn)
    
# checkISBN: Prints ISBN-13 number using 12 digits and a 13th digit checksum 
def checkISBN(isbn):
    i = 0
    size = len(isbn)
    value = 0
    
    while(i < size):
        if(i % 2 != 0):
            value += int(isbn[i])
        else:
            value += 3 * int(isbn[i])
        i += 1
           
    value = 10 - value % 10
    
    if(value == 10):
        isbn = isbn + "0"
    else:
        isbn = isbn + str(value)
    print(isbn)
     

if __name__ == "__main__":
    main()