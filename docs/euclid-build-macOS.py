from pkgutil import find_loader
from subprocess import call
from platform import system

if find_loader('pyinstaller') is None:
    if system() == 'Windows':
        call('pip install pyinstaller', shell = True)
    elif system() == 'Darwin' or system() == 'Linux':
        call('pip3 install pyinstaller', shell = True)

import PyInstaller.__main__

PyInstaller.__main__.run([
    '../euclid/gui.py',
    '--onefile',
    '--noconsole',
    '--disable-windowed-traceback',
    '--clean',
    '-ilogo.png'
])