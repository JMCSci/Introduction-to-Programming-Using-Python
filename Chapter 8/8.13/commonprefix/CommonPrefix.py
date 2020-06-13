''' Chapter 8.13 '''

def main():
    s1 = input("Enter a string: ")
    s2 = input("Enter prefix: ")
    prefix(s1, s2)
    
# prefix: Returns the longest common prefix of two string (s3)
def prefix(s1, s2):
    size = len(s2)
    i = 0
    s3 = ""
    
    if(s1[0] == s2[0]):
        while(i < size):
            if(s1[i] == s2[i]):
                s3 += s1[i]
                i += 1
            else:
                break    
                 
    print(s3)
    return s3


if __name__ == "__main__":
    main()