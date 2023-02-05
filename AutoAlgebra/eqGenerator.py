# imports functions/classes from modules
from random import randint
from fpdf import FPDF
from subprocess import call
from platform import system
from os.path import abspath
from os import getenv

# function for generating the equation
def generateEq(endpt1: int, endpt2: int, equiv: str):
	a = randint(endpt1, endpt2)
	if a == 1:
		a = ''

	b = randint(endpt1, endpt2)
	if b == 1:
		b = ''

	c = randint(endpt1, endpt2)

	symbol1 = '-' if randint(1, 2) == 1 else ''
	symbol2 = '-' if randint(1, 2) == 1 else '+'
	symbol3 = '-' if randint(1, 2) == 1 else '+'

	p1 = f'{symbol1}{a}x^2'
	p2 = f'{symbol2} {b}x'
	p3 = f'{symbol3} {c}'

	if equiv.lower() == 'yes' or equiv.lower() == 'y':
		eq = f'{p1} {p2} {p3} = 0'

	elif equiv.lower() == 'no' or equiv.lower() == 'n':
		d = randint(endpt1, endpt2)

		symbol4 = '-' if randint(1, 2) == 1 else ''

		p4 = f'{symbol4}{d}'

		eq = f'{p1} {p2} {p3} = {p4}'
  
	return eq

if __name__ == '__main__':
	# clears the terminal screen (multiplatform)
	if system() == 'Darwin' or system() == 'Linux':
		call('clear', shell = True)
	elif system() == 'Windows':
		call('cls', shell = True)
	
	# takes initial input for eq gen
	eqNum = int(input('\nPlease enter the number of equations you want: '))
	equiv = input('\nDo you want the equation to be equal to zero: ' )

	# asks for endpoints until conditions are met
	repeat = True
	while repeat:
		endpt1 = int(input('\nPlease enter the first endpoint for the range (must be positive, not 0): '))
		endpt2 = int(input('\nPlease enter the second endpoint for the range (should be greater than the first endpoint): '))

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

	# loads font for use, either Comic Sans MS or Arial
	try:
		fontPath = abspath('Comic Sans MS.ttf')
		pdf.add_font('csms', '', fontPath, True)
		pdf.set_font('csms', '',  20)
	except:
		pdf.set_font('Arial', '', 20)

	# adds each equation to the PDF
	for i in range(len(equations) + 1):
		pdf.cell(200, 10, txt = equations[i - 1], ln = i, align = 'L')
		pdf.cell(200, 10, txt = '', ln = i, align = 'L')

	# gets user's downloads folder absolute path
	if system() == 'Darwin' or system() == 'Linux':
		env = getenv('HOME')
		pdfPath = f'{env}/Downloads'
	elif system() == 'Windows':
		env = getenv('USERPROFILE')
		pdfPath = f'{env}\\Downloads'
		
	pdf.output(f'{pdfPath}/QuadraticEqs.pdf')

	# prints a success message
	print(f'\nSuccess! The PDF was saved in your Downloads folder here:')
	print(f'\n{pdfPath}/QuadraticEqs.pdf\n')
