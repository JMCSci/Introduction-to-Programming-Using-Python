''' Chapter 6.16 '''

def main():
    year = int(input("Enter year: "))
    
    print(format("\nYear", "<15s"), "Days")
    
    while(year <= 2020):
        daysInYear = numberOfDaysInYear(year)
        print(format(str(year),"<15s"), daysInYear)
        year += 1
    
# numberOfDaysInYear: Returns the number of days in a given year
def numberOfDaysInYear(year):
    if(year % 4 != 0):
        days = 365
    elif(year % 100 != 0): 
        days = 366
    elif(year % 400 != 0):
        days = 365
    else:
        days = 366
    return days;    
            
if __name__ == '__main__':
    main()