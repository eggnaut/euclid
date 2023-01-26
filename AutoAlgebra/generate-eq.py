from random import randint
from fpdf import FPDF

def generateEq():
  a = f'{randint(endpt1, endpt2)}x^2'
  b = f'{randint(endpt1, endpt2)}x'
  c = f'{randint(endpt1, endpt2)}'

  if equiv.lower() == 'yes' or equiv.lower() == 'y':
    eq = f'{a} + {b} + {c} = 0'
  elif equiv.lower() == 'no' or equiv.lower() == 'n':
    eq = f'{a} + {b} + {c} = {randint(endpt1, endpt2)}'
  
  return eq

eqNum = int(input('Please enter the number of equations you want: '))
equiv = input('Do you want the equation to be equal to zero?' )

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

pdf = FPDF()
pdf.add_page()
pdf.set_font('comic sans ms', size = 20)

for i in range(len(equations)):
  pdf.cell(200, 10, txt = equations[i - 1], ln = i, align = 'L')

pdf.output('QuadraticEqs.pdf')