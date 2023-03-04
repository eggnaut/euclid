#    Automatically generate quadratic equations to study/practice with.
#    Copyright (C) 2023  Dishant B. (eggnaut)
#
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Lesser General Public
#    License as published by the Free Software Foundation; either
#    version 2.1 of the License, or (at your option) any later version.
#
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with this library; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
#    USA

from random import randint

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