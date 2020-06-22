''' Chapter 12.2 '''

class Location:
    def __init__(self, row = 0, column = 0, maxValue = 0):
        self.row = row
        self.column = column
        self.maxValue = maxValue
        
    def createMatrix(self, rows, columns):
        a = []
        r = rows
        c = columns
        
        for i in range(0,rows):
            a.append([])
            for j in range(0, columns):
                values = eval(input("Enter values for row: "))
                a[i].append(values)
           
        return a
    
    def locateLargest(self, a):
        numberOfRows = len(a)
        numberOfColumns = len(a[0])
        max = 0
        rowIndex = 0
        columnIndex = 0
        
        for i in range(numberOfRows):
            for j in range(numberOfColumns):
                if(a[i][j] > max):
                    max = a[i][j]
                    rowIndex = i
                    columnIndex = j  
                    
        self.maxValue = max
        self.row = rowIndex
        self.column = columnIndex 
        return Location(self.row, self.column, self.maxValue)
    
    def __str__(self):
        return "The location of the largest element is" + str(self.maxValue) + " at (" + str(self.row) + "," + str(self.column) + ")" 