''' Chapter 8.2 '''

def main():
    myString = input("Enter a string: ")
    mySubstring = input("Enter a substring to be found: ")
    print(find(myString, mySubstring))
    
# find: Finds substring -- returns first letter index of string
def find(myString, mySubstring):
    for i in range(0,len(myString)):
        # If the first letter is found, enter loop to check next
        if(mySubstring[0] == myString[i]):
            size = len(mySubstring)
            j = 0  # index for mySubstring variable 
            k = i  # index for myString variable -- current outer loop index
            match = False
            while(j < size and k < len(myString)):
                if(mySubstring[j] == myString[k]):
                    match = True    # boolean flag for each index in string
                    j += 1
                    k += 1
                    if(j == size):  # when index of mySubstring reaches the end -- check flag
                        if(match == True):
                            return i
                        else:
                            match = False
                            return -1
                    continue
                else:       # if the next character in index doesnt match -- start again from outer loop
                    match = False
                    break 
            return -1

if __name__ == '__main__':
    main()