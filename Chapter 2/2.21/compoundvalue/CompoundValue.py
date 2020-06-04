'''
Chapter 2.21

Created on Jun 4, 2020

@author: jasonmoreau
'''

MONTHLYINTERESTRATE = 0.05 / 12

savingsAmount = input("Enter the monthly savings amount: ")

monthOne = savingsAmount * (1 + MONTHLYINTERESTRATE)
monthTwo = (savingsAmount + monthOne) * (1 + MONTHLYINTERESTRATE)
monthThree = (savingsAmount + monthTwo) * (1 + MONTHLYINTERESTRATE)
monthFour = (savingsAmount + monthThree) * (1 + MONTHLYINTERESTRATE)
monthFive = (savingsAmount + monthFour) * (1 + MONTHLYINTERESTRATE)
monthSix = (savingsAmount + monthFive) * (1 + MONTHLYINTERESTRATE)

print "After the sixth month, the account value is", format(monthSix, ".2f")





