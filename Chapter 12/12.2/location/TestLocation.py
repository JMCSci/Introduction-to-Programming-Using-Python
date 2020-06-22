''' Chapter 12.2 '''

from Location import Location

# 23.4 35 2 10
# 4.5 3 45 3.5
# 35 44 5.5 12.6

def main():
    rows, columns = eval(input("Enter the number of rows and columns in the list: "))
    location1 = Location()
    numbers0 = input("Enter row 0: ") 
    numbers1 = input("Enter row 1: ") 
    numbers2 = input("Enter row 2: ") 
    a = location1.createMatrix(numbers0, numbers1, numbers2, rows, columns)
    location2 = location1.locateLargest(a)
    print(location2.__str__())
    
if __name__ == "__main__":
    main()