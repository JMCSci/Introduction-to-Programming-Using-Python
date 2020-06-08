''' Chapter 6.17 '''

import math

def main():
    side1, side2, side3 = eval(input("Enter three sides in double: "))
    result = isValid(side1, side2, side3)
    if(result == True):
        areaOfTriange = area(side1, side2, side3)
        print("The area of the triangle is", areaOfTriange)
    else:    
        print("Input is invalid")
       
# isValid: Checks to see of it is a valid triangle -- returns a boolean
def isValid(side1, side2, side3):
    if(side1 + side2 > side3):
        if(side1 + side3 > side2):
            if(side2 + side3 > side1):
                return True
    else:
        return False

# area: Computers the area of a triangle
def area(side1, side2, side3):
    perimeter = (side1 + side2 + side3) / 2
    area = math.sqrt(perimeter * (perimeter - side1) * (perimeter - side2) \
                     * (perimeter - side3))
    return area


if __name__ == '__main__':
    main()