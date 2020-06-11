''' Chapter 8.2 '''

def main():
    myString = input("Enter a string: ")
    mySubstring = input("Enter a substring to be found: ")
    print(find(myString, mySubstring))
    
# find: Finds substring -- returns first letter index of string
def find(myString, mySubstring):
    for i in range(0,len(myString)):
        # If the first letter is found check next -- else break off
        if(mySubstring[0] == myString[i]):
            size = len(mySubstring)
            j = 0
            k = i  # set next letter for while loop
            match = False
            while(j < size and k < len(myString)):
                if(mySubstring[j] == myString[k]):
                    match = True
                    j += 1
                    k += 1
                    if(j == size):
                        if(match == True):
                            return i
                        else:
                            match = False
                            return -1
                    continue
                else: 
                    match = False
                    break 
            return -1

if __name__ == '__main__':
    main()