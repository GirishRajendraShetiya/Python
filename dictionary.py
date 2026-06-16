# An un-ordered and mutable data structure for declaring relationships between objects.
# It’s a key-value pair. Denoted by '{}'.

# Keys should be unique and are case-sensitive, values can be duplicates.
# Keys should be immutable (integers, tuples, booleans), values can be of any type.

# If there are 2 same keys present in the dictionary, the latest / last one will be picked.

# Dictionary is for mapping, List is for order.
# If the key is not present in the defined dictionary, a KeyError will be generated.

age = {
    "A": 24,
    "B": 25,
    "C": 24
}

print(age[1])  # KeyError

age = {
    "A": 24,
    "B": 25,
    "C": 24
}

print(age["A"])  # 24

# get() method: To access a value, get() method can also be used.
# Also, if the mentioned key is not present in the defined dictionary,
# the second passed argument will work as the value for the key, instead of throwing an error.
# If nothing is mentioned, the method will return “None”.

age = {
    "A": 24,
    "B": 25,
    "C": 24
}
print(age.get("D", 26))  # 26

age = {
    "A": 24,
    "B": 25,
    "C": 24
}

print(age.get("D"))  # None

# in and not in operator in dictionary: To validate whether the mentioned key is present in the dictionary or not.

age = {
    "A": 24,
    "B": 25,
    "C": 24
}

print("A" in age)  # True
print(age.get("D", 25))  # 25
print("D" in age)  # False
print("B" not in age)  # False

# Add or Modify Key-Value pair in Dictionary:

age = {
    "A": 24,
    "B": 25,
    "C": 24
}

age["D"] = [23, 25]
print(age["D"])  # [23, 25]
print(age)  # {'A': 24, 'B': 25, 'C': 24, 'D': [23, 25]}

words = ["danger", "beware", "danger", "rocket"]

def words_count(string_list):
    dict_1 = {}
    for word in string_list:
        if word in dict_1:
            dict_1[word] += 1
        else:
            dict_1[word] = 1
    
    return dict_1

print(words_count(words))  # {'danger': 2, 'beware': 1, 'rocket': 1}

# setdefault() method: In the get() method, the mentioned key-value pair doesn’t mutate the original dictionary,
# but in the setdefault() method, the pair gets added to the dictionary.
# If the key is already present in the dictionary, the value doesn’t get updated.

age = {
    "A": 24,
    "B": 25
}

age.setdefault("C", 26)
print(age)  # {'A': 24, 'B': 25, 'C': 26}

def to_dictionary(string_list):
    dict_1 = {}
    for detective in string_list:
        dict_1[detective] = string_list.index(detective)
    
    return dict_1

detectives = ["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]
answer = to_dictionary(detectives)
print(answer)  # {'Sherlock Holmes': 0, 'Hercules Poirot': 1, 'Nancy Drew': 2}

def length_counts(string_list):
    dict_1 = {}
    for string in string_list:
        if len(string) in dict_1:
            dict_1[len(string)] += 1
        else:
            dict_1[len(string)] = 1

    return dict_1
    
print(length_counts(["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]))  # {6: 1, 9: 2, 7: 2, 4: 1}

def length_counts(elements):
    counts = {}

    for element in elements:
        length = len(element)
        current_count = counts.get(length, 0)
        counts[length] = current_count + 1

    return counts  # Same as above

# pop() method / del keyword: To delete a key-value pair

age = {
    "A": 24,
    "B": 25
}
new_age = age.pop("C", 26)
print(new_age)  # 26
print(age)  # {'A': 24, 'B': 25}

age = {
    "A": 24,
    "B": 25
}

del age["B"]
print(age)  # {'A': 24}

def delete_keys(dict_1, string_list):
    for string in string_list:
        if string in dict_1:
            dict_1.pop(string)
    return dict_1

my_dict = {
    "A": 1,
    "B": 2,
    "C": 3
}

strings = ["A", "C"]
    
print(delete_keys(my_dict, strings))  # {“B”: 2}

# clear() method: To clear / delete the dictionary

age = {
    "A": 24,
    "B": 25
}

age.clear()
print(age)  # {}

# del keyword can also be used to remove the variable pointing to the dictionary object.

age = {
    "A": 24,
    "B": 25
}

del age
print(age)  # NameError will be thrown

# update() method: To merge a dictionary into another.
# Duplicate key gets updated with the merging list.

age = {
    "A": 24,
    "B": 25
}

age_1 = {
    "C": 25,
    "D": 27
}

age.update(age_1)
print(age)  # {'A': 24, 'B': 25, 'C': 25, 'D': 27}

# dict() function: To create an empty dictionary.

age = [
    ["A", 25],  # key: value
    ["B", 26],
    ["C", 24]
]

print(dict(age))  # {'A': 25, 'B': 26, 'C': 24}

nba_finals = {

  "Game 1": {

    "date": "05/05/2019",

    "location": "San Francisco",

    "statistics": {

      "points": 200,

      "rebounds": 20,

      "assists": 25

    }

  }

}  # nba_finals["Game 1"]["statistics"]["rebounds"]

# Accessing values in a dictionary:

age = {
    "A": 24,
    "B": 25,
    "C": 25
}

for person in age:
    print(f"The age of {person} is {age[person]}")

# O/p:
# The age of A is 24
# The age of B is 25
# The age of C is 25

pounds_to_kilos = {
    5: 2.72,
    10: 5.2,
    25: 11.26
}

for number in pounds_to_kilos:
    print(f"{number} is equal to {pounds_to_kilos[number]}")

# O/p:
# 5 is equal to 2.72
# 10 is equal to 5.2
# 25 is equal to 11.26

# items() method:

pounds_to_kilos = {
    5: 2.72,
    10: 5.2,
    25: 11.26
}

for number, conv in pounds_to_kilos.items():
    print(f"{number} is equal to {conv}")

# O/p:
# 5 is equal to 2.72
# 10 is equal to 5.2
# 25 is equal to 11.26

# Underscore is used to not get the value from the dictionary:

pounds_to_kilos = {
    5: 2.72,
    10: 5.2,
    25: 11.26
}

for _, conv in pounds_to_kilos.items():
    print(f"It is equal to {conv}")

# O/p:
# It is equal to 2.72
# It is equal to 5.2
# It is equal to 11.26

def invert(dict_obj):
    dict_1 = {}
    for key in dict_obj:
        dict_1.setdefault(dict_obj[key], key)
        
    return dict_1
    
my_dict = {
  "A": "B", 
  "C": "D",
  "E": "F"
}

print(invert(my_dict))  # {'B': 'A', 'D': 'C', 'F': 'E'}

def count_of_value(dict_1, obj_1):
    count = 0
    for _, value in dict_1.items():
        if value == obj_1:
            count += 1
    
    return count
    
my_dict = { "a" : 5, "b" : 3, "c" : 5 }
print(count_of_value(my_dict, 5))  # 2

def sum_of_values(dict_1, string_list):
    count = 0
    for key, value in dict_1.items():
        if key in string_list:
            count += value
    return count

my_dict = { "a": 5, "b": 3, "c": 10 }
print(sum_of_values(my_dict, ["a", "c"]))  # 15

# keys() & values() methods: To get keys and values from the dictionary

pounds_to_kilos = {
    5: 2.72,
    10: 5.2,
    25: 11.26
}

print(pounds_to_kilos.keys())  # dict_keys([5, 10, 25])
print(pounds_to_kilos.values())  # dict_values([2.72, 5.2, 11.26])

# The output above are not lists, they’re of class dict_keys.

def common_elements(dict_1):
    list_1 = []
    for k in dict_1.keys():
        if k in dict_1.values():
            list_1.append(k)
    return list_1
    
my_dict = {
  "A": "K",
  "B": "D",
  "C": "A",
  "D": "Z"
}

print(common_elements(my_dict))  # [“A”, “D”]

# Alternative to the above question:

def common_elements(dict_1):
    return [key for key in dict_1.keys() if key in dict_1.values()]

# sorted() function: Sorts the dictionary as per the key and also returns only the key in a list format,
# which doesn’t mutate the original dictionary.

age = {
    "C": 20,
    "D": 25,
    "A": 26
}

print(sorted(age))  # ['A', 'C', 'D']

details = [
    {"name": "Girish", "age": 24, "company": "TCS"},
    {"name": "Anil", "age": 25, "company": "TCS"},
    {"name": "Shashikant", "age": 36, "company": "TCS"}
]

for i in details:
    for k, v in i.items():
        print(f"{k}: {v}")

# O/p:
# name: Girish
# age: 24
# company: TCS
# name: Anil
# age: 25
# company: TCS
# name: Shashikant
# age: 36
# company: TCS

complexity = [
    {"Name": True, "Age": False},
    {2.1: ["A", "B", "C"], 2.2: ["D", "E", "F"], 2.3: ["G", "H", "I"]},
    {"Name": False, "Age": True},
    {4.1: ["A1", "B1", "C1"], 4.2: ["D1", "E1", "F1"], 4.3: ["G1", "H1", "I1"]}
]

# **kwargs - Keyword arguments in dictionary format.
# If keyword variables are present, then only **kwargs will represent them, otherwise NOT.

def height_to_meters(feet, inches):
    total_inches = (feet * 12) + inches
    return total_inches * 0.0254

details = {
    "feet": 5,
    "inches": 11
}

print(height_to_meters(**details))  # 1.8034

def plenty_of_arguments(a, b, **kwargs):
    sum_1 = 0
    sum_1 += a + b + sum(kwargs.values())
    
    if sum_1 > 100:
        return True
    else:
        return False
        
answer = plenty_of_arguments(a = 25, b = 25, c = 25, d = 26)
print(answer)  # True

# Dictionary comprehension:

tea_price_inr = {
    "Masala Chai": 40,
    "Green Tea": 50,
    "Lemon Tea": 60
}

tea_price_dollar = {
    chai: inr_price / 95 for chai, inr_price in tea_price_inr.items()
}
print(tea_price_dollar)  # {'Masala Chai': 0.42105263157894735, 'Green Tea': 0.5263157894736842, 'Lemon Tea': 0.631578947368421}

word = "hcgjxrhxjxfysrkxdtcuycuytvgjytvygviuttiovdcdxo"
count_1 = {letter: word.count(letter) for letter in word}
print(count_1)  # {'h': 2, 'c': 4, 'g': 3, 'j': 3, 'x': 5, 'r': 2, 'f': 1, 'y': 5, 's': 1, 'k': 1, 'd': 3, 't': 5, 'u': 3, 'v': 4, 'i': 2, 'o': 2}

# You are writing a Python program to model a remote control
# for a television set. Declare a stations_to_numbers
# function that accepts a dictionary. The keys will be
# channel numbers and the values will be the station names.
# For example...
# channels = {
#   2: "CBS",
#   4: "NBC",
#   5: "FOX",
#   7: "ABC"
# }
# The stations_to_numbers function should return an
# inverted dictionary where the keys are the station names
# and the values are the channel numbers
# stations_to_numbers(channels) => {'CBS': 2, 'NBC': 4, 'FOX': 5, 'ABC': 7}

def stations_to_numbers(dict_1):
    final = {value: key for key, value in dict_1.items()}
    return final
    
channels = {
  2: "CBS",
  4: "NBC",
  5: "FOX",
  7: "ABC"
}

answer = stations_to_numbers(channels)
print(answer)  # {'CBS': 2, 'NBC': 4, 'FOX': 5, 'ABC': 7}
