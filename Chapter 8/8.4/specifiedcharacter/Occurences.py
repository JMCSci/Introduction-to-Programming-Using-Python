''' Chapter 8.4 '''

def main():
    s = input("Enter a string: ")
    ch = input("Enter a character: ")
    count(s, ch)

# count: Prints the number of occurences of a character in a specified string
def count(s, ch):
    size = len(s)
    i = 0
    characterCount = 0
    
    while(i < size):
        if(ch == s[i]):
            characterCount += 1        
        i += 1
    if(characterCount == 0):
        print(ch,"does not occur in this string")
    elif(characterCount == 1):
        print(ch, "occurs",characterCount,"time")
    else: 
        print(ch,"occurs",characterCount,"times")

if __name__ == '__main__':
    main()