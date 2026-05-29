# An ordered and mutable data structure that can store different type of objects (int, float, string, dictionary, etc.) in a single list.

# Create an empty list and assign it to the variable "empty".
empty = []

# Create an empty list and assign it to the variable "c".
c = []

# Create a list with a single Boolean — True — and assign it to the variable "active".
active = [True]

# Create a list with 5 integers of your choice and assign it to the variable "favorite_numbers".
favorite_numbers = [1, 2, 3, 4, 5]

# Create a list with 3 strings  — "red", "green", "blue" — and assign it to the variable "colors".
colors = ["red", "green", "blue"]

# Declare an is_long function that accepts a single list as an argument
# It should return True if the list has more than 5 elements, and False otherwise

def is_long(list_input):
    if len(list_input) > 5:
        return True
    else:
        return False

print(is_long("colors"))  # True

# in and not in Lists:
test_scores = [99.0, 102.0, 113.0]
print(99.0 in test_scores)  # True
print(99 in test_scores)  # True

# Above, Python is smart enough to understand that 99.0 and 99 are equivalent in Maths

print([5, 4, 3] not in [[5, 4, 3], 4, 3])  # False - [5, 4, 3] is present in the list as a whole

prime_minister = ["Manmohan", "Modi", "Nehru", "Vajpayee", "Shastri", "Rao"]
print(prime_minister[3][2])  # j

# Slicing in lists: It starts from 0 and the second index provided is exclusive.

prime_minister = ["Manmohan", "Modi", "Nehru", "Vajpayee", "Shastri", "Rao"]
print(prime_minister[1:4])  # ['Modi', 'Nehru', 'Vajpayee']

# With -ve interval of 2
prime_minister = ["Manmohan", "Modi", "Nehru", "Vajpayee", "Shastri", "Rao"]
print(prime_minister[::-2])  # ['Rao', 'Vajpayee', 'Modi']

# With +ve interval of 2
prime_minister = ["Manmohan", "Modi", "Nehru", "Vajpayee", "Shastri", "Rao"]
print(prime_minister[::2])  # ['Manmohan', 'Nehru', 'Shastri']

def nested_extraction(list_1, index_pos):
    return list_1[index_pos][index_pos]
    
nl = [[3, 4, 5], [7, 8, 9], [10, 11, 12]]
print(nested_extraction(nl, 0))  # 3

def beginning_and_end(list_1):
    if list_1[0] == list_1[-1]:
        return True
    else:
        return False

print(beginning_and_end([1, 2, 3, 1]))  # True

def long_word_in_collection(list_1, string_1):
    if string_1 in list_1 and len(string_1) > 4:
        return True
    else:
        return False

words = ["cat", "dog", "rhino"]
print(long_word_in_collection(words, "rhino"))  # True

def split_in_two(list_1, number):
    if number % 2 == 0:
        return list_1[2:]
    else:
        return list_1[0:2]

list_1 = [1, 2, 3, 4, 5]
print(split_in_two(list_1, 4))  # [3, 4, 5]

def sum_of_lengths(list_1):
    sum_1 = 0
    for s in list_1:
        sum_1 += len(s)
    return sum_1

print(sum_of_lengths(["Hello", "Bob"]))  # 8

def product(num_1):
    prod = 1
    for num in num_1:
        prod *= num
    return prod
    
print(product([1, 2, 3]))  # 6

def add_func(list_1):
    greatest_num = list_1[0]
    for i in list_1:
        if i > greatest_num:
            greatest_num = i
    return greatest_num

answer = add_func([5, 150, 45, 20, 75, 30])
print(answer)  # 150

# Missing of parenthesis “()” at the time of function calling can lead to a TypeError.
def greatest_num(num_1):
    greatest = num_1[0]
    for i in num_1:
        if i > greatest:
            greatest = i
    return greatest

print(greatest_num[1, 2, 3])  # TypeError: 'function' object is not subscriptable

values = [3, 6, 9, 12, 15, 18, 21, 24]
other_values = [5, 10, 15, 20, 25, 30]

def odds_sum(num_1):
    sum_1 = 0
    for i in num_1:
        if i % 2 != 0:
            sum_1 += i
    return sum_1

print(odds_sum(values))  # 48
print(odds_sum(other_values))  # 45

def smallest_number(num_list):
    smallest = num_list[0]
    for number in num_list:
        if number < smallest:
            smallest = number
    return smallest
    
print(smallest_number([1, 2, 3]))  # 1

def concatenate(string_list):
    concat = ""
    for string in string_list:
        if len(string) > 2:
            concat += string
    return concat
    
print(concatenate(["abc", "df", "ghi"]))  # abcghi

# Using the index method
def super_sum(string_list):
    sum_1 = 0
    for i in string_list:
        if "s" in i:
            sum_1 += i.index("s")
    return sum_1
    
print(super_sum(["mustache", "greatest", "almost"]))  # 12

# Using the find method - Not a good solution
def super_sum(string_list):
    total = 0
    for string in string_list:
        if string.find("s"):
            total += string.find("s")
    return total
    
print(super_sum(["mustache", "greatest", "almost"]))  # -2 (should be 0)

'''
Reason: The issue comes down to how Python's .find() method behaves when it cannot find a character,
combined with how Python evaluates truthiness in if statements.

Your code is returning -2 because of two specific traps:

Trap 1: .find() returns -1 on failure. When .find("g") doesn't find the letter "g" in a string, it returns -1, not 0 or False.

Trap 2: In Python, -1 is "True". In Python, any non-zero number is considered True when placed inside an if condition.
Because -1 is not 0, your if string.find("g"): statement evaluates to True even when the letter "g" is missing.

Walking through your list step-by-step:
"mustache": Has no "g".
string.find("g") returns -1.
if -1: is True, so it executes total += -1. (Total is now -1)

"greatest": The "g" is at index 0.
string.find("g") returns 0.
if 0: is False (because 0 is falsy), so it skips the block. It completely misses this "g"!

"almost": Has no "g".
string.find("g") returns -1.
if -1: is True, so it executes total += -1. (Total is now -1 + -1 = -2)

That is exactly how you ended up with -2.
'''

# reversed() - To reverse the list
# enumerate() - Iterate over a list with the index position.

# The enumerate function starts by default with 0th index
list_1 = ["H", "E", "L", "L", "O"]

for index, value in enumerate(list_1):
    print(index, value)

# O/p:
# 0 H
# 1 E
# 2 L
# 3 L
# 4 O

# To start the index from any number
list_1 = ["H", "E", "L", "L", "O"]

for index, value in enumerate(list_1, 1):
    print(index, value)

# O/p:
# 1 H
# 2 E
# 3 L
# 4 L
# 5 O

# Define an in_list function that accepts a list of strings and a separate string.
# Return the index where the string exists in the list.
# If the string does not exist, return -1.
# Do NOT use the find or index methods.
# EXAMPLES
# strings = ["enchanted", "sparks fly", "long live"]
# in_list(strings, "enchanted")  ==> 0
# in_list(strings, "sparks fly") ==> 1
# in_list(strings, "fifteen")    ==> -1
# in_list(strings, "love story") ==> -1

# 1st option
def in_list(string_list, string_1):
    for index, value in enumerate(string_list):
        if string_1 == value:
            return index
    return -1

strings = ["enchanted", "sparks fly", "long live"]
print(in_list(strings, "sparks fly"))  # 1

# 2nd option
def in_list(string_list, string_1):
    final = 0
    for index, value in enumerate(string_list):
        if value == string_1:
            final = index
            break
        elif value != string_1:
            final = -1
    return final
    
strings = ["enchanted", "sparks fly", "long live"]
print(in_list(strings, "sparks fly"))  # 1

# Define a sum_of_values_and_indices function that accepts a list of numbers. 
# It should return the sum of all of the elements along with their index values.
#
# EXAMPLES
# sum_of_values_and_indices([1, 2, 3])    => (1 + 0) + (2 + 1) + (3 + 2) => 9
# sum_of_values_and_indices([0, 0, 0, 0]) => 6
# sum_of_values_and_indices([])           => 0

def sum_of_values_and_indices(num_list):
    total = 0
    for index, value in enumerate(num_list):
        total += index + value
    return total

print(sum_of_values_and_indices([1, 2, 3]))  # 9

# range() function: The last number is exclusive.

# for i in range(0, 11) -> It'll go from 0 to 10
# for i in range(2, 11) -> It'll go from 2 to 10
# for i in range(2, 11, 3) -> It'll go from 2 to 10 in an interval of 3, i.e., 2, 5, 8
# for i in range(99, -1, 11) -> It'll go from 99 to 0 in an interval of 11, i.e., 99, 88, 77, 66, etc.

# break() function: To get out from the current flow.
# continue() function: To stop the current iteration and move forward.

for index, num in enumerate([1, 1, 2, 2, 5]):
    if index > num:
        break
    print(num)

# O/p:
# 1
# 1
# 2

# Explanation
# index: 0, 1, 2, 3, 4
# num:   1, 1, 2, 2, 5

for index, num in enumerate([1, 1, 2, 2, 5]):
    if index < num:
        continue
    print(num)

# O/p:
# 1
# 2
# 2

# Assigning new values (overwrite) at a declared position: both +ve and -ve values can be used
# list_name[index_num] = 'new_value'

# Assigning new values to list slice:

coworkers = ["Saloni", "Vaishnavi", "Harshada", "Megha", "Ananya", "Samiksha"]
coworkers[3:5] = ["Sonam", "Pranita"]
print(coworkers)  # ['Saloni', 'Vaishnavi', 'Harshada', 'Sonam', 'Pranita', 'Samiksha']

coworkers = ["Saloni", "Vaishnavi", "Harshada", "Megha", "Ananya", "Samiksha"]
coworkers[3:5] = ["Sonam"]
print(coworkers)  # ['Saloni', 'Vaishnavi', 'Harshada', 'Sonam', 'Samiksha']

coworkers = ["Saloni", "Vaishnavi", "Harshada", "Megha", "Ananya", "Samiksha"]
coworkers[3:5] = ["Sonam", "Pranita", "Udaini"]
print(coworkers)  # ['Saloni', 'Vaishnavi', 'Harshada', 'Sonam', 'Pranita', 'Udaini', 'Samiksha']

# Append method: To add any object to the list at the end.
# Extend method: To add more than an object to the list at the end. A list can also be added.

coworkers = ["Saloni", "Vaishnavi", "Harshada", "Megha", "Ananya", "Samiksha"]
coworkers.append("Udaini")
print(coworkers)  # ['Saloni', 'Vaishnavi', 'Harshada', 'Megha', 'Ananya', 'Samiksha', 'Udaini']

def length_match(string_list, num_1):
    count = 0
    for string in string_list:
        if len(string) == num_1:
            count += 1
    return count
    
print(length_match(["cat", "dog", "kangaroo", "mouse"], 3))  # 2

def sum_from(num_1, num_2):
    sum_1 = 0
    for number in range(num_1, num_2 + 1):
        sum_1 += number
    return sum_1

print(sum_from(3, 8))  # 33

def same_index_values(list_1, list_2):
    list_3 = []
    for index in range(len(list_1)):
        if list_1[index] == list_2[index]:
            list_3.append(index)
    return list_3
        
print(same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"]))  # [1, 3]

def same_index_values(list_1, list_2):
    list_3 = []
    for index_1, _ in enumerate(list_1):
        if list_1[index_1] == list_2[index_1]:
            list_3.append(index_1)
    return list_3

print(same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"]))  # [1, 3]


