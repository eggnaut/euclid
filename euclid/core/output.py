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

from fpdf import FPDF
from os import getenv
from platform import system

# function to generate the PDF with equations
def generatePDF(equations):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font('Arial', '', 20)

    for i in range(len(equations) + 1):
        pdf.cell(200, 10, txt = equations[i - 1], ln = i, align = 'L')
        pdf.cell(200, 10, txt = '', ln = i, align = 'L')

    if system() == 'Darwin' or system() == 'Linux':
        env = getenv('HOME')
        pdfPath = f'{env}/Downloads'
    elif system() == 'Windows':
        env = getenv('USERPROFILE')
        pdfPath = f'{env}\\Downloads'
	
    if system() == 'Darwin' or system() == 'Linux':
        pdf.output(f'{pdfPath}/QuadraticEqs.pdf')
    elif system() == 'Windows':
        pdf.output(f'{pdfPath}\\QuadraticEqs.pdf')