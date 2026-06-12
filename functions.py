break# A sequence of one or more steps, a series of instructions, a collection of organized Python code that can be re-used.

# Types - Built-in (print, len, etc.) & Custom (user-defined).

# Inputs - Arguments (they're optional)
# Parameter - Expected argument to a function
# Outputs - Return values

# print(“Hello World !”, sep = “__”, end = “@#”)

# sep, end - parameters
# “__”, “@#” - arguments

# Functions - Declaring and Invoking (to call the function with parenthesis ()), both are important

# Passing a Function: Referencing the function as an object, Function name without parentheses, Code within the function is not executed, Assigning to a variable, passing as
# an argument

# Invoking a Function: Executing the function's code, Function name followed by parentheses (), Code within the function is executed, Performing the function's task and getting
# result

# Parameters (expected argument to a function) given in function are all up to the developer.

def p(text):
    print(text)

p("Hello")  # Hello

# Types of arguments:

# Positional arguments: A positional argument is passed to a function by sequence (the order of expected arguments).
# add(4, 6)

# Keyword arguments: A keyword argument is passed to a function by a keyword identifier.
# add(a = 4, b = 6)

# Note: Positional argument follows Keyword argument, otherwise taken, a SyntaxError appears:
# add(1, 3, c = 3) - Proper
# add(1, b = 3, 3) - Improper

# Return values: After the return statement, anything present will not be executed.

def add(a, b, c):
    return a+b+c

addition = add(1, 3, c = 3)
print(addition)  # 7

# Default arguments: It's a fallback value that will be passed to a parameter if an argument is not passed during function invocation.

# Whichever arguments are optional, should be at the end.
# def add(a, b = 0) - correct
# def add(a = 0, b) - NOT correct

def add(a = 0, b = 0):
    return a+b

print(add())  # 0 (No error got populated as the default value for the parameters is provided)


def string_adder(a = "", b = ""):
    return a + " " + b
    
print(string_adder("Hello", "World"))  # Hello World

# “None” type: As the print expects an input, it returns None along with the output.

def subtract(a, b):
    print(a - b)
    
result = subtract(5, 3)
print(result)

# O/p:
# 2
# None

# Function Annotation: “str” and “int” written below are just for symbolic purpose, it doesn’t guarantee the type of the output.

def word_multiplier(word: str, times: int) -> str:
    return word * times
print(word_multiplier("Hello ", 5))  # Hello Hello Hello Hello Hello 

def word_multiplier(word: str, times: int) -> str:
    return word * times
print(word_multiplier(5, 5))  # 25
