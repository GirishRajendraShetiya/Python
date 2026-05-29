# Fixed length of im-mutable list.
# Values separated by “,” and within round parenthesis.
# Within a tuple, if a mutable object like list is included, it’s accepted.

# to change a list into tuple - tuple(list_1)

values = (1, 2)
print(type(values))  # <class 'tuple'>

faves = ["A", "B", "C"]
movies = tuple(faves)
print(movies)  # ('A', 'B', 'C')

numbers_a = (1, 2, 3)
numbers_b = (4, 5, 6)
numbers_c = (7, 8, 9)
all_numbers = (numbers_a, numbers_b, numbers_c)

values = (7, 5, 2000)
print(len(values))  # 3

values = (7, 5, 2000)
print(values[1])  # 5

values = (7, 5, 2000)
print(values[-1])  # 2000

values = (["Swift", "Renault", "Hyundai", "Tata"],
["BMW", "Ferrari", "Lamborgini", "Aston Martin"])

values[1][2] = "Maserati"
print(values)  # (['Swift', 'Renault', 'Hyundai', 'Tata'], ['BMW', 'Ferrari', 'Maserati', 'Aston Martin'])

# Un-packing a tuple:
values = ("Swift", "Renault", "Hyundai", "Tata")

car_1, car_2, car_3, car_4 = values
print(car_1, car_2, car_3, car_4)  # Swift Renault Hyundai Tata

values = ("Swift", "Renault", "Hyundai", "Tata")

car_1, car_2, car_3 = values
print(car_1, car_2, car_3)  # ValueError: too many values to unpack (expected 3)

# asterisk (*) is used to combine more than an object and the output is a list (NOT a tuple):
# Only a single asterisk can be used at a time.

values = ("Swift", "Renault", "Hyundai", "Tata")

car_1, car_2, *car_3 = values
print(car_1, car_2, car_3)  # O/p: Swift Renault ['Hyundai', 'Tata']

values = ("Swift", "Renault", "Hyundai", "Tata")

*car_1, car_2, car_3 = values
print(car_1, car_2, car_3)  # ['Swift', 'Renault'], 'Hyundai', 'Tata'

def greatest_num(*num_1):
    greatest = num_1[0]
    for number in num_1:
        if number > greatest:
            greatest = number
            
    return greatest

print(greatest_num(1, 4, -2, 0))  # 4

# If any variable is to be assigned post the *args variable, it should be a keyword argument.

# def greatest_num(*num_1, name):
# greatest_num(1, 3, 5, name = 'Girish')

# To unpack arguments:

def product(a, b):
    return a * b

print(product(3, 5))  # 15

# tuple or list both can be used.
numbers = [3, 5]
numbers = (3, 5)

print(product(*numbers))  # 15
