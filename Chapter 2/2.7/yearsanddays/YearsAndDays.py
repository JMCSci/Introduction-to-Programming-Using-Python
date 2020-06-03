'''
Created on Jun 3, 2020

Chapter 2.8

@author: jasonmoreau
'''

# Days in a year
year = 365
# Minutes in a day
minutesInDay = 1440
# Minutes in a year
totalMinutesInYear = year * minutesInDay

minutes = input("Enter the number of minutes: ")
totalYears = minutes / totalMinutesInYear  
totalDays = (minutes % totalMinutesInYear) / minutesInDay

print minutes, "minutes is approximately", totalYears, "years and", totalDays, "days"