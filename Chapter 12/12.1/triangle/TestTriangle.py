''' Chapter 12.1 '''

from TriangleFromGeometricObject import Triangle

def main():
    side1, side2, side3 = eval(input("Enter 3 sides of triangle: "))
    color = input("Enter a color: ")
    filled = eval(input("Is it filled? True or False: "))
    triangle = Triangle(side1, side2, side3)
    if(filled == 1):
        fill = True
        triangle.setFilled(fill)
    else:
        fill = False
        triangle.setFilled(fill)
   
    triangle.setColor(color)
    print(triangle)

if __name__ == "__main__":
    main()