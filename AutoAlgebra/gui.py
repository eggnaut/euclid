from sys import exit
import PySimpleGUI as sg

sg.theme('SystemDefaultForReal')
font = ('Jost', 20)

layout = [
    [sg.P(), sg.B('Cancel  \u274C', key = '-QUIT-')],
    [sg.T('')],
    [sg.T('Please enter the number of equations you want:'), sg.P(), sg.InputText(key = '-NUM-')],
    [sg.T('Do you want the equation to be equal to zero (y/n):'), sg.P(), sg.InputText(key = '-EQUIV-')],
    [sg.T('Please enter the first endpoint for the range (must be positive, not 0):'), sg.P(), sg.InputText(key = '-ENDPT1-')],
    [sg.T('Please enter the second endpoint for the range (should be greater than the first endpoint):'), sg.P(), sg.InputText(key = '-ENDPT2-')],
    [sg.T('')],
    [sg.P(), sg.B('Submit  \u2705', key = '-SUBMIT-')]
]

wn = sg.Window('AutoAlgebra', layout, font = font)

while True:
    ev, val = wn.read()

    if ev == sg.WIN_CLOSED or ev == '-QUIT-':
        wn.close()
        exit()

    if ev == '-SUBMIT-':
        num = val['-NUM-']
        equiv = val['-EQUIV-']
        endpt1 = val['-ENDPT1-']
        endpt2 = val['-ENDPT2-']