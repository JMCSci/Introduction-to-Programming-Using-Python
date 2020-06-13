''' Chapter 8.11 '''

def main():
    s = input("Enter a string: ")
    reverse(s)
    
# reverse: Displays a reversed string
def reverse(s):
    size = len(s)
    i = size
    
    while(i > 0):
        s += s[i - 1]    
        i -= 1
    
    s = s[size:len(s)]
    print(s)
        
if __name__ == '__main__':
    main()