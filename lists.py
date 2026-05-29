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

def super_sum(string_list):
    sum_1 = 0
    for i in string_list:
        if "s" in i:
            sum_1 += i.index("s")
    return sum_1
    
print(super_sum(["mustache", "greatest", "almost"]))  # 12


