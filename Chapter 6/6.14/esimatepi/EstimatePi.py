''' Chapter 6.14 '''

import math;

def main():
    num = 1;
    i = int(input("Enter a value for i: "));
    print(format("i", "<15s"), "m(i)\n");
    
    while(num <= i):
        result = estimatePI(num);
        print(format(str(num),"<15s"), format(result, ".4f"))
        num += 100;
             
# estimatePI: Computes and returns the sum of a series -- m(i) = 4(1 - 1/3 + 1/5 - 1/7 + 
#     1/9 - 1/11 + ... (-1)^ i + 1 / 2i - 1)    
def estimatePI(i):
    sum = 0;
    for i in range(1, i + 1):
        sum += 4 * (pow(-1, i + 1)) / (2 * i - 1);           
    return sum

if __name__ == '__main__':
    main();