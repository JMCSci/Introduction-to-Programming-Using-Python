''' Chapter 10.17 '''

def main():
    s1, s2 = input("Enter two strings: ").split()
    isAnagram(s1, s2)
    
def isAnagram(s1, s2):
    size1 = len(s1)
    size2 = len(s2)
    lst1 = []
    lst2 = []
    
    if(size1 == size2):
        for i in range(0, size1):
            lst1.append(s1[i])
        
        for j in range(0, size2):
            lst2.append(s2[j])
         
        # sort list
        lst1.sort()
        lst2.sort()
        
        if(lst1 == lst2):
            print("Is an anagram")
        else:
            print("Is not a anagram") 
    else:
        print("Is not a anagram")
    
    

if __name__ == "__main__":
    main()