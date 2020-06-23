''' Chapter 13.4 '''

import random, os.path

def main():
    filename = input("Enter a filename: ")
    pathExists = os.path.exists(filename)   # check if file exists
    if(pathExists == False):
        fileOutput = open(filename, "a")
        for i in range(0, 100):
            value = random.randint(0, 200)
            fileOutput.write(str(value) + " ")
        fileOutput.close()
        a = readFile(filename)
        sortList(a)
        printValues(a)
    else:
        print("The file already exists")
        
def readFile(filename):
    lst = []
    fileInput = open(filename, "r")
    
    values = fileInput.read()
    elements = values.split()
    lst = [eval(x) for x in elements]
    fileInput.close()
    return lst
    
def sortList(a):
    temp = 0
    size = len(a)
    
    for i in range(0, size - 1):
        for j in range(0, size - 1):
            if(a[j] > a[j + 1]):
                temp = a[j + 1]
                a[j + 1] = a[j]
                a[j] = temp

def printValues(a):
    size = len(a)
    for i in range(0, size):
        print(a[i], end = " ")
    
if __name__ == "__main__":
    main()