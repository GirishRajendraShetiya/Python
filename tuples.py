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


