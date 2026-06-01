# Regular Expressions (RegEx) in Python: A way of searching a pattern.

import re
pattern = re.compile("flower")  # compile is used to set a pattern
print(type(pattern))  # <class 're.Pattern'>

print(pattern.search("candy"))  # None (If there is no match found, Python returns None)

result = pattern.search("a yellow flower in the garden")
print(result)  # <re.Match object; span=(9, 15), match='flower'>
# (found at 9th index position till 15th position which is exclusive,
# it's the space after the “flower” word)
print(type(result))  # <class 're.Match'>

print(result.group())  # flower (able to let us know what's the found pattern)

print(result.start())  # 9
print(result.end())  # 15
print(result.span())  # (9, 15 (9th index position is inclusive, but 15 is exclusive)

# THE SEARCH METHOD WILL RETURN THE MATCH OF THE FIRST OCCURRENCE OF THE PATTERN, NOT OTHER THAN THAT.

import re
pattern = re.compile("flower")
# print(type(pattern))

result = pattern.search("a yellow flower in the garden of flower")
print(result)  # <re.Match object; span=(9, 15), match='flower'>
print(type(result))  # <class 're.Match'>

if result:
    print(result.group())  # flower

    print(result.start())  # 9
    print(result.end())  # 15
    print(result.span())  # (9, 15)

# match method: It'll search the pattern only at the start and will return None if not found
# (even if it's present after the starting position).

import re
pattern = re.compile("flower")
result = pattern.match("a flower power")

if result:
    print(result.group())
    print(result.span())

# O/p: No output

import re
pattern = re.compile("flower")
result = pattern.match("flower power")

if result:
    print(result.group())  # flower
    print(result.span())  # (0, 6)

# findall and finditer methods:

# 1. findall - It'll return the exact word match in a list.

import re
pattern = re.compile("flower")

result = "A red flower with a bouquet of yellow flowers is so flowery"
print(pattern.findall(result))  # ['flower', 'flower', 'flower']

# 2. finditer - It'll return the positions of the matched word with span.

import re
pattern = re.compile("flower")

result = "A red flower with a bouquet of yellow flowers is so flowery"
for match in pattern.finditer(result):
    print(match)

# O/p:
# <re.Match object; span=(6, 12), match='flower'>
# <re.Match object; span=(38, 44), match='flower'>
# <re.Match object; span=(52, 58), match='flower'>

# Instead of using the compile of get a pattern, following could be implemented:
# In the parenthesis, the first argument is the pattern and
# second is the string in which the pattern is to be searched.

import re
print(re.search("flower", "A red flower in the garden of flowers"))
print(re.match("flower", "flower in the garden of flowers"))
print(re.findall("flower", "A red flower in the garden of flowers"))

for match in re.finditer("flower", "A red flower in the garden of flowers"):
    print(match)

# O/p:
# <re.Match object; span=(6, 12), match='flower'>
# <re.Match object; span=(0, 6), match='flower'>
# ['flower', 'flower']
# <re.Match object; span=(6, 12), match='flower'>
# <re.Match object; span=(30, 36), match='flower'>

# Raw strings:

print("\tHello\nWorld !")
# 	Hello
# World !
print(r"\tHello\nWorld !")  # \tHello\nWorld !

# Search for digit and non-digit characters:

import re
pattern = re.compile(r"\d")
sentence = "There are 5 red roses, 4 yellow and 10 white ones."
print(pattern.findall(sentence))  # ['5', '4', '1', '0'] (small d is for digits from 0 to 9)

pattern = re.compile(r"\D")
print(pattern.findall(sentence))  # ['T', 'h', 'e', 'r', 'e', ' ', 'a', 'r', 'e', ' ', ' ', 'r', 'e', 'd', ' ', 'r', 'o', 's', 'e', 's', ',', ' ', ' ', 'y', 'e', 'l', 'l', 'o', 'w', ' ', 'a', 'n', 'd', ' ', ' ', 'w', 'h', 'i', 't', 'e', ' ', 'o', 'n', 'e', 's', '.']
# (capital D is for all except digits)

# Search for word and non-word characters:

# \w: any alphanumeric characters (a-z, A-Z, 0-9, _) except the spaces, periods and commas.
# \W: opposite of above.

import re

pattern = re.compile(r"\w")
sentence = "There are 5 red roses, 4 yellow and 10 white ones."
print(pattern.findall(sentence))  # ['T', 'h', 'e', 'r', 'e', 'a', 'r', 'e', '5', 'r', 'e', 'd', 'r', 'o', 's', 'e', 's', '4', 'y', 'e', 'l', 'l', 'o', 'w', 'a', 'n', 'd', '1', '0', 'w', 'h', 'i', 't', 'e', 'o', 'n', 'e', 's']

pattern = re.compile(r"\W")
print(pattern.findall(sentence))  # [' ', ' ', ' ', ' ', ',', ' ', ' ', ' ', ' ', ' ', ' ', '.']

# Search for whitespace and non-whitespace characters:

# \s: for whitepace
# \S: opposite of above

import re

pattern = re.compile(r"\s")
sentence = "There are 5 red roses, 4 yellow and 10 white ones."
print(pattern.findall(sentence))  # [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

pattern = re.compile(r"\S")
print(pattern.findall(sentence))  # ['T', 'h', 'e', 'r', 'e', 'a', 'r', 'e', '5', 'r', 'e', 'd', 'r', 'o', 's', 'e', 's', ',', '4', 'y', 'e', 'l', 'l', 'o', 'w', 'a', 'n', 'd', '1', '0', 'w', 'h', 'i', 't', 'e', 'o', 'n', 'e', 's', '.']

# Search for word boundaries (start / end of a word): They're case sensitive.

# \b: if entered before any character, it'll return the word / words having that character
# at the start and if entered after, it’ll return the word / words having that character at the end.

import re
pattern = re.compile(r"\bs")
sentence = "There are 5 red roses, 4 yellow and 10 white ones."
print(pattern.findall(sentence))  # [] (No output as there is no word starting with the letter 's')

import re
pattern = re.compile(r"\bA")
sentence = "There Are 5 red roses, 4 yellow and 10 white ones."
print(pattern.findall(sentence))  # ['A']

import re
pattern = re.compile(r"\bA")
sentence = "There Are 5 red roses, 4 yellow And 10 white ones."
print(pattern.findall(sentence))  # ['A', 'A']

import re
pattern = re.compile(r"s\b")
sentence = "There Are 5 red roses, 4 yellow and 10 white ones."
print(pattern.findall(sentence))  # ['s', 's']

# \B: opposite of \b. It’ll return the word / words that are not starting with the specified character.

import re
pattern = re.compile(r"\Bt")
sentence = "There Are 5 red roses, 4 yellow and 10 white ones."
print(pattern.findall(sentence))  # ['t']

import re
pattern = re.compile(r"T\B")
sentence = "There Are 5 red roses, 4 yellow and 10 white ones."
print(pattern.findall(sentence))  # ['T']

# Metacharacters in RegEx:

# 1. The period / dot - .
# It means every character except the new line character (\n).
# If written as '\.', it'll return only the dot.

import re
pattern = re.compile(r"\.")
sentence = "There Are 5 red roses, 4 yellow and 10 white ones."
print(pattern.findall(sentence))  # ['.']

# 2. The square brackets - 

import re
pattern = re.compile(r"[aro]")
sentence = "There Are 5 red roses, 4 yellow and 10 white ones."
print(pattern.findall(sentence))  # ['r', 'r', 'r', 'r', 'o', 'o', 'a', 'o']
# (It'll search all the references of a, r and o separately in the string)

import re
pattern = re.compile(r"[^aro]")
sentence = "There Are 5 red roses, 4 yellow and 10 white ones."
print(pattern.findall(sentence))  # ['T', 'h', 'e', 'e', ' ', 'A', 'e', ' ', '5', ' ', 'e', 'd', ' ', 's', 'e', 's', ',', ' ', '4', ' ', 'y', 'e', 'l', 'l', 'w', ' ', 'n', 'd', ' ', '1', '0', ' ', 'w', 'h', 'i', 't', 'e', ' ', 'n', 'e', 's', '.']
# (It'll search all the references except a, r and o separately in the string)

import re
pattern = re.compile(r"[a-m]")
sentence = "There Are 5 red roses, 4 yellow and 10 white ones."
print(pattern.findall(sentence))  # ['h', 'e', 'e', 'e', 'e', 'd', 'e', 'e', 'l', 'l', 'a', 'd', 'h', 'i', 'e', 'e']
# (All characters between a and m with both inclusive)

import re
pattern = re.compile(r"[a-m A-T]")
sentence = "There Are 5 red roses, 4 yellow and 10 white ones."
print(pattern.findall(sentence))  # ['T', 'h', 'e', 'e', ' ', 'A', 'e', ' ', ' ', 'e', 'd', ' ', 'e', ' ', ' ', 'e', 'l', 'l', ' ', 'a', 'd', ' ', ' ', 'h', 'i', 'e', ' ', 'e']
# ('T' is also included)

# 3. The curly brackets - 

import re
pattern = re.compile(r"l{2}")
sentence = "There Are 5 red roses, 4 yellow ll and 10 white ones."
print(pattern.findall(sentence))  # ['ll', ‘ll’]
# (Jitne bhi 2 'l' saath mein hai, woh return honge)

import re
pattern = re.compile(r"l{1}")
sentence = "There Are 5 red roses, 4 yellow ll and 10 white ones."
print(pattern.findall(sentence))  # ['l', 'l', 'l', 'l']
# (Jitne bhi 1 'l' saath mein hai, woh return honge)

import re
pattern = re.compile(r"l{1,}")
sentence = "There Are 5 red roses, l 4 yellow ll lll and 10 white ones."
print(pattern.findall(sentence))  # ['l', 'll', 'll', 'lll']
# (1 'l' aur phir baaki sab bhi)

import re
pattern = re.compile(r"l{1,2}")
sentence = "There Are 5 red roses, l 4 yellow ll lll and 10 white ones."
print(pattern.findall(sentence))  # ['l', 'll', 'll', 'll', 'l']
# (1 'l' wale, 2 “l” wale)

# To extract only the numbers:

import re
pattern = re.compile(r"\d{3}-\d{3}-\d{4}")
sentence = "I can be reached at 555-123-4567 and I'd appreciate a call tomorrow. Again, my number is 555-123-4567. Thank you.."
print(pattern.findall(sentence))  # ['555-123-4567', '555-123-4567']

# With a dash or space between the numbers:

import re
pattern = re.compile(r"\d{3} \d{3} \d{4}")  # pattern = re.compile(r"\d{3}\s\d{3}\s\d{4}") could also be used
sentence = "I can be reached at 555 123 4567 and I'd appreciate a call tomorrow. Again, my number is 555 123 4567. Thank you.."
print(pattern.findall(sentence))  # ['555 123 4567', '555 123 4567']

# To extract the numbers with any number of spaces between them

import re
pattern = re.compile(r"\d{3}\s{1,}\d{3}\s{1,}\d{4}")
sentence = "I can be reached at 555    123     4567 and I'd appreciate a call tomorrow. Again, my number is 555   123    4567. Thank you.."
print(pattern.findall(sentence))  # ['555    123     4567', '555   123    4567']

# + symbol: To be used instead of the curly braces

import re
pattern = re.compile(r"\d+\s+\d+\s+\d+")
sentence = "I can be reached at 555    123     4567 and I'd appreciate a call tomorrow. Again, my number is 555   123    4567. Thank you.."
print(pattern.findall(sentence))  # ['555    123     4567', '555   123    4567']

import re
pattern = re.compile(r"\d+(\s+|-)\d+(\s+|-)\d+")
sentence = "I can be reached at 555    123     4567 and I'd appreciate a call tomorrow. Again, my number is 555-123-4567. Thank you.."
print(pattern.findall(sentence))  # ['555    123     4567', '555-123-4567']

# '192.168.1.1 - - [23/May/2026:16:45:01] "GET /home HTTP/1.1" 200 4523'
# For IP address(192.168.1.1) - \d{1,}\.\d{1,}\.\d{1,}\.\d{1,}
# For status code(200) - \s\d{3}\s

# The quick brown fox jumps over the laziness dog.
# To extract the 5 letter words: 
# [a-zA-Z]{5} O/p: quick, brown, jumps, lazin (it's NOT correct as it has picked 5 letters from the laziness word)
# Correct one - \b[a-zA-Z]{5}\b O/p: quick, brown, jumps (Due to \b at the start and end, it picks only those words having 5 letters)
