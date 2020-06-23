''' Chapter 13.2 '''

def main():
    filename = input("Enter a filename: ")
    fileInput = open(filename)
    characterCount = 0
    wordCount = 0
    lineCount = 0
    
    for line in fileInput:
        for i in line:
            if(i == " "):
                wordCount += 1
            else:
                characterCount += 1
        if(not line.endswith(" ")):
            characterCount += 1
        lineCount += 1
        
    print(characterCount,"characters")
    print(wordCount,"words")
    print(lineCount,"lines")
    
    fileInput.close()
         

if __name__ == "__main__":
    main()