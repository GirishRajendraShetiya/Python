# calculator.py

creator = "Girish"
PI = 3.14

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
    
def multiply(a, b):
    return a * b
    
def divide(a, b):
    return a / b

# main.py

import calculator
print(calculator.creator)  # Girish
print(calculator.add(2, 7))  # 9

# Python Standard Library: There are around 250 and more modules in Python.

import string

print(string.ascii_letters)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)  # 0123456789

import math

print(math.pi)  # 3.141592653589793
print(math.ceil(3.1))  # 4
print(math.floor(7.9))  # 7

# Dunder name(__name__):
# __name__ is a special built-in variable in Python that holds the name of the current module.
# It is automatically set by the Python interpreter and is hidden / private for every module.
# When a Python file is executed directly, the value of __name__ is set to "__main__".
# This indicates that the script is the primary program being run.

import math
print(math.__name__)  # math

import math
print(__name__)  # __main__

# If a file is being run as a script, then dunder name will evaluate to dunder main.
# But if a file is being used as a module, as calculator is being used here, we’re importing it, it’s not the primary launching pad.

# If something is being used as a module, then its dunder name printing in that file will evaluate to the name of the module.
# So because we are running playground.py, this is when this runs in. This file is going to evaluate the calculator.

calculator.py
creator = "Girish"
PI = 3.14

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
    
def multiply(a, b):
    return a * b
    
def divide(a, b):
    return a / b

print(__name__)

# main.py
import math
import calculator  # calculator

creator = "Girish"
PI = 3.14

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
    
def multiply(a, b):
    return a * b
    
def divide(a, b):
    return a / b

if __name__ == "__main__":
    print("Hello")  # Hello
    print(subtract(3, 5))  # -2

# Alias with the as keyword:
import calculator as calc
import datetime as dt

# Import specific attributes with the from syntax:
# from <module_name> import <attribute_name>

from calculator import add, subtract
print(add(2, 4))  # 6

# Import all attributes with * syntax:
from calculator import *

# If in the module, a variable is written with an underscore at the start, it can’t be exported to another program.
# import keyword can be used to include a module, as well as a package (a directory of modules).

# __init_.py file
# If Python finds a __init__.py in a folder, so just by importing the respective package, it’ll automatically run the file.

# Also, without importing, it'll not run automatically. It converts a directory into a package.
# Eg: from feature.subfeature.calculator import subtract

# It'll first run the __init__.py file of the feature module, then of the subfeature module and then the further code will execute.

# In the __init__.py file, we can include the functions of another module which is present in the same directory.
# Eg: In the __init__.py file of subfeature directory having a module named calculator
# from .calculator import subtract, add

# A script refers to a Python file that is executed directly.
# A module is a Python file that is imported by another file (such as a script).

# Ways to import another module into the current one
# import another_module
# another_module.package()

# from another_module import package_1
# package_1()

# from another_module import package_1 as p1
# p1
