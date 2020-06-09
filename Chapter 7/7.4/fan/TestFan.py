''' Chapter 7.4 '''

from Fan import Fan

def main():
    fan1 = Fan(Fan.FAST, True, 10, "Yellow")
    fan2 = Fan(Fan.MEDIUM, False, 5, "Blue")
    
    print("Fan 1 speed:",fan1.getSpeed())
    print("Fan 1 radius:",fan1.getRadius())
    print("Fan 1 color:",fan1.getColor())
    print("Fan 1 on:",fan1.getOn())
    blankLine()
    print("Fan 2 speed:",fan2.getSpeed())
    print("Fan 2 radius:",fan2.getRadius())
    print("Fan 2 color:",fan2.getColor())
    print("Fan 2 on:",fan2.getOn())

def blankLine():
    print()

if __name__ == '__main__':
    main()
    