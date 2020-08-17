''' Chapter 13.5 '''

import os.path, sys

def main():
    filename = input("Enter a filename: ")
    pathExists = os.path.exists(filename)
    if(pathExists == False):
        print("File does not exist")
        sys.exit(-1)
    else:
        file = open(filename, "r")
        oldString = input("Enter the old string to be replaced: ")
        newString = input("Enter the new string to be replaced: ")
        # Process file
        replaceString(file, oldString, newString)
        # Replace old file with new file
        os.replace("temp.txt", filename)
        # Complete
        print("Done")
        file.close()
            
def replaceString(file, oldString, newString):
    # Save to a new temp file 
    outFile = open("temp.txt", "w")
    line = file.readline()
    # Read each line from file
    # Replace string
    while line != "":
        line = line.replace(oldString, newString)
        outFile.write(line)
        
        line = file.readline()
    outFile.close()
        
def readFile(file):
    line = file.readline()
    while line != "":
        print(line)
        line = file.readline()

if __name__ == "__main__":
    main()