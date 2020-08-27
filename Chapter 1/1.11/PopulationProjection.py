'''
Chapter 1.11

Created on Jun 3, 2020

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

year1 = CURRENT_POPULATION + year_net_change
year2 = year1 + year_net_change
year3 = year2 + year_net_change
year4 = year3 + year_net_change
year5 = year4 + year_net_change

print(year1) # 314812582.703
print(year2) # 317592679.407
print(year3) # 320372776.11
print(year4) # 323152872.813
print(year5) # 325932969.516


