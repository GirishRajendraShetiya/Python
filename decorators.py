# Higher order function: A function that either accepts a function as an argument or returns a function as a return value.

def add(a, b):
    return a + b
    
def subtract(a, b):
    return a - b
    
def calculate(func, a, b):
    return func(a, b)
    
print(calculate(add, 5, 6))  # 11

def sample(a):
    return a

def output_func(another_func, string_value):
    return another_func(string_value)

print(output_func(sample, "A"))  # A

def sample():
    print("A")

def main_func(another_func):
    another_func()
    another_func()
    another_func()

main_func(sample)

# O/p:
# A
# A
# A

# If no parenthesis are given for the function, no output will be generated.
def sample():
    print("A")

def main_func(another_func):
    another_func
    another_func
    another_func

main_func(sample)  # No output

def be_nice(good_1):
    def inner():
        print("You're a great person !")
        good_1()
        print("See you !!!")
        
    return inner

@be_nice
def other_func():
    print("Wonderful !")
    
other_func(be_nice)

# O/p:
# You're a great person !
# Wonderful !
# See you !!!

# Nested functions: The functions which are encapsulated within a function, can’t be called from outside that function.

# 1km = 1000m
# 1m = 100cm

def convert_km_to_cm(km_1):
    def convert_km_to_m(km_1):
        print(f"Converting {km_1} km to meters")
        return km_1 * 1000
    
    def convert_m_to_cm(m_1):
        print(f"Converting {m_1} meters to cm")
        return m_1 * 100
    
    kilo_meter = convert_km_to_m(km_1)
    meter = convert_m_to_cm(kilo_meter)
    return meter

print(convert_km_to_cm(1.3))

# O/p:
# Converting 1.3 km to meters
# Converting 1300.0 meters to cm
# 130000.0

# Functions as return values:

def calculator(operation):
    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b

    if operation == "add":
        return add
    elif operation == "subtract":
        return subtract

print(calculator("add")(2, 5))  # 7

def square(num_1):
    return num_1 ** 2

def cube(num_1):
    return num_1 ** 3

operations = [square, cube]

for i in operations:
    print(i(3))

# O/p:
# 9
# 27

def outer():
    def inner():
        return 5
    
    return inner

print(outer()())  # 5

def outer():
    def inner():
        return 5
    
    return inner

print(outer())  # <function outer.<locals>.inner at 0x7f15eb054c10>

def outer():
    def inner():
        return 5
    
    return inner

print(outer)  # <function outer at 0x7f34e67eab80>


