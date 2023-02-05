from sys import exit
import PySimpleGUI as sg

sg.theme('SystemDefaultForReal')
font = ('Jost', 20)

layout = [
    [sg.B('\u274C', key = '-QUIT-')],
    [sg.T('Please enter the number of equations you want: '), sg.InputText()],
    [sg.T('Do you want the equation to be equal to zero (y/n): '), sg.InputText()],
    [sg.T('Please enter the first endpoint for the range (must be positive, not 0): '), sg.InputText()],
    [sg.T('Please enter the second endpoint for the range (should be greater than the first endpoint): '), sg.InputText()],
    [sg.B('\u2705', key = '-SUBMIT-')]
]

wn = sg.Window('AutoAlgebra', layout, font = font)

while True:
    ev, val = wn.read()

    if ev == sg.WIN_CLOSED or ev == '-QUIT-':
        wn.close()
        exit()