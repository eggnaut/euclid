from eqGenerator import generateEq

from sys import exit
from fpdf import FPDF
from platform import system
from os.path import abspath
from os import getenv
import PySimpleGUI as sg

sg.theme('SystemDefaultForReal')
font = ('Jost', 20)

layout = [
    [sg.P(), sg.B('Quit  \u274C', key = '-QUIT-')],
    [sg.T('')],
    [sg.T('Please enter the number of equations you want:'), sg.P(), sg.InputText(key = '-NUM-')],
    [sg.T('Do you want the equation to be equal to zero (y/n):'), sg.P(), sg.InputText(key = '-EQUIV-')],
    [sg.T('Please enter the first endpoint for the range (must be positive, not 0):'), sg.P(), sg.InputText(key = '-ENDPT1-')],
    [sg.T('Please enter the second endpoint for the range (should be greater than the first endpoint):'), sg.P(), sg.InputText(key = '-ENDPT2-')],
    [sg.T('')],
    [sg.P(), sg.B('Submit  \u2705', key = '-SUBMIT-')]
]

wn = sg.Window('AutoAlgebra', layout, font = font)

def generatePDF():
    global pdfPath

    pdf = FPDF()
    pdf.add_page()

    try:
        fontPath = abspath('Comic Sans MS.ttf')
        pdf.add_font('csms', '', fontPath, True)
        pdf.set_font('csms', '',  20)
    except:
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
		
    pdf.output(f'{pdfPath}/QuadraticEqs.pdf')

while True:
    ev, val = wn.read()

    if ev == sg.WIN_CLOSED or ev == '-QUIT-':
        wn.close()
        exit()

    if ev == '-SUBMIT-':
        num = int(val['-NUM-'])
        equiv = val['-EQUIV-']
        endpt1 = int(val['-ENDPT1-'])
        endpt2 = int(val['-ENDPT2-'])

        equations = []
        for x in range(num):
            eq = generateEq(endpt1, endpt2, equiv)
            equations.append(eq)

        generatePDF()

        sg.popup_no_buttons(
            f'The PDF was saved in your Downloads folder here:\n\n{pdfPath}/QuadraticEqs.pdf\n\nYou can now click the \'Quit  \u274C\' button.', 
            font = font, 
            title = 'Success', 
            keep_on_top = True, 
            auto_close = True, 
            auto_close_duration = 4
            )
