''' Chapter 8.6 '''

def main():
    s = input("Enter a string: ")
    countLetters(s)
    
# countLetters: Displays the number of letters in a string
def countLetters(s):
    i = 0
    count = 0
    size = len(s)
    
    while(i < size):
        if(s[i].isalpha() == True):
            count += 1
        i += 1
    
    if(count == 0):
        print("There are no letters in this string")
    elif(count == 1):
        print("There is one letter in this string")
    else:
        print("There are", count,"letters in this string")

if __name__ == "__main__":
    main()