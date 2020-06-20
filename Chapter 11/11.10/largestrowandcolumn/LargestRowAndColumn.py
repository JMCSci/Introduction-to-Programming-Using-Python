''' Chapter 11.10 '''

import random

def main():
    matrix = []
    createMatrix(matrix)
    printMatrix(matrix)
    mostOnes(matrix)
    
def createMatrix(matrix):
    sizeOfRow = 4
    sizeOfColumn = 4

    for i in range(sizeOfRow):
        matrix.append([])
        for j in range(sizeOfColumn):
            value = random.randint(0,1)
            matrix[i].append(value)
    
def printMatrix(matrix):
    row = len(matrix)
    column = len(matrix[0])
    
    for i in range(0, row):
        for j in range(0, column):
            print(matrix[i][j], end = " ")
        print()
 
def mostOnes(matrix):
    row = len(matrix)
    column = len(matrix[0])
    rowIndex = 0
    columnIndex = 0
    max = 0
    rowList = []
    columnList = []
    
    # ROW 
    for i in range(row):
        count = 0
        for j in range(column):
            if(matrix[i][j] == 1):
                count += 1   
        if(count > max):  
            rowList.clear()
            max = count
            rowIndex = i
            rowList.append(rowIndex)
        elif(count == max):
            rowIndex = i
            rowList.append(i)

    max = 0 # reset max
    count = 0 # reset count
    
    # COLUMN
    for i in range(row):
        count = 0
        for j in range(column):
            if(matrix[j][i] == 1):
                count += 1
        if(count > max): 
            columnList.clear()
            max = count
            columnIndex = i
            columnList.append(columnIndex)
        elif(count == max):
            columnIndex = i
            columnList.append(i)
        
    print("\nThe largest row index:", end = " ")       
    if(len(rowList) == 1):
        print(rowIndex, end = " ")
    elif(len(rowList) > 1):
        for i in rowList:
            print(i, end = " ")
            
    print("\nThe largest column index:", end = " ")
    if(len(columnList) == 1):
        print(columnIndex, end = " ")
    elif(len(columnList) > 1):
        for i in columnList:
            print(i, end = " ")

if __name__ == "__main__":
    main()