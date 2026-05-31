# It's a code that handles errors.

# Exception: An error that occurs at the time of program execution.
# Traceback - Report of exception that was raised.
# A traceback is a report or summary or analysis of the exception that was raised.
# It includes the file name, the line number, the type of error, and more.

# try-except block: To try a piece of code, and if it's going to generate an error, it goes to the except block.

def num_division(num_1):
    try:
        return 5 / num_1
    except:
        hello = "Are you out of your mind !"
        return hello
        
print(num_division(0))  # Are you out of your mind !

def num_division(num_1):
    try:
        return 5 / num_1
    except ZeroDivisionError:
        return "Can't divide by Zero"
    except TypeError:
        return "Can't divide by string"

print(num_division(0))  # Can't divide by Zero
print(num_division("Hello"))  # Can't divide by string

# raise keyword: To raise an exception separately.

def num_addition(num_1, num_2):
    try:
        if num_1 <= 0 or num_2 <= 0:
            raise ValueError("One or both the entered number/s is/are less than or equal to zero")
        return num_1 + num_2
    except ValueError as e:
        return f"Caught an error: {e}"

print(num_addition(-1, 2))  # Caught an error: One or both the entered number/s is/are less than or equal to zero

# User defined exceptions:

class NegativeNumberException(Exception):
    """One or more numbers are negative"""
    pass

def add_numbers(num_1, num_2):
    try:
        if num_1 <= 0 or num_2 <= 0:
            raise NegativeNumberException        
        return num_1 + num_2

    except NegativeNumberException:
        return "Are you out of your mind !"
        
print(add_numbers(-1, 2))  # Are you out of your mind !

# Exception Inheritance Hierarchies:

class Mistake(Exception):
    pass

class SuperMistake(Mistake):
    pass

class SillyMistake(Mistake):
    pass

try:
    raise SuperMistake("Got an error")
except SuperMistake as e:
    print(f"Caught: {e}")  # Caught: Got an error

class Mistake(Exception):
    pass

class SuperMistake(Mistake):
    pass

class SillyMistake(Mistake):
    pass

try:
    raise SuperMistake("Got an error")
except Mistake as e:
    print(f"Caught: {e}")  # Caught: Got an error

class Mistake(Exception):
    pass

class SuperMistake(Mistake):
    pass

class SillyMistake(Mistake):
    pass

try:
    raise SuperMistake("Got an error")
except SillyMistake as e:
    print(f"Caught: {e}")  # SuperMistake: Got an error

class Problem(Exception):
  pass
 
class BusinessProblem(Problem):
  pass
 
class CodingProblem(Problem):
  pass
 
def monday_morning():
  try:
    raise Problem
  except CodingProblem:
    print("Will this print?")

monday_morning()  # An error will be populated.

# The else and finally blocks: else block runs after the try block, only if the try block has NO ERROR.
# finally block always runs at the last.

x = 10

try:
    print(x + 15)
except NameError:
    print("Some variables not defined")
    
else:
    print("This will print if there is no error in the try block")
    
finally:
    print("Regardless of anything, this'll print !")

# O/p:
# 25
# This will print if there is no error in the try block
# Regardless of anything, this'll print !

# x = 10

try:
    print(x + 15)
except NameError:
    print("Some variables not defined")
    
else:
    print("This will print if there is no error in the try block")
    
finally:
    print("Regardless of anything, this'll print !")

# O/p:
# Some variables not defined
# Regardless of anything, this'll print !
