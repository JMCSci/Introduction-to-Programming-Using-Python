'''
Chapter 2.17

Created on Jun 4, 2020

@author: jasonmoreau
'''
from datetime import date

# BMI = kilograms / meters^2

# One pound = 0.45359237 kilograms
# one inch = 0.0254 meters

pounds = input("Enter weight in pounds: ")
inches = input("Enter height in inches: ")

weightInKilograms = pounds * 0.45359237
heightInMeters = inches * 0.0254
BMI = weightInKilograms / heightInMeters ** 2

print "BMI is", BMI