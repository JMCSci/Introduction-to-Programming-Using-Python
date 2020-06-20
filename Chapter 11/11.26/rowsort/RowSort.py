''' Chapter 11.26 '''

def main():
    m = []    
    createMatrix(m)
    sortRows(m)
    print("The row-sorted list is ")
    printMatrix(m)
    
# 0.15 0.875 0.375
# 0.55 0.005 0.225
# 0.30 0.12 0.4
  
def createMatrix(m):
    print("Enter a 3-by-3 matrix row by row:")
    number0 = input()
    number1 = input()
    number2 = input()
    
    elements0 = number0.split()
    elements1 = number1.split()
    elements2 = number2.split()
    
    m.append([eval(x) for x in elements0])
    m.append([eval(y) for y in elements1])
    m.append([eval(z) for z in elements2])
    
def sortRows(m):
    rows = len(m) 
    columns = len(m[0])
    
    for i in range(0, rows):
        for j in range(0, columns - 1):
            if(m[i][j] > m[i][j + 1]):
                temp = m[i][j + 1]
                m[i][j + 1] = m[i][j]
                m[i][j] = temp  

def printMatrix(m):
    rows = len(m) 
    columns = len(m[0])
    
    for i in range(0, rows):
        for j in range(0, columns):
            print(format(m[i][j],".3f"), end = " ")
        print()

if __name__ == "__main__":
    main()