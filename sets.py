# It's a mutable, un-ordered data structure that prohibits duplicate values. Declared by “{}”

# Lists and Dictionaries are not allowed in sets as they're mutable.
# Integers, Floats, Tuples and Booleans are allowed as they're immutable.

stocks = {"A", "B", "C"}
print(stocks)  # {'C', 'A', 'B'}

# in and not in operator in sets:

stocks = {"A", "B", "C"}
print("B" in stocks)  # True

stocks = {"A", "B", "C"}
print("A" not in stocks)  # False

# set doesn't support indexing, if tried, an error will be thrown.

# set() - To create an empty set

print(set([1, 2, 3]))  # {1, 2, 3}

def remove_duplicates(list_1):
    list_set = list(set(list_1))
    return list_set
    
print(remove_duplicates([1, 2, 1, 2]))  # [1, 2]

# All the below mentioned methods are case-sensitive.

# add() method: Lists can’t be added as it’s mutable.

friends = {"Saloni", "Ishika", "Samiksha"}
friends.add("Nidhi")
print(friends)  # {'Nidhi', 'Samiksha', 'Saloni', 'Ishika'}

# update() method: To add more than an object. It accepts lists, tuples as an argument.

friends = {"Saloni", "Ishika", "Samiksha"}
friends.update(["Nidhi", "Lavanya"])
print(friends)  # {'Nidhi', 'Lavanya', 'Samiksha', 'Ishika', 'Saloni'}

# remove() method: If the value which is to be looked into the set is not present, it throws a KeyError exception.

friends = {"Saloni", "Ishika", "Samiksha"}
friends.remove("Ishika")
print(friends)  # {'Saloni', 'Samiksha'}

friends = {"Saloni", "Ishika", "Samiksha"}
friends.remove("ishika")
print(friends)  # KeyError: “ishika"

# discard() method: If the value which is to be looked into the set is not present, it doesn’t throw any exception.

friends = {"Saloni", "Ishika", "Samiksha"}
friends.discard("Ishika")
print(friends)  # {'Saloni', 'Samiksha'}

friends = {"Saloni", "Ishika", "Samiksha"}
friends.discard("Nidhi")
print(friends)  # {'Ishika', 'Saloni', 'Samiksha'}

# In a set, it’ll separate the mentioned string in a single character.

h = set("sw")
print(h)  # {'s', 'w'}

# intersection() method: Displays what is common in both the sets.

a = {"Girish", "Anil", "Amit"}
b = {"Rahul", "Anil", "Denik"}

print(a & b)  # {“Anil”}
print(a.intersection(b))  # {“Anil”}

# union() method: It’s the combination of all the elements present in both the sets.
# Duplicates are removed.

a = {"Girish", "Anil", "Amit"}
b = {"Rahul", "Anil", "Denik"}

print(a | b)  # {'Rahul', 'Girish', 'Denik', 'Anil', 'Amit'}
print(a.union(b))  # {'Rahul', 'Girish', 'Denik', 'Anil', 'Amit'}

# difference() method:

a = {"Girish", "Anil", "Amit"}
b = {"Rahul", "Anil", "Denik"}

print(a - b)  # {'Girish', 'Amit'}
print(a.difference(b))  # {'Girish', 'Amit'}
print(b - a)  # {'Denik', 'Rahul'}
print(b.difference(a))  # {'Denik', 'Rahul'}

# symmetric_difference() method: To check the elements not shared by both the sets.

a = {"Girish", "Anil", "Amit"}
b = {"Rahul", "Anil", "Denik"}

print(a ^ b)  # {'Girish', 'Amit', 'Rahul', 'Denik'}
print(a.symmetric_difference(b))  # {'Girish', 'Amit', 'Rahul', 'Denik'}

# issubset() & issuperset() methods:

a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

print(a.issubset(b))  # True

a = {1, 2, 3}
b = {1, 2, 3}
print(a.issubset(b))  # True

a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
print(a.issuperset(b))  # False

a = {1, 2, 3}
b = {1, 2, 3}
print(a.issuperset(b))  # True

# frozenset() - im-mutable set. No addition / update is allowed.

mr_freeze = frozenset([1, 2, 3, 2])
print(mr_freeze)  # frozenset({1, 2, 3})

# Use-case: A dictionary’s key consists of im-mutable objects (integer, boolean, tuple), frozen set could also be used.

mr_freeze = frozenset([1, 2, 3, 2])
print({mr_freeze: 'Some value'})  # {frozenset({1, 2, 3}): 'Some value'}
