# Higher order function: A function that either accepts a function as an argument or returns a function as a return value.

def add(a, b):
    return a + b
    
def subtract(a, b):
    return a - b
    
def calculate(func, a, b):
    return func(a, b)
    
print(calculate(add, 5, 6))  # 11

def sample(a):
    return a

def output_func(another_func, string_value):
    return another_func(string_value)

print(output_func(sample, "A"))  # A

def sample():
    print("A")

def main_func(another_func):
    another_func()
    another_func()
    another_func()

main_func(sample)

# O/p:
# A
# A
# A

# If no parenthesis are given for the function, no output will be generated.
def sample():
    print("A")

def main_func(another_func):
    another_func
    another_func
    another_func

main_func(sample)  # No output

def be_nice(good_1):
    def inner():
        print("You're a great person !")
        good_1()
        print("See you !!!")
        
    return inner

@be_nice
def other_func():
    print("Wonderful !")
    
other_func(be_nice)

# O/p:
# You're a great person !
# Wonderful !
# See you !!!

# Nested functions: The functions which are encapsulated within a function, can’t be called from outside that function.

# 1km = 1000m
# 1m = 100cm

def convert_km_to_cm(km_1):
    def convert_km_to_m(km_1):
        print(f"Converting {km_1} km to meters")
        return km_1 * 1000
    
    def convert_m_to_cm(m_1):
        print(f"Converting {m_1} meters to cm")
        return m_1 * 100
    
    kilo_meter = convert_km_to_m(km_1)
    meter = convert_m_to_cm(kilo_meter)
    return meter

print(convert_km_to_cm(1.3))

# O/p:
# Converting 1.3 km to meters
# Converting 1300.0 meters to cm
# 130000.0

# Functions as return values:

def calculator(operation):
    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b

    if operation == "add":
        return add
    elif operation == "subtract":
        return subtract

print(calculator("add")(2, 5))  # 7

def square(num_1):
    return num_1 ** 2

def cube(num_1):
    return num_1 ** 3

operations = [square, cube]

for i in operations:
    print(i(3))

# O/p:
# 9
# 27

def outer():
    def inner():
        return 5
    
    return inner

print(outer()())  # 5

def outer():
    def inner():
        return 5
    
    return inner

print(outer())  # <function outer.<locals>.inner at 0x7f15eb054c10>

def outer():
    def inner():
        return 5
    
    return inner

print(outer)  # <function outer at 0x7f34e67eab80>

def be_nice(func):
    def inner():
        print("Hello")
        func()
        print("World !")
    return inner
    
def another_func():
    print("Cruel")

be_nice(another_func)  # No output (the inner function is not invoked, but passed)

def be_nice(func):
    def inner():
        print("Hello")
        func()
        print("World !")
    return inner
    
def another_func():
    print("Cruel")

print(be_nice(another_func))  # <function be_nice.<locals>.inner at 0x77766fb47a60> (It’ll print the location of the inner function)

def be_nice(func):
    def inner():
        print("Hello")
        func()
        print("World !")
    return inner
    
def another_func():
    print("Cruel")

print(be_nice(another_func)())

# O/p:
# Hello
# Cruel
# World !
# None (Due to the extra braces in the print statement, the return statement will give None)

def be_nice(func_1):
    def inner():
        print("Hello !")
        func_1()
        print("Bye !")
        
    return inner()

def lets_dance():
    print("Let's break the floor !!!")

be_nice(lets_dance)

# O/p:
# Hello !
# Let's break the floor !!!
# Bye ! (Due to the braces at the return statement and no print statement, the output doesn’t have None)

# PRINT STATEMENT BHOOKA HAI, JAB BHI AAYEGA, KUCH NA KUCH LEGA, AUR KUCH NA MILE, TOH NONE RETURN KAREGA.

# Short-hand to decorator: @

def be_nice(func_1):
    def inner():
        print("Hello !")
        func_1()
        print("Bye !")
        
    return inner

@be_nice
def lets_dance():
    print("Let's break the floor !!!")

lets_dance()

# O/p:
# Hello !
# Let's break the floor !!!
# Bye !

# *args: Tuples representing all sequential arguments.
# **kwargs: Dictionary (key-value pair) with keyword arguments

def be_nice(func_1):
    def inner(*args, **kwargs):
        print("Hello !")
        print(args)
        print(kwargs)
        # func_1()
        print("Bye !")
        
    return inner

@be_nice
def lets_dance(name):
    print(f"Let's break the floor {name} !!!")

lets_dance(name = "Soniya")

# O/p:
# Hello !
# ()
# {'name': 'Soniya'}
# Bye !

def be_nice(func_1):
    def inner(*args, **kwargs):
        print("Hello !")
        func_1(*args, **kwargs)
        print("Bye !")
        
    return inner

@be_nice
def lets_dance(name):
    print(f"Let's break the floor {name} !!!")

lets_dance(name = "Soniya")

# O/p:
# Hello !
# Let's break the floor Soniya !!!
# Bye !

def be_nice(func_1):
    def inner(*args, **kwargs):
        print("Hello !")
        func_1()
        print("Bye !")
        
    return inner

@be_nice
def lets_dance(name):
    print(f"Let's break the floor {name} !!!")

lets_dance(name = "Soniya")  # TypeError will be populated.

# If the values are passed to the inner function of the decorator (using *args / **kwargs),
# but not to the function, a TypeError will be populated.

# Returned values from decorated functions:
def be_nice(func_1):
    def inner(*args, **kwargs):
        print("Hello !")
        func_1(*args, **kwargs)
        print("Bye !")
    return inner

@be_nice
def lets_dance(a, b):
    return a + b

print(lets_dance(2, b = 5))

# O/p:
# Hello !
# Bye !
# None  (The func_1 invoking gets completed prior to the Bye printing, and hence when lets_dance is called,
# it’s returning the value as None)

def be_nice(func_1):
    def inner(*args, **kwargs):
        print("Hello !")
        result = func_1(*args, **kwargs)
        print("Bye !")
        return result
    return inner


@be_nice
def lets_dance(a, b):
    return a + b

print(lets_dance(2, b = 5))

# O/p:
# Hello !
# Bye !
# 7

def be_nice(func_1):
    def inner(*args, **kwargs):
        print("Hello !")
        func_1(*args, **kwargs)
        print("Bye !")
    return inner

@be_nice
def lets_dance(a, b):
    print(a + b)

lets_dance(2, b = 5)

# O/p:
# Hello !
# 7
# Bye !

# functools.wrap decorator: To keep the original documentation intact.

import functools
def be_nice(func_1):
    @functools.wraps(func_1)
    def inner(*args, **kwargs):
        print("Hello !")
        result = func_1(*args, **kwargs)
        print("Bye !")
        return result
    return inner

@be_nice
def lets_dance(a, b):
    "Let's Dance"
    return a + b

help(lets_dance)

# O/p:
# Help on function lets_dance in module __main__:

# lets_dance(a, b)
#     Let's Dance

import functools
def uppercase(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        fn(*args, **kwargs).upper()
    return wrapper
@uppercase
def concatenate(a, b):
    """Combines two strings together"""
    return a + b
print(concatenate("pyt", "hon"))  # None - The output of fn(*args, **kwargs).upper() is not saved into any variable and also not returned

import functools
def uppercase(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs).upper()        
        return result
    return wrapper

@uppercase
def concatenate(a, b):
    """Combines two strings together"""
    return a + b

print(concatenate("pyt", "hon"))  # PYTHON
