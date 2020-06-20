''' Chapter 11.27 '''

def main():
    m = []
    createMatrix(m)
    sortColumns(m)
    print("The column-sort list is ")
    printMatrix(m)

# 0.15 0.875 0.375
# 0.55 0.005 0.225
# 0.30 0.12 0.4 

def createMatrix(m):
    print("Enter a 3-by-3 matrix row by row: ")
    
    numbers0 = input()
    numbers1 = input()
    numbers2 = input()
    
    elements0 = numbers0.split()
    elements1 = numbers1.split()
    elements2 = numbers2.split()
    
    m.append([eval(x) for x in elements0])
    m.append([eval(y) for y in elements1])
    m.append([eval(z) for z in elements2])

def sortColumns(m):
    numberOfRows = len(m)
    numberOfColumns = len(m[0])
    
    for i in range(0, numberOfRows - 1):
        for j in range(0, numberOfColumns):
            if(m[i][j] > m[i + 1][j]):
                temp = m[i + 1][j]
                m[i + 1][j] = m[i][j]
                m[i][j] = temp 

def printMatrix(m):
    numberOfRows = len(m)
    numberOfColumns = len(m[0])
    
    for i in range(0, numberOfRows):
        for j in range(0, numberOfColumns):
            print(format(m[i][j], ".3f"), end = " ")
        print()
        

if __name__ == "__main__":
    main()