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

# 1st option
def same_index_values(list_1, list_2):
    list_3 = []
    for index in range(len(list_1)):
        if list_1[index] == list_2[index]:
            list_3.append(index)
    return list_3
        
print(same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"]))  # [1, 3]

# 2nd option
def same_index_values(list_1, list_2):
    list_3 = []
    for index_1, _ in enumerate(list_1):
        if list_1[index_1] == list_2[index_1]:
            list_3.append(index_1)
    return list_3

print(same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"]))  # [1, 3]

# insert keyword: To add an object at any position in the list.
# Previous objects are not over-written, instead their position changes respectively.

coworkers = ["Saloni", "Vaishnavi", "Harshada", "Megha", "Ananya", "Samiksha"]
coworkers.insert(1, "Nidhi")
print(coworkers)  # ['Saloni', 'Nidhi', 'Vaishnavi', 'Harshada', 'Megha', 'Ananya', 'Samiksha']

# If given an index not present in the list, Python will extend it to the last position of the list.

coworkers = ["Saloni", "Vaishnavi", "Harshada", "Megha", "Ananya", "Samiksha"]
coworkers.insert(11, "Sailee")
print(coworkers)  # ['Saloni', 'Vaishnavi', 'Harshada', 'Megha', 'Ananya', 'Samiksha', 'Sailee']

# 1st option
def factors(whole_num):
    list_1 = []
    for i in range(1, whole_num + 1):
        if whole_num % i == 0:
            list_1.append(i)
            
    return list_1

print(factors(10))  # [1, 2, 5, 10]

# 2nd option
def factors(whole_num):
    list_1 = []
    i = 1
    while i <= whole_num:
        if whole_num % i == 0:
            list_1.append(i)
        i += 1

    return list_1

print(factors(10))  # [1, 2, 5, 10]

# pop() method: By default, it removes the last object from the list.

coworkers = ["Saloni", "Vaishnavi", "Harshada", "Megha", "Ananya", "Samiksha"]
coworkers.pop()
print(coworkers)  # ['Saloni', 'Vaishnavi', 'Harshada', 'Megha', 'Ananya']

coworkers = ["Saloni", "Vaishnavi", "Harshada", "Megha", "Ananya", "Samiksha"]
coworkers.pop(1)
print(coworkers)  # ['Saloni', 'Harshada', 'Megha', 'Ananya', 'Samiksha']

coworkers = ["Saloni", "Vaishnavi", "Harshada", "Megha", "Ananya", "Samiksha"]
coworkers.pop(-2)
print(coworkers)  # ['Saloni', 'Vaishnavi', 'Harshada', 'Megha', 'Samiksha']

# del keyword: Can remove more than an object at the same time.

coworkers = ["Saloni", "Vaishnavi", "Harshada", "Megha", "Ananya", "Samiksha"]
del coworkers[3]
print(coworkers)  # ['Saloni', 'Vaishnavi', 'Harshada', 'Ananya', 'Samiksha']

coworkers = ["Saloni", "Vaishnavi", "Harshada", "Megha", "Ananya", "Samiksha"]
del coworkers[-3]
print(coworkers)  # ['Saloni', 'Vaishnavi', 'Harshada', 'Ananya', 'Samiksha']

coworkers = ["Saloni", "Vaishnavi", "Harshada", "Megha", "Ananya", "Samiksha"]
del coworkers[3:5]
print(coworkers)  # ['Saloni', 'Vaishnavi', 'Harshada', 'Samiksha'] - The 2nd index is exclusive

# remove method: Removes an object by its value, not index.
# It removes the first occurrence of the object.

coworkers = ["Saloni", "Vaishnavi", "Harshada", "Megha", "Ananya", "Samiksha", "Vaishnavi"]
coworkers.remove("Vaishnavi")
print(coworkers)  # ['Saloni', 'Harshada', 'Megha', 'Ananya', 'Samiksha', 'Vaishnavi']

# If the value is not found, it throws an error.

# clear method: To clear the list.

coworkers = ["Saloni", "Vaishnavi", "Harshada", "Megha", "Ananya", "Samiksha", "Vaishnavi"]
coworkers.clear()
print(coworkers)  # []

def delete_all(string_list, target_string):
    while target_string in string_list:
        string_list.remove(target_string)

    return string_list
    
print(delete_all([1, 2, 3, 3], 3))  # [1, 2]

def push_or_pop(num_list):
    list_1 = []
    for number in num_list:
        if number > 5:
            list_1.append(number)
        elif number <= 5:
            list_1.pop()
    
    return list_1
    
print(push_or_pop([10, 20, 2, 30]))  # [10, 30]

# reverse() method: It returns “None”.

coworkers = ["Saloni", "Vaishnavi", "Harshada", "Megha", "Ananya", "Samiksha", "Vaishnavi"]
coworkers.reverse()
print(coworkers)  # ['Vaishnavi', 'Samiksha', 'Ananya', 'Megha', 'Harshada', 'Vaishnavi', 'Saloni']

# sort() method: It sorts the method.

coworkers = [0, 23, -11]
coworkers.sort()
print(coworkers)  # [-11, 0, 23]

coworkers = ["Saloni", "Vaishnavi", "Harshada", "Megha", "Ananya", "Samiksha", "Vaishnavi"]
coworkers.sort()
print(coworkers)  # ['Ananya', 'Harshada', 'Megha', 'Saloni', 'Samiksha', 'Vaishnavi', 'Vaishnavi']

# To sort strings in ascending order, it'll assign as per the first alphabet’s ASCII value of the string.
coworkers = ["Saloni", "vaishnavi", "Harshada", "Megha", "ananya", "Samiksha", "Vaishnavi"]
coworkers.sort()
print(coworkers)  # ['Harshada', 'Megha', 'Saloni', 'Samiksha', 'Vaishnavi', 'ananya', 'vaishnavi']

# sorted() method: Creates a new list in the memory.

# count() method: To get the number of occurrences in a list. It’s case sensitive.

coworkers = ["Saloni", "Vaishnavi", "Harshada", "Saloni", "Harshada", "Samiksha", "Vaishnavi"]
print(coworkers.count("Saloni"))  # 2

# index() method: Gives the first occurrence of an object. If not found, throws a ValueError.
# index(value, starting_position) and starting_position is inclusive.

coworkers = ["Saloni", "Vaishnavi", "Harshada", "Saloni", "Harshada", "Samiksha", "Vaishnavi"]
print(coworkers.index("Saloni"))  # 0

# Define an encrypt_message function that accepts a string.
# The input string will consist of only alphabetic characters.
# The function should return a string where all characters have been moved
# "up" two spots in the alphabet. For example, "a" will become "c".
#
# EXAMPLES
# encrypt_message("abc") => "cde"
# encrypt_message("xyz") => "zab"
# encrypt_message("")    => ""

def encrypt_message(string_1):
    output_string = ""
    list_1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for char in string_1:
        char_index = list_1.index(char)
        final_char_index = (char_index + 2) % 26
        output_string += list_1[final_char_index]
    return output_string
    
print(encrypt_message("xyz"))  # zab

# copy() method: To make a copy of the list, the copy made is distinct on the computer’s memory.
# [:] can also be used to create a list's copy.

# split() method: Splits a string into a list based on the occurrence of the delimiter (sub-string) in the string
# split(delimiter, threshold_value) -> split(' ', 2) - Only 2 spaces will be removed

users = "Saloni, Nidhi, Samiksha, Sailee, Megha, Lavanya"
print(users.split(", "))  # ['Saloni', 'Nidhi', 'Samiksha', 'Sailee', 'Megha', 'Lavanya']

# join() method: To join all the objects.

users = ["Saloni, Nidhi, Samiksha, Sailee, Megha, Lavanya"]
print(" ".join(users))  # Saloni, Nidhi, Samiksha, Sailee, Megha, Lavanya

def word_lengths(string_1):
    list_1 = []
    for word in string_1.split(" "):
        list_1.append(len(word))
    return list_1

print(word_lengths("Mary Poppins was a nanny"))  # [4, 7, 3, 1, 5]

# Define a cleanup function that accepts a list of strings.
# The function should return the strings joined together by a space.
# There's one BIG problem -- some of the strings are empty or only consist of spaces!
# These should NOT be included in the final string
#
# cleanup(["cat", "er", "pillar"])           => "cat er pillar"
# cleanup(["cat", " ", "er", "", "pillar"])  => "cat er pillar"
# cleanup(["", "", " "])                     => ""

# 1st option
def cleanup(string_list):
    while " " in string_list and "" in string_list:
        string_list.remove(" ")
        string_list.remove("")
    
    return " ".join(string_list)

print(cleanup(["cat", " ", "er", "", "pillar"]))  # cat er pillar

# 2nd option
def cleanup(string_list):
    final_string = ""
    for word in string_list:
        if word == "" or word == " ":
            string_list.remove(word)
    final_string += " ".join(string_list)
    return final_string
    
print(cleanup(["cat", " ", "er", "", "pillar"]))  # cat er pillar

# zip

for a, b, c in zip([3, 2, 1], [1, 2, 3], [2, 3, 1]):
  print("*-*".join([str(a), str(b), str(c)]))

# O/p:
# 3*-*1*-*2
# 2*-*2*-*3
# 1*-*3*-*1

# Multi-dimensional list:

# Define a fancy_concatenate function that accepts a list of lists of strings
# The function should return a concatenated string
# The strings in a list should only be concatenated if the length of the list is 3
#
# EXAMPLES
# fancy_concatenate([["A", "B", "C"]])                        => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]])       => "ABCDEF"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]])  => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E"]])            => "ABC"
# fancy_concatenate([["A", "B"], ["C", "D"]])                 => ""

def fancy_concatenate(strings_list):
    final_string = ""
    for i in strings_list:
        if len(i) == 3:
            for j in i:
                final_string += j
    return final_string

answer = fancy_concatenate([["A", "B", "C"], ["D", "F"]])
print(answer)  # ABC

# List comprehension: In this, the variable used doesn’t store any value after the execution of the program ('number' in this case).
# It will always generate a new list, not mutate the original one.

numbers = [1, 2, 3, 4, 5]
cube = [number ** 3 for number in numbers]
print(cube)  # [1, 8, 27, 64, 125]

# Declare a destroy_elements function that accepts two lists.
# It should return a list of all elements from the first list that are NOT contained in the second list.
# Use list comprehension in your solution.
#
# EXAMPLES
# destroy_elements([1, 2, 3], [1, 2])      => [3]
# destroy_elements([1, 2, 3], [1, 2, 3])   => []
# destroy_elements([1, 2, 3], [4, 5])      => [1, 2, 3]

def destroy_elements(list_1, list_2):
    list_3 = [value for value in list_1 if value not in list_2]
    return list_3
    
answer = destroy_elements([1, 2, 3], [1, 2])
print(answer)  # [3]

# Built-in functions: print, len, int, float, bool, zip, etc.

# help, map, filter, lambda
# map() function:

numbers = [1, 2, 3, 4, 5]
def cubes(num_1):
    return num_1 ** 3
    
print(list(map(cubes, numbers)))  # [1, 8, 27, 64, 125]

animals = ["cat", "dog", "lion", "tiger", "cheetah"]
print(list(map(len, animals)))  # [3, 3, 4, 5, 7]

animals = ["cat", "dog", "lion", "tiger", "cheetah"]
long_animals = [animal for animal in animals if len(animal) > 3]
print(long_animals)  # ['lion', 'tiger', 'cheetah']

# filter(): The first command in the filter statement must return a boolean value.

def is_long(animal):
    return len(animal) > 3

animals = ["cat", "dog", "lion", "tiger", "cheetah"]    
print(list(filter(is_long, animals)))  # ['lion', 'tiger', 'cheetah']

# lambda() function: no return keyword is required to use.

animals = ["cat", "dog", "lion", "tiger", "cheetah"]
print(list(filter(lambda animal: len(animal) > 3, animals)))  # ['lion', 'tiger', 'cheetah']

# 1st option
def right_words(string_list, num_1):
    new_list = [string for string in string_list if len(string) == num_1]
    return new_list

print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3))  # ['cat', 'dog', 'ace']

# 2nd option
def right_words(string_list, num_1):
    return list(filter(lambda string: len(string) == num_1, string_list))
    
print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3))  # ['cat', 'dog', 'ace']

# 3rd option
def right_words(string_list, num_1):
    list_1 = []
    for string in string_list:
        if len(string) == num_1:
            list_1.append(string)
            
    return list_1
    
print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3))  # Same output as above.

def only_odds(num_list):
    return list(filter(lambda num_1: num_1 % 2 != 0, num_list))
    
print(only_odds([1, 3, 5, 6, 7, 8]))  # [1, 3, 5, 7]

# 1st option
def count_of_a(string_list):
    list_1 = []
    for string in string_list:
        list_1.append(string.count("a"))
            
    return list_1
    
print(count_of_a(["alligator", "aardvark", "albatross"]))  # [2, 3, 2]

# 2nd option
def count_of_a(string_list):
    return list(map(lambda string: string.count("a"), string_list))
    
print(count_of_a(["alligator", "aardvark", "albatross"]))  # Same output as above.

# all and any method - all is like “and” operation and any is like “or” operation.

print(all([True]))  # True
print(all([True, False]))  # False
print(all([1, 2]))  # True
print(all([1, 2, 0]))  # False
print(all([]))  # True

print(any([True]))  # True
print(any([True, False]))  # True
print(any([True]))  # True
print(any(['', ' ']))  # True
print(any(['']))  # False
print(any([]))  # False

# dir function: Displays the double underscore methods available in Python.

print("st" in "pasta")  # True
print("pasta".__contains__("st"))  # True

print("pasta" + " and meatballs")  # pasta and meatballs
print("pasta".__add__(" and meatballs"))  # pasta and meatballs

# format() function: to get a formatted value of a number / string. Output is always from the <str> class.

num_1 = 0.123456789
print(format(num_1, "f"))  # 0.123457

num_1 = 0.123456789
print(format(num_1, ".3f"))  # 0.123

print(format(0.6, ".2%"))  # 60.00%

# string:
print(format(1234567, ","))  # 1,234,567
