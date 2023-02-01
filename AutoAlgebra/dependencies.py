# imports functions/classes from modules
from subprocess import call
from platform import system

# runs terminal commands to install packages
if system() == 'Windows':
    call('pip install fpdf', shell = True)
elif system() == 'Darwin' or system() == 'Linux':
    call('pip3 install fpdf', shell = True)