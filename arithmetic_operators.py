# PEMDAS (Parenthesis, Exponent, Multiplication / Division, Addition / Subtraction) rule is being followed always.

# Division: Few types in Python.

# Clean and Un-clean division
print(15 / 3)  # 5.0
print(14 / 3)  # 4.667

# Input is an integer, then also the output is in float ?
# To handle both the above scenarios [clean (1st case) and un-clean (2nd case) division].

# Floor division - The decimal component of the quotient is chopped off. Also, the output is in integer form.
print(14 // 3)  # 4
print(-14 // 3)  # -5

# Modulo operator - Only the remainder is returned.
print(14 % 3)  # 2
print(18 % 3)  # 0

# Tricky one
print(2 % 3)  # 2 (If the value on the left side is less than the right one, the same left side number is returned)

# Important to note that there is an exception to the left-sided binding order of equal operators when it comes to exponentiations, which are executed in a right-sided binding order.
# That means that exponentiations happen from right to left.

print(2 ** 2 ** 3)  # 256

# In the above example, we could calculate in the following ways:
# 2 ** 2 -> 4; 4 ** 3 -> 64
# 2 ** 3 -> 8; 2 ** 8 -> 256

# However, the second one is correct.

# Now, if we move the first exponentiation into parentheses, we prioritize the operation inside those parentheses.

print((2 ** 2) ** 3)  # 64

# Equal priority operators follow the left to right order except for exponentiations and operations within parentheses.
