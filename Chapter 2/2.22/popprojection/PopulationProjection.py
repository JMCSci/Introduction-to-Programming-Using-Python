'''
Chapter 2.22

Created on Jun 4, 2020

@author: jasonmoreau
'''

# 1 birth every 7 seconds
# 1 death every 13 seconds
# 1 new immigrant every 45 seconds

CURRENT_POPULATION = 312032486

birth = 24 * (60.0 / 7 * 60.0)           # births in one day
death = 24 * (60.0 / 13 * 60.0)          # deaths in one data
immigration = 24 * (60.0 / 45 * 60.0)    # immigration in one day

one_day = birth + immigration - death # net change in one day
year_net_change = one_day * 365

numberOfYears = input("Enter the number of years: ")

population = CURRENT_POPULATION + (year_net_change * numberOfYears) 

print "The population in", numberOfYears, "years is", format(population, ".0f")

# Year 1: 314812582.703
# Year 2: 317592679.407
# Year 3: 320372776.11
# Year 4: 323152872.813
# Year 5: 325932969.516