''' Chapter 7.3 '''

from Account import Account

def main():
    a1 = Account(1122, 20000.0, 0.045)
    a1.withdraw(2500)
    a1.deposit(3000)
    print("ID:",format(a1.getId(), ".2f"))
    print("Balance:",a1.getBalance())
    print("Monthly interest rate:",format(a1.getMonthlyInterestRate(), ".3%"))
    print("Monthly interest:",format(a1.getMonthlyInterest(), ".2f"))

if __name__ == '__main__':
    main()