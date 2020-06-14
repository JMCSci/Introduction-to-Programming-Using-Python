''' Test '''

from Circle2D import Circle2D

def main():
    x1, y1, radius1 = eval(input("Enter x1, y1, radius: "))
    x2, y2, radius2 = eval(input("Enter x2, y2, radius: "))
    c1 = Circle2D(x1, y1, radius1)
    c2 = Circle2D(x2, y2, radius2)
    
    print("Area for c1 is",c1.getArea())
    print("Perimeter for c1 is",c1.getPerimeter())
    print("Area for c2 is",c2.getArea())
    print("Perimeter for c2 is",c2.getPerimeter())
    print("c1 contains the center of c2?",c1.containsPoint(c2.getX(), c2.getY()))
    print("c1 contains c2?",c1.contains(c2))
    print("c1 overlaps c2?",c1.overlaps(c2))

if __name__ == "__main__":
    main()