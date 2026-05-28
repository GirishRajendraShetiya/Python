# String - An immutable sequence of character (including spaces) objects in single / double quotes.
# """ """ quotes (triple quotes) - Mostly used for documentation purposes.

# Note: By calling the input() function without saving it to a variable, and instructing the user to hit Enter, it can be used to exit a program.

# Length: To calculate the length.

print(len(12))  # TypeError as there is no length for any integer

print(len("12"))  # 2

# Concatenation: To combine more than one string together.

print("Girish" + "Shetiya")  # GirishShetiya
print("Girish " + "Shetiya")  # Girish Shetiya

# Indexing in Python - It starts with 0 from LEFT-RIGHT and -1 from RIGHT-LEFT.

# String indexing with +ve values

language = "Python"
print(language[2])  # t

# String indexing with -ve values

language = "Python"
print(language[-5])  # y

def same_first_and_last_letter(word):
    return word[0] == word[-1]

result = same_first_and_last_letter("Runner")
print(result)  # False

def three_number_sum(num):
    num1 = int(num[0]) + int(num[1]) + int(num[2])
    return num1
result = three_number_sum("123")
print(result)  # 6

# Slicing: To get a part of the string.
# [0:2] => 0 - starting index inclusive, 2 => ending index exclusive

statement = "How are you ?"
print(statement[0:2])  # Ho

statement = "How are you ?"
print(statement[3:150])  #  are you ? (No IndexError in this will get generated)

statement = "How are you ?"
print(statement[2:-6])  # w are

statement = "How are you ?"
print(statement[:-2])  # How are you
print(statement[-12:])  # ow are you ?
print(statement[:])  # How are you ?
print(statement[2:])  # w are you ?
print(statement[2:-5])  # w are

# To validate palindrome
def is_palindrome(str_1):
    if str_1[:] == str_1[::-1]:
        return True
    return False

result = is_palindrome("Level")
print(result)  # False - "L" and "l" are not equal

# Escape characters: \n, \t, \

print("\"To be or not to be\", said by Hamlet")  # "To be or not to be", said by Hamlet

file_1 = r"C:\users\name\templates"  # r is for raw data
print(file_1)  # C:\users\name\templates

# in and not in operator to check inclusion of a substring within a string

browser = "Google"
print('o' in browser)  # True

browser = "Google"
print('O' in browser)  # False - in and not in operator validates case-sensitivity

# Method: A function that acts upon a specific object.

# 1. find - to get the index of the first occurrence of the mentioned character.
# The second number indicates from which position the search should start (the searching will be from 0, same as index).
# If not found, -1 value will be returned.

browser = "Google Chrome"
print(browser.find("o", 4))  # 10

# 2. index - It'll return the index of the first occurrence of the mentioned character.

browser = "Google Chrome"
print(browser.index("o"))  # 1

browser = "Google Chrome"
print(browser.index("Z"))  # ValueError generated

# 3. rfind - While the find method returns the first index where a substring occurs, the rfind method returns the last index where a substring occurs.

txt = "Hello, welcome to my world."
x = txt.rfind("e")
print(x)  # 13

txt = "Hello, welcome to my world."
x = txt.rfind("o")
print(x)  # 22

txt = "Hello, welcome to my world."
x = txt.rfind("l")
print(x)  # 24


