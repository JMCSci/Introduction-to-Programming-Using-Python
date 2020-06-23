''' Chapter 13.1 '''

def main():
    filename = input("Enter a filename: ")
    word = input("Enter string to be removed: ")
    fileRead = open(filename, "r")
    fileWrite = open("output.txt", "w")
    
    line = fileRead.readline()
    for line in fileRead:
        line = line.replace(word, "")   
        line = line.replace("  ", " ")  # remove double space
        fileWrite.write(line)
    print("Done")
   
    fileRead.close()
    fileWrite.close()
    
if __name__ == "__main__":
    main()