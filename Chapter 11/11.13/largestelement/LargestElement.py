''' Chapter 11.13 '''

def main():
    a = []
    createMatrix(a)
    locateLargest(a)
    
# 23.5 35 2 10 
# 4.5 3 45 3.5
# 35 44 5.5 11.6

def createMatrix(a):
    numberOfRows = eval(input("Enter the number of rows in the list: "))
    row0 = input("Enter a row0: ")
    row1 = input("Enter a row1: ")
    row2 = input("Enter a row2: ")
    
    number0 = row0.split()
    number1 = row1.split()
    number2 = row2.split()
    
    a.append([eval(x) for x in number0])
    a.append([eval(x) for x in number1])
    a.append([eval(x) for x in number2])
 
def printMatrix(a):
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            print(format(a[i][j], ".1f"), end = format("", ">3s"))
        print()
        
def locateLargest(a):
    row = len(a)
    column = len(a[0])
    rowIndex = 0
    columnIndex = 0
    max = 0
    
    for i in range(0, row):
        for j in range(0, column):
            if(a[i][j] > max):
                max = a[i][j] 
                rowIndex = i
                columnIndex = j
    
    print("The location of the largest element is (" + str(rowIndex) + 
          "," + str(columnIndex) + ")")
      
if __name__ == "__main__":
    main()