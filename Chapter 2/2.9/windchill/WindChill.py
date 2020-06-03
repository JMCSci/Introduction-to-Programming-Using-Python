'''
Chapter 2.9

Created on Jun 3, 2020

@author: jasonmoreau
'''

temperature = input("Enter the temperature in Fahrenheit between -58 and 41: ")
windSpeed = input("Enter the wind speed in miles per hour: ")
windChill = (35.74 + 0.6215 * temperature - 35.75 * windSpeed ** 0.16  
    + 0.4275 * temperature * windSpeed ** 0.16) 
print "The wind chill index is", windChill