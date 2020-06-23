''' Chapter 13.3 '''

def main():
    filename = input("Enter a filename: ")
    fileInput = open(filename)    
    a = extractScores(fileInput)
    computeAverage(a)
    
def extractScores(fileInput):
    a = []
    score = fileInput.read()
    elements = score.split()
    a = [eval(x) for x in elements]
    return a
    
def computeAverage(a):
    total = 0
    size = len(a)
    
    for i in a:
        total += i
    
    average = total / size    
        
    print("There are",size,"scores")
    print("The total is", total)
    print("The average is", format(average, ".2f"))
    
if __name__ == "__main__":
    main()