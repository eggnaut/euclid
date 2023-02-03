# imports functions/classes from modules
from cmath import sqrt

# a function that returns True if the val is an int
def isInt(num: float | int) -> bool:
    return (num % 1) == 0

# a function that returns True if the val is positive or 0
def isPos(num : float | int) -> bool:
    return num >= 0

# solves quadratic equations if possible
def solveEq(a: int, b: int, c: int) -> str | int:
    p1 = -b
    p2 = (b**2) - (4 * a * c)
    p3 = 2 * a

    if not isInt(sqrt(p2)):
        p2 = f'sqrt({p2})'
    else:
        p2 = sqrt(p2)
    
    p1 = -b + p2
    p4 = -b - p2
    
    if not isInt(p1 / p3):
        p3 = f'{p1} / {p3}'
    else:
        p3 = p1 / p3

    if not isInt(p4 / p3):
        p5 = f'{p4} / {p3}'
    else:
        p5 = p4 / p3

    solutions = (p3, p5)

    return solutions
