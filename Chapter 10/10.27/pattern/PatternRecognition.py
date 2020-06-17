''' Chapter 10.27 '''

def main():
    numbers = input("Enters numbers: ")
    elements = numbers.split()
    values = [eval(x) for x in elements]
    isConsecutuveFour(values)

def isConsecutuveFour(values):
    flag = False
    size = len(values)
    count = 0
    
    for i in values:
        if(flag == True):
            break
        count = 0
        for j in range(0, size):
            if(i == values[j]):
                count += 1
                if(count > 3):
                    flag = True
            else:
                count = 0
                
    if(flag == True):
        print("List contains four consecutive identical values")    
    else: 
        print("List does not contain four consecutive identical values")
    


if __name__ == "__main__":
    main()