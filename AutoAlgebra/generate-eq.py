# imports functions/classes from modules
from random import randint
from fpdf import FPDF
from subprocess import call
from platform import system
from os.path import abspath

# function for generating the equation
def generateEq(endpt1: int, endpt2: int, equiv: str):
  a = randint(endpt1, endpt2)
  if a == 1:
    a = ''

  b = randint(endpt1, endpt2)
  if b == 1:
    b = ''

  c = randint(endpt1, endpt2)
  
  symbol1 = '-' if randint(1, 2) == 1 else '+'
  symbol2 = '-' if randint(1, 2) == 1 else '+'
  symbol3 = '-' if randint(1, 2) == 1 else '+'

  p1 = f'{symbol1}{a}x^2'
  p2 = f'{symbol2} {b}x'
  p3 = f'{symbol3} {c}'

  if equiv.lower() == 'yes' or equiv.lower() == 'y':
    eq = f'{p1} {p2} {p3} = 0'
  
  elif equiv.lower() == 'no' or equiv.lower() == 'n':
    d = randint(endpt1, endpt2)

    symbol4 = '-' if randint(1, 2) == 1 else '+'

    p4 = f'{symbol4}{d}'

    eq = f'{p1} {p2} {p3} = {p4}'
  
  return eq

# clears the terminal screen (multiplatform)
if system() == 'Darwin' or system() == 'Linux':
  call('clear', shell = True)
elif system() == 'Windows':
  call('cls', shell = True)
  
# takes initial input for eq gen
eqNum = int(input('Please enter the number of equations you want: '))
equiv = input('Do you want the equation to be equal to zero: ' )

# asks for endpoints until conditions are met
repeat = True
while repeat:
  endpt1 = int(input('Please enter the first endpoint for the range (must be positive, not 0): '))
  endpt2 = int(input('Please enter the second endpoint for the range (should be greater than the first endpoint): '))

  if endpt1 > 0 and endpt1 < endpt2:
    repeat = False

# empty list to store eqs
equations = []

# generates number of equations user asks for
for x in range(eqNum):
  eq = generateEq(endpt1, endpt2, equiv)
  equations.append(eq)

# generates empty PDF to add eqs
pdf = FPDF()
pdf.add_page()

# loads font for use 
path = abspath('Comic Sans MS.ttf')
pdf.add_font('csms', '', path, True)
pdf.set_font('csms', '',  20)

# adds each equation to the PDF
for i in range(len(equations) + 1):
  pdf.cell(200, 10, txt = equations[i - 1], ln = i, align = 'L')
  pdf.cell(200, 10, txt = '', ln = i, align = 'L')

# saves PDF to computer
pdf.output('QuadraticEqs.pdf')