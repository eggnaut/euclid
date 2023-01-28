from subprocess import call
from platform import system

if system() == 'Windows':
    call('pip install fpdf', shell = True)
elif system() == 'Darwin' or system() == 'Linux':
    call('pip3 install fpdf', shell = True)