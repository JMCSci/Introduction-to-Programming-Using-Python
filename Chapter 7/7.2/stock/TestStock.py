''' Chapter 7.2 '''

from Stock import Stock

def main():
    
    s1 = Stock("INTC", "Intel Corporation", 20.5, 20.35)
    print(s1.getName())
    print(s1.getSymbol())
    print(format(s1.getChangePercent(), ".3%"))
    
if __name__ == '__main__':
    main()