''' Chapter 7.7 '''

from LinearEquation import LinearEquation

def main():
    a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f: "))
    equation1 = LinearEquation(a, b, c, d, e, f)
    equation1.solve()

if __name__ == '__main__':
    main()