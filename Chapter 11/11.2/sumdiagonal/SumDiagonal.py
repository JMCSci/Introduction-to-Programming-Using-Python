''' Chapter 11.2 '''

def main():
    row1 = input("Enter a 4-by-4 matrix for row 1: ")
    row2 = input("Enter a 4-by-4 matrix for row 2: ")
    row3 = input("Enter a 4-by-4 matrix for row 3: ")
    row4 = input("Enter a 4-by-4 matrix for row 4: ")
    
    elements1 = row1.split()
    elements2 = row2.split()
    elements3 = row3.split()
    elements4 = row4.split()
    
    m = [[eval(w) for w in elements1],
         [eval(x) for x in elements2],
         [eval(y) for y in elements3],
         [eval(z) for z in elements4]
         ]
    sumMajorDiagonal(m)
    
# 1 2 3 4
# 5 6.5 7 8
# 9 10 11 12
# 13 14 15 16

def sumMajorDiagonal(m):
    rows = len(m)
    columns =  len(m[0])
    sum = 0
    
    for i in range(columns):
        for j in range(rows):
            if(i == j):
                sum += m[j][i]
    
    print("Sum of the elements in the major diagonal is", sum)

if __name__ == "__main__":
    main()