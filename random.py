import random
print(random.random())  # 0.9370128477805795 (Generates a random number between 0 and 1)

# If a larger number is required, multiply it with 10, 100, etc.

print(random.random() * 100)  # 99.53323223626612

# randint: To randomly generate an integer between the given numbers (both are inclusive).

import random
print(random.randint(1, 5))  # 5

# randrange: To randomly generate an integer between the given numbers but with a step and also the upper bound is EXCLUSIVE.

import random
print(random.randrange(0, 50, 10))  # 20

# choice function from the random module: Iterable order objects can be provided as inputs like strings,
# lists, tuples (but not dictionary and set). Output is a single character.

import random
print(random.choice([1, 2, 3]))  # 2
print(random.choice("cheetah"))  # t

# sample function from the random module: Provides an output in the list format.

import random
lottery = [random.randint(0, 49) for number in range(0, 50)]
# print(lottery)

print(random.sample(lottery, 2))  # [29, 12]
print(random.sample(lottery, 3))  # [47, 5, 29]

# shuffle function: It requires ONLY mutable objects like a list.

import random
characters = ["Girish", "Rajendra", "Shetiya"]

print(random.shuffle(characters))  # None (No output is returned for the random.shuffle function)
print(characters)  # ['Shetiya', 'Girish', 'Rajendra']

# An attempt was made to randomize the roles list provided below.
# However, the roles variable still points to the same sequence even after being passed to the shuffle function.
# Why is this occurring ?

import random
roles = ["DPS", "Tank", "Healer"]
random.shuffle(sorted(roles))
print(roles)  # ["DPS", "Tank", "Healer"]

# Reason: The sorted function is creating a copy of the roles list. That list is shuffled, then thrown out of memory.
# The original roles list remains unaffected.
