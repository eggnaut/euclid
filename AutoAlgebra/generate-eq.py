from random import randint
from fpdf import FPDF
from subprocess import call
from platform import system
from os.path import abspath

def generateEq(endpt1: int, endpt2: int, equiv: str):
  a = f'{randint(endpt1, endpt2)}x^2'
  b = f'{randint(endpt1, endpt2)}x'
  c = f'{randint(endpt1, endpt2)}'
  
  symbol1 = '-' if randint(1, 2) == 1 else '+'
  symbol2 = '-' if randint(1, 2) == 1 else '+'

  if equiv.lower() == 'yes' or equiv.lower() == 'y':
    eq = f'{a} {symbol1} {b} {symbol2} {c} = 0'
  elif equiv.lower() == 'no' or equiv.lower() == 'n':
    symbol3 = '-' if randint(1, 2) == 1 else '+'
    eq = f'{a} {symbol1} {b} {symbol2} {c} = {symbol3}{randint(endpt1, endpt2)}'
  
  return eq

if system() == 'Darwin':
  call('clear', shell = True)
elif system() == 'Windows':
  call('cls', shell = True)
  
eqNum = int(input('Please enter the number of equations you want: '))
equiv = input('Do you want the equation to be equal to zero: ' )

repeat = True

while repeat:
  endpt1 = int(input('Please enter the first endpoint for the range (must be positive, not 0): '))
  endpt2 = int(input('Please enter the second endpoint for the range (should be greater than the first endpoint): '))

  if endpt1 > 0 and endpt1 < endpt2:
    repeat = False

equations = []

for x in range(eqNum):
  eq = generateEq(endpt1, endpt2, equiv)
  equations.append(eq)

pdf = FPDF()
pdf.add_page()

path = abspath('Comic Sans MS.ttf')
pdf.add_font('csms', '', path, True)
pdf.set_font('csms', '',  20)

for i in range(len(equations) + 1):
  pdf.cell(200, 10, txt = equations[i - 1], ln = i, align = 'L')
  pdf.cell(200, 10, txt = '', ln = i, align = 'L')

pdf.output('QuadraticEqs.pdf')