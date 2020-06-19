''' Chapter 11.1 '''

def main():
    num0 = input("Enter a 3-by-4 matrix row for row 0: ")
    num1 = input("Enter a 3-by-4 matrix row for row 1: ")
    num2 = input("Enter a 3-by-4 matrix row for row 2: ")
    columnIndex = eval(input("Enter a column to sum: "))
    
    element0 = num0.split()
    element1 = num1.split()
    element2 = num2.split()
    
    m = [[eval(x) for x in element0],
         [eval(y) for y in element1],
         [eval(z) for z in element2]]
    
    sumColumn(m, columnIndex)
 
# 1.5 2 3 4
# 5.5 6 7 8
# 9.5 1 3 1
 
def sumColumn(m, columnIndex):
    sum = 0
    size = len(m)
    
    for i in range(size):
        sum += m[i][columnIndex]
        
    print("Sum of the elements for column", columnIndex,"is",sum)
    
if __name__ == "__main__":
    main()