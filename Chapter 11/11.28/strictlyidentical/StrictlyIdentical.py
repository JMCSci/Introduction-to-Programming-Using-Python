''' Chapter 11.28 '''

def main():
    m1 = []
    m2 = []
    createMatrix(m1,m2)
    equal(m1, m2)

# 51 22 25 6 1 4 24 54 6
# 51 25 22 6 1 4 24 54 6

def createMatrix(m1, m2):
    numbers1 = input("Enter m1: ")
    numbers2 = input("Enter m2: ")
    
    elements1 = numbers1.split()
    elements2 = numbers2.split()
    
    # For a 3 x 3 matrix
    for i in range(3):
        list1 = [eval(elements1[x]) for x in range(3 * i, 3 * i + 3)]
        m1.append(list1)
        
    for j in range(3):
        list2 = [eval(elements2[y]) for y in range(3 * j, 3 * j + 3)]
        m2.append(list2)


def equal(m1, m2):
    numberOfRows = len(m1)
    numberOfColumns = len(m1[0])
    flag = True
    
    for i in range(0, numberOfRows):
        if(flag == False):
            break
        for j in range(0, numberOfColumns):
            if(m1[i][j] == m2[i][j]):
                flag = True
            else:
                flag = False
                break
    
    if(flag == True):
        print("The two lists are strictly identical")
        return True
    else: 
        print("The two lists are not strictly identical")
        return False
        
def printMatrix(matrix):
    for row in matrix:
        for value in row:
            print(format(str(value), ">2s"), end = " ")
        print()
    
    print() 
    
if __name__ == "__main__":
    main()