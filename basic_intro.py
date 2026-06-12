# Python is an OBJECT-ORIENTED language - Everything in Python is in the form of an "object" which means a data structure, a way of storing data.
# REPL (Read, Evaluate, Print, Loop)

# Object has the following types: Identity, Type & Value

# Through identity, mutability (changeable) and immutability (non-changeable) could be figured out.

# Immutability: Integers, Floats, Booleans, Tuples and Strings.

num_1 = 10
print(num_1)  # 10
print(id(num_1))  # 140265468717416

num_1 = 20
print(num_1)  # 20
print(id(num_1))  # 140265468717736

# The same variable num_1 points to 2 different references (10 & 20), as integers can’t be modified (immutable).
# In Python, variables aren't boxes that hold data; they are labels (or pointers) that stick to objects floating around in computer memory.

# It rips the label num_1 off of the 10 and sticks it onto the 20.
# The integer 10 is still sitting in memory (at least until Python's garbage collector cleans it up), but the variable num_1 has completely lost track of it.

# Mutability

set_1 = set()
print(set_1)  # set() - Empty set is created

set_1.add(10)
print(set_1)  # {10}

# The set_1 variable is pointing to same reference even after updating it, as it’s modifiable (mutable).

# Comment is also called as 'octothorpe'
# For inline comments, keep 2 spaces between the code and the “#” tag, and 1 space between the hash tag and the comment to be written.

# Any file / folder containing the __init__.py file, it’s called a package.
# Other .py files are called modules.

# To install packages faster, use “uv” package manager instead of “pip”.

# Data Types:
# Numbers- Integers, Boolean, Float, Complex
# Logical - And, Or, Not / Negation
# String
