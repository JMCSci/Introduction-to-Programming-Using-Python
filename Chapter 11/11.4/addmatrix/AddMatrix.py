''' Chapter 11.5 '''

def main():
    createMatrix()
   
   
   
def createMatrix():
    numberOfRows = eval(input("Enter the number of rows: "))
    numberOfColumns = eval(input("Enter the number of columns: "))
    a = []
    b = []
    
    print(numberOfRows,"X",numberOfColumns,"matrix created")
    
    print("\nEnter element values for Matrix A")
    for row in range(numberOfRows):
        a.append([])    # add row
        for column in range(numberOfColumns):
            value = eval(input("Enter an element: "))
            a[row].append(value) # add element to row index
      
    print("\nEnter element values for Matrix B")      
    for row in range(numberOfRows):
        b.append([])
        for column in range(numberOfColumns):
            value = eval(input("Enter an element: "))
            b[row].append(value)
    
    return a,b

def printMatrix(a, b):
    print("Matrix A")
    for i in a:
        for j in i:
            print(j, end = " ")
        print()
    
    print()
    
    print("Matrix B")
    for i in b:
        for j in i:
            print(j, end = " ")
        print()
    
    
    return a, b  
    

def addMatrix(a, b):
    pass


if __name__ == "__main__":
    main()