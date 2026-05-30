# Variable: Used to reference an object. It doesn’t have any data type.

# Garbage collection: To remove all the values in a program which is not referenced at all.
# Garbage collection refers to Python cleaning up unused objects in the program.
# It occurs whenever an object no longer has a reference (variable) pointing to it (for example, after a variable reassignment).

# Shared variables with Immutable and Mutable Types:

# If an immutable object is present, changes applied to a variable will not impact another object.
# If a mutable object is present, changes to one will impact another one also.

a = 3
b = a
print(a)  # 3
print(b)  # 3

a = 5
b = a
print(a)  # 5
print(b)  # 5

a = [1, 2, 3, 4]
b = a
a.append(5)
print(a)  # [1, 2, 3, 4, 5]
print(b)  # [1, 2, 3, 4, 5]

# Equality vs Identity: All identical objects will be equal, but not all equal objects will be identical.
# 'is' operator is used to validate the identity in Python.

# Equality is the state of two objects being intrinsically equal, i.e. being of the same value.
# Identity means two references (variables) in the program refer to the same object in the computer’s memory.

# For mutable objects - 'a' and 'b' variables are pointing to the same object in the system,
# but the 'c' variable is pointing to another variable even though both objects hold the same value.

a = [1, 2, 3]
b = a

c = [1, 2, 3]

print(a == b)  # True
print(a == c)  # True

print(a is b)  # True
print(a is c)  # False

# For immutable objects - 2 different variables point to the same object.
# Changing an object’s value doesn’t hamper another variable pointing to the same object.

a = 1
b = 1

print(a == b)  # True
print(a is b)  # True

# Shallow and Deep copies:

# Shallow copies: It creates a new list.
# It’s a great choice if the original list doesn’t contain any nested list, a list of numbers, strings, booleans.
# A shallow copy only creates a copy of the outermost level or layer of an object.

# In comparison, a deep copy recursively creates copies of all internal nested objects, down any number of levels.
# It is a more "complete" copy.

# Copy is not made
a = [1, 2, 3]
b = a

print(id(a))  # 139885974374784
print(id(b))  # 139885974374784

print(a == b)  # True
print(a is b)  # True

# Copy has been made
a = [1, 2, 3]
b = a[:]

print(id(a))  # 140275791808896
print(id(b))  # 140275791810816

print(a == b)  # True
print(a is b)  # False

c = a.copy()
print(a == c)  # True
print(a is c)  # False

# shallow copy
numbers = [2, 3, 4]
a = [1, numbers, 5]

b = a[:]

print(a == b)  # True
print(a is b)  # False
print(a[1] is b[1])  # True - As [:] makes shallow copies, hence the nested list 'numbers' is pointing to the same object in the memmory

# deep copy
import copy

numbers = [2, 3, 4]
a = [1, numbers, 5]

b = copy.deepcopy(a)

print(a == b)  # True
print(a is b)  # False
print(a[1] is b[1])  # False
