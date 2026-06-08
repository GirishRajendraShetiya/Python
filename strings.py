# String - An immutable sequence of character (including spaces) objects in single / double quotes.
# """ """ quotes (triple quotes) - Mostly used for documentation purposes.

# Note: By calling the input() function without saving it to a variable, and instructing the user to hit Enter, it can be used to exit a program.

# Encoding / Decoding in strings
string_1 = "Hello Special World !"
encoded_string = string_1.encode("utf-8")

print(string_1)  # Hello Special World !
print(encoded_string)  # b'Hello Special World !'

decoded_string = encoded_string.decode("utf-8")
print(decoded_string)  # Hello Special World !

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
# [::-1] => To reverse a string

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

# startswith method: To check whether a mentioned substring is present at the first in the string or not.
# It’s case sensitive. Returns True / False.

browser = "Google Chrome"
print(browser.startswith("Gg"))  # False

browser = "Google Chrome"
print(browser.startswith("G"))  # True

# endswith method: To check whether a mentioned substring is present at the end in the string or not.
# It’s case sensitive. Returns True / False.

browser = "Google Chrome"
print(browser.endswith("mE"))  # False

browser = "Google Chrome"
print(browser.endswith("rome"))  # True

# count method: To get the occurrence of a character in a string.
# It’s case sensitive. If not found, it returns “0”.

browser = "Google Chrome"
print(browser.count("g"))  # 1

# upper(), lower(), capitalize(), title(), swapcase()

word = "Hello World"
print(word.upper())  # HELLO WORLD
print(word.lower())  # hello world
print(word.capitalize())  # Hello world
print(word.title())  # Hello World
print(word.swapcase())  # hELLO wORLD

# isupper(), islower(), istitle()
# isalpha(), isnumeric(), isalnum(), isspace()

word = "Hello World"
print(word.isupper())  # False
print(word.islower())  # False
print(word.istitle())  # True

word = "Hello World"
print(word.isalpha())  # False - A space is included between the 2 words

word = "HelloWorld"
print(word.isalpha())  # True - No space between the words

word = "123"
print(word.isnumeric())  # True

word = "Hello123"
print(word.isalnum())  # True - No space, hence True

word = "   "
print(word.isspace())  # True

# rstrip(), lstrip(), strip() - Default removal is a space character. Every time at the beginning and end.

browser = "www.python.org"

# (Will check for “w”, “o”, “r”, “g”, “.”)
print(browser.strip("worg."))  # python
print(browser.rstrip("worg."))  # www.python
print(browser.lstrip("worg."))  # python.org

# replace() - In place of a single character, two or more characters can be replaced.

browser = "Google Chrome"
print(browser.replace("o", "d"))  # Gddgle Chrdme

def fancy_cleanup(word):
    word = word.strip().replace("g", "z").replace(" ", "!")
    return word

print(fancy_cleanup("       geronimo crikey  "))  # zeronimo!crikey

# format method:

mad_libs = "{} laughed at the {} {}"
print(mad_libs.format("Girish", "funny", "guy"))  # Girish laughed at the funny guy

mad_libs = "{0} laughed at the {1} {2}"
print(mad_libs.format("Girish", "funny", "guy"))  # Girish laughed at the funny guy

mad_libs = "{name} laughed at the {adjective} {noun}."

print(mad_libs.format(name ="Girish", adjective = "funny", noun = "guy"))  # Girish laughed at the funny guy
print(mad_libs. format(name = "Jennifer", adjective = "funny", noun = "guy") )  # Jennifer laughed at the funny guy

mad_libs = "{name} laughed at the {adjective} {noun}."

name = input("Enter your name: ")
adjective = input("Enter the adjective: ")
noun = input("Enter the noun: ")

print(mad_libs.format(name = name, adjective = adjective, noun = noun))

# O/p:
# Enter your name: Girish
# Enter the adjective: cute
# Enter the noun: girl
# Girish laughed at the cute girl.

# If the number of arguments passed are less than the index, then an IndexError gets populated.

# Traceback (most recent call last):
#   File "main.py", line 2, in <module>
#     print(mad_libs.format("Girish", "funny"))
# IndexError: Replacement index 2 out of range for positional args tuple


