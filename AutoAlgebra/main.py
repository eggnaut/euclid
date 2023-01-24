from random import randint

def generateEq():
    a = f'{randint(endpt1, endpt2)}x^2'
    b = f'{randint(endpt1, endpt2)}x'
    c = f'{randint(endpt1, endpt2)}'

    eq = f'{a} + {b} + {c}'


eqNum = input('Please enter the number of equations you want: ')

while endpt1 > 0 and endpt1 >= endpt2:
    endpt1 = input('Please enter the first endpoint for the range (must be positive, not 0): ')
    endpt2 = input('Please enter the second endpoint for the range (should be greater than the first endpoint): ')

equations = []

for x in eqNum:
    eq = generateEq()
    equations.append(eq)

for eq in equations:
    print(eq)
    print('\n')