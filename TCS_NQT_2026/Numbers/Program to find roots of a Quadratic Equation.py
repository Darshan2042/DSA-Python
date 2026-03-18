# Program to find roots of a Quadratic Equation.

import math

def quadratic_roots(a, b, c):
    d = b*b - 4*a*c   # discriminant

    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        print("Two real roots:", root1, root2)

    elif d == 0:
        root = -b / (2*a)
        print("One real root:", root)

    else:
        real = -b / (2*a)
        imag = math.sqrt(-d) / (2*a)
        print("Complex roots:", real, "+ i", imag, "and", real, "- i", imag)


# Example
quadratic_roots(1, -5, 6)