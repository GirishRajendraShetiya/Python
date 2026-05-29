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


