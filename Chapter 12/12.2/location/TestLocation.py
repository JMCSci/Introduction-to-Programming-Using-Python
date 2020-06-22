''' Chapter 12.2 '''

from Location import Location

# 23.4 35 2 10
# 4.5 3 45 3.5
# 35 44 5.5 12.6

def main():
    rows, columns = eval(input("Enter the number of rows and columns in the list: "))
    location1 = Location()
    a = location1.createMatrix(rows, columns)
    location2 = location1.locateLargest(a)
    print(location2.__str__())
    
if __name__ == "__main__":
    main()