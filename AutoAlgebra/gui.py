from eqGenerator import generateEq

from sys import exit
from fpdf import FPDF
from platform import system
from os.path import abspath
from os import getenv
from functools import partial
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
	
    if system() == 'Darwin' or system() == 'Linux':
        pdf.output(f'{pdfPath}/QuadraticEqs.pdf')
    elif system() == 'Windows':
        pdf.output(f'{pdfPath}\\QuadraticEqs.pdf')

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

        if not (endpt1 > 0 and endpt2 > endpt1):
            sg.popup_no_buttons(
                f'Please check that the first endpoint is greater than 0.\n\nPlease check that the second endpoint is greater than the first endpoint.',
                font = font,
                title = 'Error \u274C',
                keep_on_top = True,
                auto_close = True,
                auto_close_duration = 4
            )
        elif num <= 0:
            sg.popup_no_buttons(
                f'Please check that the number of equations requested is greater than 0.',
                font = font,
                title = 'Error \u274C',
                keep_on_top = True,
                auto_close = True,
                auto_close_duration = 4
            )
        elif not (equiv.lower() == 'y' or equiv.lower() == 'yes' or equiv.lower() == 'n' or equiv.lower() == 'no'):
            sg.popup_no_buttons(
                f'Please make sure you entered \'y\' or \'n\' for the second question:\n\n\'Do you want the equation to be equal to zero (y/n)\'',
                font = font,
                title = 'Error \u274C',
                keep_on_top = True,
                auto_close = True,
                auto_close_duration = 4
            )
        else:
            equations = []
            for x in range(num):
                eq = generateEq(endpt1, endpt2, equiv)
                equations.append(eq)

            generatePDF()

            sg.popup_no_buttons(
                f'The PDF was saved in your Downloads folder here:\n\n{pdfPath}/QuadraticEqs.pdf\n\nYou can now quit the app.', 
                font = font, 
                title = 'Success \u2705', 
                keep_on_top = True, 
                auto_close = True, 
                auto_close_duration = 4
                )
