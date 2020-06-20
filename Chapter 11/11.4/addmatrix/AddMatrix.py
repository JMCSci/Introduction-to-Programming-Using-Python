'''' Chapter 11.5 '''

def main():
    a, b = createMatrix()    
    c = addMatrix(a, b)
    printMatrix(c)
   
# 1 2 3 4 5 6 7 8 9
# 0 2 4 1 4.5 2.2 1.1 4.3 5.2
   
def createMatrix():
    numberOfRows = eval(input("Enter the number of rows: "))
    numberOfColumns = eval(input("Enter the number of columns: "))
    a = []
    b = []
    
    print("Two",numberOfRows,"X",numberOfColumns,"matrices created.")
    
    numbers1 = input("\nEnter numbers for Matrix A: ") # add element to row index
    elements1 = numbers1.split()
    for i in range(numberOfRows):
        list1 = [eval(elements1[x]) for x in range(numberOfRows * i, numberOfColumns * i + numberOfRows)]
        a.append(list1)
            
    numbers2 = input("\nEnter numbers for Matrix B: ")
    elements2 = numbers2.split()
    for i in range(numberOfRows):
        list2 = [eval(elements2[x]) for x in range(numberOfRows * i, numberOfColumns * i + numberOfRows)]
        b.append(list2)
            
    return a, b

def addMatrix(a, b):
    rows = len(a)
    columns = len(a[0])
    c = []
    
    for i in range(rows):
        c.append([])
        for j in range(columns):
            sum = 0
            sum += a[i][j] + b[i][j]
            c[i].append(sum)
    
    return c

def printMatrix(matrix):
    for row in matrix:
        for value in row:
            print(format(value, ".1f"), end = format(" ", "<2s"))
        print()
    
    print()
    
if __name__ == "__main__":
    main()