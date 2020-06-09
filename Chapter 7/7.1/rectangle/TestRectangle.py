''' Chapter 7.1 '''

from Rectangle import Rectangle

def main():
    r1 = Rectangle(4,40)
    r2 = Rectangle(3.5, 35.7)
    
    print("The width of Rectangle 1 is:", r1.getWidth())
    print("The height of Rectangle 1 is:", r1.getHeight())
    print("The area of Rectangle 1 is:", r1.getArea())
    print("The perimeter of Rectangle 1 is:", r1.getPerimeter())
    blankLine()
    print("The width of Rectangle 2 is:", r2.getWidth())
    print("The height of Rectangle 2 is:", r2.getHeight())
    print("The area of Rectangle 2 is:", r2.getArea())
    print("The perimeter of Rectangle 2 is:", r2.getPerimeter())
 
# blankLine: Print an empty line      
def blankLine():
    print()


if __name__ == '__main__':
    main()