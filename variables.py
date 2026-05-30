# Variables - Name given / refers to an object.
# A variable can store different data types at the same time.

# Variable naming rules

# 1. No spaces are allowed.
# 2. The first character must be a letter (lowercase or uppercase) or an underscore.
# 3. Only letters, numbers and underscores are permitted after the first character.
# 4. Variable names are case-sensitive. ​name​ and ​Name​ are two distinct, separate variables.
# 5. Variable names should describe the data that they are referencing.
# 6. Use underscores to separate multiple words. This is called snake case style because the text resembles a snake. Example: my_favorite_flavor_of_ice_cream

# Variable: Snake case (variable_example)
# Function: functionExample
# Class: Camel case (ClassExample)

# Code optimization is also known as code re-factoring.

# Multiple variable assignment: 2 variables having the same value, but not pointing to each other.

a = b = 4
b = 10
print(a)  # 4
print(b)  # 10

# Global vs Local variables: Both have different scopes.

# Shadow variable: A local variable sharing the name of a global variable.

# Constants: Defined by capital letters.

# LEGB (Local Enclosing functions Global Built-in) rule: How Python searches for any variable.

def outer():
    x = 10
    
    def inner():
        x = 5
        return x
        
    return inner()

print(outer())  # 5

def outer():
    x = 10
    
    def inner():
        return x
        
    return inner()

print(outer())  # 10

x = 15

def outer():

    def inner():
        return x
        
    return inner()

print(outer())  # 15

def outer():

    def inner():
        return len
        
    return inner()

print(outer()("Python"))  # 6

# Closure: A closure describes a programming pattern where a scope retains access to an enclosing scope's name or data.
# That data will persist even if the external scope has finished executing;
# an example is a nested function that is returned from another that holds access to a variable value.

def outer():
    greet = "Hello"
    
    def inner():
        return greet
    
    return inner()
    
print(outer())  # Hello

def outer():
    greet = "Hello"
    
    def inner():
        return greet
    
    return inner()
    
the_func = outer()
print(the_func)  # Hello

# Even after the scope of the outer() function is till the_func line only, it’ll print the value of the_func as 'Hello'.

def outer():
    greet = "Hello"
    
    def inner():
        return greet
    
    return inner
    
print(outer()())  # Hello

def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

def calculate(func, a, b):
    func(a, b)
print(calculate(multiply, 10, 5))  # Error: The return value of invocation of func is not being returned out of the calculate function.

def a():
    def b():
        def c():
            return val
        return c()
    return b()

print(a())  # NameError
val = "Hello"

def a():
    def b():
        def c():
            return val
        return c()
    return b()

val = "Hello"
print(a())  # Hello


