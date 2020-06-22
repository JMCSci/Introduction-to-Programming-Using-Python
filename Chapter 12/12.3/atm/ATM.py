''' Chapter 12.3 '''

from Account import Account

def main(): 
    # Create accounts    
    accountList = []
    createAccounts(accountList)
    start = True
    while(start):
        id = eval(input("Enter an account id: "))
        # Pull from list data structure 
        # Notice that a 'cast' has been used to access the class functions
        if(id >= 0 and id <= 9):
            optionsMenu()
            acct = Account(accountList[id])
            choice = eval(input("Enter a choice: "))
            if(choice == 1):
                print("\nThe balance is:",acct.getBalance())
            elif(choice == 2):
                withdrawlAmount = eval(input("Enter withdrawal amount: "))
                acct.withdraw(withdrawlAmount)
                accountList[id] = acct
            elif(choice == 3):
                depositAmount = eval(input("Enter deposit amount: "))
                acct.deposit(depositAmount)
                accountList[id] = acct
            elif(choice == 4):
                start = False
                print("\nGoodbye")
                break
            else:
                print("Incorrect selection")
        else:
            print("Incorrect id")
    
    
    
    
    
    
    

     
def createAccounts(accountList):
    for i in range(0, 10):
        accountList.append([])
        for j in range(0, 1):
            id = i
            balance = 100
            a = Account(id, balance, 0.0)
            accountList[i].append(a)
    
    #b = Account(accountList[0])
    #b.withdraw(1000)
    #print(b.getBalance())
    
 
            
def optionsMenu():
    print("\nMain menu")
    print("1. Check balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")

if __name__ == "__main__":
    main()