''' Chapter 8.1 '''

# FORMAT: 123-45-6789
# String array values: 0, 1, 2, - 4, 5, - 7, 8, 9, 10

def main():
    ssn = input("Enter social security number: ")
    checkSSN(ssn)
 
def checkSSN(ssn):
    if(ssn[3] == "-" and ssn[6] == "-"):
        for ch in range(0, 10):
            if(ch % 3 == 0 or ch % 6 == 0):
                continue;
            else:
                if(ssn[ch].isdigit()):
                    continue
                else: 
                    print("Invalid SSN")
                    return
        print("Valid SSN")
    else: 
        print("Invalid SSN")        
    

if __name__ == '__main__':
    main()
