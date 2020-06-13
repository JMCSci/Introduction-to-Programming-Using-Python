''' Test '''

from Point import Point

def main():
    x1, y1, x2, y2 = eval(input("Enter two points: "))
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    
    print("The distance between the two points is", format(p1.distance(p2), ".2f"))
    if(p1.nearBy(p2) == True):
        print("The two points are near each other")
    else:
        print("The two points are not near each other")
        
    print(p1)
    print(p2)


if __name__ == "__main__":
    main()
