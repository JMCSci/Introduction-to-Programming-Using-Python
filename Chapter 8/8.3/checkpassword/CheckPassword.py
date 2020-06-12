''' Chapter 8.3 '''

def main():
    password = input("Enter password: ")
    checkPassword(password)
    
# checkPassword: Checks password string to see if it is valid   
def checkPassword(password):
    numberOfDigits = 0
    numberOfLetters = 0
    
    if(len(password) >= 8):     # At least 8 characters
        for i in range(0, len(password)):
            if(password[i].isalpha()):      # Only letters and digits     
                numberOfLetters += 1
            else:
                numberOfDigits += 1
        if(numberOfLetters >= 1 and numberOfDigits >= 2):   # At least two digits and remaining letters
            print("Valid password")
            return
        else:
            print("Invalid password")
            return
    else: 
        print("Invalid password")
        

if __name__ == '__main__':
    main()
