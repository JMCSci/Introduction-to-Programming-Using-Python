'''
Created on Jun 3, 2020

Chapter 2.5 

@author: jasonmoreau
'''

subtotal, gratuityRate = input("Enter the subtotal and a gratuity rate: ")
gratuityAmount = subtotal * gratuityRate / 100 
total = subtotal + gratuityAmount
print "The gratuity is", gratuityAmount, "and the total is", total 