''' Chapter 10.26 '''

def main():
    numbers1 = input("Enter list1: ")
    numbers2 = input("Enter list2: ")
    elements1 = numbers1.split()
    elements2 = numbers2.split()
    list1 = [eval(x) for x in elements1]
    list2 = [eval(x) for x in elements2]
    list3 = merge(list1, list2)
    printList(list3)
 
def merge(list1, list2):
    size = len(list1) + len(list2)
    temp = 0
    list3 = list1 + list2
    
    for i in range(0, size - 1):
        for j in range(0, size - 1):
            if(list3[j] > list3[j + 1]):
                temp = list3[j + 1]
                list3[j + 1] = list3[j]
                list3[j] = temp
    return list3

def printList(list):
    print("The merged list is:", end = " ")
    for i in list:
        print("", end = str(i) + " ")
    
if __name__ == "__main__":
    main()