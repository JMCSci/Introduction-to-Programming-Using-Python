''' Chapter 7.6 '''

from QuadraticEquation import QuadraticEquation

def main():
    equation1 = QuadraticEquation(9, -12, 4)
    equation2 = QuadraticEquation(3, -5, -1)
    equation3 = QuadraticEquation(1, 2, 2)
    
    equation1.solve()
    blankLine()
    equation2.solve()
    blankLine()
    equation3.solve()
      
def blankLine():
    print()
  
  
if __name__ == '__main__':
    main()