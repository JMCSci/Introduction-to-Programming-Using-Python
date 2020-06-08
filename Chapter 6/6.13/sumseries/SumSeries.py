''' Chapter 6.13 '''

def main():
    sumSeries();

# sumSeries: Computes and prints a series -- m(i) = 1/2 + 2/3 + ... i/ i + 1
def sumSeries():
    sum = 0;
    print(format("i", "<15s"), "m(i)\n");
    for i in range(1, 21):
        sum += i / (i + 1);
        print(format(i, "<15.0f"), format(sum, "0.4f"));
        

if __name__ == '__main__':
    main();