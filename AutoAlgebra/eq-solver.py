import cmath as cm

def isInt(num: float | int) -> bool:
    return ((num % 1) == 0)

a = int(input('\nPlease enter the value of \'a\' in the qudratic equation: '))
b = int(input('\nPlease enter the value of \'b\' in the qudratic equation: '))
c = int(input('\nPlease enter the value of \'c\' in the qudratic equation: '))
d = int(input('\nPlease enter what the quadratic expression is equal to: '))

c -= d

if isInt(cm.sqrt(b**2 - 4 * a * c)):
    if isInt(((-b + (cm.sqrt(b**2 - 4 * a * c))) / 2 * a)):
        sol1 = (-b + (cm.sqrt(b**2 - 4 * a * c))) / 2 * a
        sol2 = (-b - (cm.sqrt(b**2 - 4 * a * c))) / 2 * a
    else:
        sol1 = f'{-b + (cm.sqrt(b**2 - 4 * a * c))} / {2 * a}'
        sol2 = f'{-b - (cm.sqrt(b**2 - 4 * a * c))} / {2 * a}'
else:
    sol1 = f'(-{b} + sqrt({b**2 - 4 * a * c})) / {2 * a}'
    sol2 = f'(-{b} - sqrt({b**2 - 4 * a * c})) / {2 * a}'

print(f'\nThe two solutions to the quadratic equation are {sol1} and {sol2}.')