''' Chapter 10.11 '''

import random

def main():
    numbers = input("Enter numbers: ")
    elements = numbers.split()
    lst = [eval(x) for x in elements]
    shuffle(lst)

def shuffle(lst):
    size = len(lst)
    lst2 = []
    
    lst2 = random.sample(lst, size)    
    
    print(lst2)
    
if __name__ == "__main__":
    main()