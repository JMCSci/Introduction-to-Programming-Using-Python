''' Chapter 12.2 '''

class Location:
    def __init__(self, row = 0, column = 0, maxValue = 0):
        self.row = row
        self.column = column
        self.maxValue = maxValue
        
    def createMatrix(self, numbers0, numbers1, numbers2, rows, columns):
        a = []
        r = rows
        c = columns
        
        elements0 = numbers0.split()
        elements1 = numbers1.split()
        elements2 = numbers2.split()
        
        for i in range(rows):
            list1 = [eval(elements0[x]) for x in range(i * r, i * c + r)]
            a.append(list1)
            
        for j in range(rows):
            list2 = [eval(elements1[y]) for y in range(j * r, j * c + r)]
            a.append(list2)
        
        for k in range(rows):
            list3 = [eval(elements2[z]) for z in range(k * r, k * c + r)]
            a.append(list3)  
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
        return "The location of the largest element is", str(self.maxValue) + " at (" + str(self.row) + "," + str(self.column) + ")" 