''' Chapter 6.18 '''

import random;

def main():
    n = eval(input("Enter n: "))
    printMatrix(n)
    
# printMatrix: Prints a n-by-n matrix of random integers from 0 - 1
def printMatrix(n):
    size = n * n
    i = 0
    
    while(i < size):
        if(i % n == 0):
            print()
        value = random.randint(0,1)
        print(value, end = " ")
        i += 1         

if __name__ == '__main__':
    main()