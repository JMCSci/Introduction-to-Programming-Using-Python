''' Chapter 11.29 '''

def main():
    m1 = []
    m2 = []
    createMatrix(m1,m2)
    equal(m1,m2)

# 51 25 22 6 1 4 24 54 6
# 51 25 22 6 1 4 24 54 6

def createMatrix(m1, m2):
    numberOfRows = 3
    numberOfColumns = 3
    
    numbers1 = input("Enter m1: ")
    numbers2 = input("Enter m2: ")
    
    elements1 = numbers1.split()
    elements2 = numbers2.split()
    
    for i in range(numberOfRows):
        list1 = [eval(elements1[x]) for x in range(numberOfRows * i, numberOfColumns * i + numberOfRows)]
        m1.append(list1)
        
    for j in range(numberOfRows):
        list2 = [eval(elements2[y]) for y in range(numberOfRows * j, numberOfColumns * j + numberOfRows)]
        m2.append(list2)


def equal(m1, m2):
    numberOfRows = len(m1)
    numberOfColumns = len(m1[0])
    flag = True
    
    m1.sort()
    m2.sort()
    
    for i in range(0, numberOfRows):
        if(flag == False):
            break
        for j in range(0, numberOfColumns):
            if(m1[i][j] == m2[i][j]):
                flag = True
            else:
                flag = False 
    
    if(flag == True):
        print("The two lists are identical")
    else: 
        print("The two lists are not identical") 

       
def printMatrix(matrix):
    for rows in matrix:
        for value in rows:
            print(format(str(value), ">2s"), end = " ")
        print()
        
if __name__ == "__main__":
    main()