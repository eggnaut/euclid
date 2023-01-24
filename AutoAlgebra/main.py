from random import randint

def generateEq():
    a = f'{randint(endpt1, endpt2)}x^2'
    b = f'{randint(endpt1, endpt2)}x'
    c = f'{randint(endpt1, endpt2)}'

    eq = f'{a} + {b} + {c} = 0'
    return eq

eqNum = int(input('Please enter the number of equations you want: '))

repeat = True

while repeat:
  endpt1 = int(input('\nPlease enter the first endpoint for the range (must be positive, not 0): '))
  endpt2 = int(input('\nPlease enter the second endpoint for the range (should be greater than the first endpoint): '))

  if endpt1 > 0 and endpt1 < endpt2:
    repeat = False

equations = []

for x in range(eqNum):
  eq = generateEq()
  equations.append(eq)

for eq in equations:
  print('\n')
  print(eq)