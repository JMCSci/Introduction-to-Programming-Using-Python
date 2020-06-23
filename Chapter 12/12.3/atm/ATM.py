''' Chapter 12.3 '''

from Account import Account

def main(): 
    # Create accounts    
    accountList = []
    createAccounts(accountList)
    atm(accountList)
 
def atm(accountList):
    start = True
    while(start):
        id = eval(input("Enter an account id: "))
        # Retrieve Account object from List data structure 
        if(id >= 0 and id <= 9):
            optionsMenu()
            a = accountList[id]
            choice = eval(input("Enter a choice: "))
            if(choice == 1):
                print("\nThe balance is:",a.getBalance())
            elif(choice == 2):
                withdrawlAmount = eval(input("Enter withdrawal amount: "))
                a.withdraw(withdrawlAmount)
                accountList[id] = a
            elif(choice == 3):
                depositAmount = eval(input("Enter deposit amount: "))
                a.deposit(depositAmount)
                accountList[id] = a
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
        id = i
        balance = 100
        a = Account(id, balance, 0.0)
        accountList.append(a)
         
def optionsMenu():
    print("\nMain menu")
    print("1. Check balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")

if __name__ == "__main__":
    main()