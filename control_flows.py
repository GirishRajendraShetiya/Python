# Control flow:

# bool condition:

print(bool(0))  # False
print(bool(1))  # True

# Empty string & 0 has a false value
# Rest others has a true value

# if condition:

def truthy_or_falsy(word):
    if bool(word):
        return f"The value {word} is truthy"
    return f"The value {word} is falsy"
    
print(truthy_or_falsy("D"))  # The value D is truthy

def negative_number(num):
    if num > 0:
        return num
    elif num < 0:
        return -1 * num
    else:
        return 0

print(negative_number(-15))  # 15

# In the above code, the negative_number function returns a value which is passed to the “print” function, which then displays the value.

def negative_number(num):
    if num > 0:
        print(num)
    elif num < 0:
        print(-1 * num)
    else:
        print(0)

answer = negative_number(-15)
print(answer)

# O/p:
# 15
# None

def negative_number(num):
    if num > 0:
        print(num)
    elif num < 0:
        print -1 * num
    else:
        print(0)

answer = negative_number(-15)
print(answer)  # TypeError: unsupported operand type(s) for -: 'builtin_function_or_method' and 'int'

pin_code = "400706"
check = "Valid" if len(pin_code) == 2 else "Invalid"
print(check)  # Invalid

def string_theory(string_1):
    if len(string_1) > 3 and string_1.startswith("S"):
        return True
    return False

print(string_theory("Fable"))  # False

# While loop:

# If print(fizzbuzz(30)) is used, the last run will generate a “None” output.
# Use “return” keyword in the function with outside “print” statement.

def fizzbuzz(num):
    num1 = 1
    while num1 <= num:
        if num1 % 3 == 0 and num1 % 5 == 0:
            print("FizzBuzz")
        elif num1 % 3 == 0:
            print("Fizz")
        elif num1 % 5 == 0:
            print("Buzz")
        else:
            print(num1)
        num1 += 1

fizzbuzz(30)

# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16
# 17
# Fizz
# 19
# Buzz
# Fizz
# 22
# 23
# Fizz
# Buzz
# 26
# Fizz
# 28
# 29
# FizzBuzz

def fizzbuzz(num):
    num1 = 1
    while num1 <= num:
        if num1 % 3 == 0 and num1 % 5 == 0:
            print("FizzBuzz")
        elif num1 % 3 == 0:
            print("Fizz")
        elif num1 % 5 == 0:
            print("Buzz")
        else:
            print(num1)
        num1 += 1

print(fizzbuzz(30))  # Same as above with None at the end.

flavors = ['mint', 'tulsi']
choice_flavor = input("Enter your choice: ")

while choice_flavor not in flavors:
    choice_flavor = input("Enter again: ")

print(f"{choice_flavor} is present")

# O/p:
# Enter your choice: f
# Enter again: f
# Enter again: mint
# mint is present

users = [
    {'id': 1, 'total': 100, 'coupon': "P20"},
    {'id': 2, 'total': 150, 'coupon': "F20"},
    {'id': 3, 'total': 200, 'coupon': "G20"},
    ]

discounts = {
    "P20": (0.2, 0),
    "F20": (0.5, 0),
    "G20": (0, 10),
}

for user in users:
    percent, fixed = discounts.get(user['coupon'], (0, 0))
    discount = user['total'] * percent + fixed
    print(f"{user["id"]} paid {user["total"]} and got a discount of {discount}")

# O/p:
# 1 paid 100 and got a discount of 20.0
# 2 paid 150 and got a discount of 75.0
# 3 paid 200 and got a discount of 10

# Recursion: A base case is important to stop at a particular point.

# 1st option
def reverse(str_1):
    return str_1[::-1]
    
print(reverse("straw"))  # warts

# 2nd option
def reverse(str_1):
    index_of_string = len(str_1) - 1
    str_2 = ""
    
    while index_of_string >= 0:
        str_2 = str_2 + str_1[index_of_string]
        index_of_string -= 1
    return str_2
    
print(reverse("straw"))  # warts

# 3rd option
def reverse_string(str_1):
    if len(str_1) == 1:
        return str_1
    
    return str_1[-1] + reverse_string(str_1[:-1])  # Everytime, reverse_string(str_1[:-1]) has all the characters of the string excluding the last character
    
print(reverse_string("straw"))  # warts

# Factorial by recursion
def factorial(num_1):
    if num_1 == 0 or num_1 == 1:
        return 1
    
    return num_1 * factorial(num_1 - 1)
    
print(factorial(5))  # 120

# For loop:

words = ["cat", "dog", "rhino"]
for word in words:
    print(word)

# O/p:
# cat
# dog
# rhino

# The variable used ('word' in this case) holds the latest / last value of the list.

print("word")  # rhino

staff = [("Amit", 16), ("Rana", 17), ("Purohit", 17)]

for member, age in staff:
    if age >= 18:
        print(f"{member} is hired")
        break

# The below else block will execute if the above for loop didn't break
else:
    print("No one is eligible for hiring")  # No one is eligible for hiring

# The condition is reversed
staff = [("Amit", 16), ("Rana", 17), ("Purohit", 17)]

for member, age in staff:
    if age <= 18:
        print(f"{member} is hired")
        break

else:
    print("No one is eligible for hiring")  # Amit is hired
