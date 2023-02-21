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

# imports functions/classes from modules
from subprocess import call
from platform import system

# runs terminal commands to install packages
if system() == 'Windows':
    call('pip install fpdf', shell = True)
    call('pip install pysimplegui', shell = True)
elif system() == 'Darwin' or system() == 'Linux':
    call('pip3 install fpdf', shell = True)
    call('pip3 install pysimplegui', shell = True)