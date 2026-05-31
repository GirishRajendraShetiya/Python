# Class - A blueprint from which objects are made. A class name can only contain letters, numbers and underscores.
# They use Camelcasing (Eg: MyFirstClass).

# Object - It’s an instance of a class.
# Instance - An object made from a class.

# A method can be viewed as a function belonging to an object.
# It can interact and modify an object’s attribute, which in turn alters its state.

# type - to get the class type of data
# int, float & str - to convert to any data type

class Person():
    pass

class DataBaseConnection():
    pass

Girish = Person()

print(Girish)  # <__main__.Person object at 0x7f14542768b0>

# The 'self' keyword used in the below code, aids in getting the values coming to the class Piano().
class Piano():
    def __init__(self):
        print(f"This is {self}")
        
Girish = Piano()  # This is <__main__.Piano object at 0x7f2dd8d6df10>
print(Girish)  # <__main__.Piano object at 0x7f2dd8d6df10>

class Piano():
    def __init__(self):
        self.wood = "Mahogany"
        
Girish = Piano()
Lavanya = Piano()
print(Girish.wood)  # Mahogany
print(Lavanya.wood)  # Mahogany

class Piano():
    def __init__(self, wood):
        self.wood = wood
        
Girish = Piano("Mahogany")
Lavanya = Piano("Alder")
print(Girish.wood)  # Mahogany
print(Lavanya.wood)  # Alder

# Instance method: A function that belongs to an object.

class Cars():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year  = year
    
    def func_1(self):
        print("Rider !")
        
Rider_1 = Cars("Audi", "R8", 2008)
Rider_2 = Cars("Aston Martin", "A8", 2010)

Rider_1.func_1()  # Rider !
Rider_2.func_1()  # Rider !

class Cars():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year  = year
    
    def func_1(self):
        print("Rider !")
        
    def func_2(self):
        print(f"{self.brand}, you're in {self.year}")
        
Rider_1 = Cars("Audi", "R8", 2008)
Rider_2 = Cars("Aston Martin", "A8", 2010)

Rider_1.func_1()  # Rider !
Rider_2.func_1()  # Rider !

Rider_1.func_2()  # Audi, you're in 2008
Rider_2.func_2()  # Aston Martin, you're in 2010

class Cars():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year  = year
    
    def func_1(self):
        print("Rider !")
        
    def func_2(self):
        print(f"{self.brand}, you're in {self.year}")
    
    def func_3(self, next_year):
        self.year -= next_year
    
Rider_1 = Cars("Audi", "R8", 2008)
Rider_2 = Cars("Aston Martin", "A8", 2010)

Rider_1.func_1()  # Rider !
Rider_2.func_1()  # Rider !

Rider_1.func_2()  # Audi, you're in 2008
Rider_2.func_2()  # Aston Martin, you're in 2010

Rider_1.func_3(100)
print(Rider_1.year)  # 1908

# Protected attributes and methods (Encapsulation): The attributes can be defined with an underscore to show Python developers
# that it’s protected.

class Cars():
    def __init__(self, brand, model, year):
        self._brand = brand
        self._model = model
        self._year  = year

class SmartPhone():
    def __init__(self):
        self._company = "Apple"
        self._firmware = 10.0
        
    def get_access(self):
        return self._firmware
        
    def update_os_version(self):
        print("Reaching out to the server ...")
        self._firmware += 1
        
iPhone = SmartPhone()

print(iPhone._firmware)  # 10.0

# If the function is only passed, the position in the memory is only shown
print(iPhone.update_os_version)  # <bound method SmartPhone.update_os_version of <__main__.SmartPhone object at 0x7f249e6dbf10>>
print(iPhone._firmware)  # 10.0

class SmartPhone():
    def __init__(self):
        self._company = "Apple"
        self._firmware = 10.0
        
    def get_access(self):
        return self._firmware
        
    def update_os_version(self):
        print("Reaching out to the server ...")
        self._firmware += 1
        
iPhone = SmartPhone()

print(iPhone._firmware)  # 10.0

# If print function is used, as it expects something in return,
# and if nothing gets from the called function, it displays as 'None'.
print(iPhone.update_os_version())  # Reaching out to the server ...
print(iPhone._firmware)  # 11.0
# None

class SmartPhone():
    def __init__(self):
        self._company = "Apple"
        self._firmware = 10.0
        
    def get_access(self):
        return self._firmware
        
    def update_os_version(self):
        print("Reaching out to the server ...")
        self._firmware += 1
        
iPhone = SmartPhone()

print(iPhone._firmware)  # 10.0

# As the called function returns nothing, and the function is being invoked
iPhone.update_os_version()  # Reaching out to the server ...
print(iPhone._firmware)  # 11.0

# book.py
# Let’s say we want to model a Book as a Python object. 
# A Book has an author and a publisher, which are characteristics that cannot change. 
# A Book also has a page_count, which could be altered if you rip some pages from the book.

# Declare a Book class that accepts author, publisher, and page_count parameters. 
# Each of the parameters should be assigned to an attribute. 
# The author and publisher attributes should be designated as protected (use an underscore). 
# The page_count attribute should be designated public.

class Book():
    def __init__(self, author, publisher, page_count):
        self._author = author
        self._publisher = publisher
        self.page_count = page_count

# Define a copyright instance method that returns a string with information about the copyright. 
# It should look the string below, where “Grant Cardone” is the value of the protected
# author attribute and “10X Enterprises” is the value of the protected publisher attribute.

    def copyright(self):
        return f"Copyright {self._author}, {self._publisher}"
        
# => Copyright Grant Cardone, 10X Enterprises

# The public page_count attribute can always be manually modified. 
# However, we can still define an instance method that modifies it. 

# Declare a rip_in_half instance method. 
# If the book has more than 1 page, it should halve the page_count. 
# If the book has 1 page or less, it should set the page_count to 0.

    def rip_in_half(self):
        if self.page_count > 1:
            self.page_count = self.page_count / 2
        else:
            self.page_count = 0

# See sample execution below

book = Book(author = "Grant Cardone", publisher = "10X Enterprises", page_count = 10)

book.copyright() # Copyright Grant Cardone, 10X Enterprises

print(book.page_count) # 10
book.rip_in_half()
print(book.page_count) # 5.0
book.rip_in_half()
print(book.page_count) # 2.5
book.rip_in_half()
print(book.page_count) # 1.25
book.rip_in_half()
print(book.page_count) # 0.625
book.rip_in_half()
print(book.page_count) # 0
book.rip_in_half()
print(book.page_count) # 0

# Declare a Musician class that accepts age and income parameters. 

class Musician():
    def __init__(self, age, income):
        self.age = age
        self.income = income

# In the instantiation process for an object, assign the two parameters
# to two attributes with the same name.

# Declare an enter_club instance method.

    def enter_club(self):
        if self.age < 21:
            return "Access denied!"
        else:
            return "Access granted!"

# If the musician is less than 21 years old, the method should 
# return the string "Access denied!”. 
# If the musician is 21 or older, the method should
# return the string "Access granted!".

# Declare a play_show instance method. The method should
# increment the musician’s income by 5.

    def play_show(self):
        self.income += 5

# EXAMPLES
#
cliff = Musician(age = 27, income = 0)
print(cliff.age)    # 27
print(cliff.enter_club())  # "Access granted!"
print(cliff.income) # 0
cliff.play_show()
print(cliff.income) # 5
cliff.play_show()
print(cliff.income) # 10

# Getters / Setters: Instance methods that get / set attribute values on an object.

# Property - a getter method, a setter method, a deletor method, a docstring describing the function of the property.
# It gives the appearance of an attribute, but behind the scenes, it invokes an instance method.

class Height():
    def __init__(self, feet):
        self._inches = feet * 12
        
    def _get_feet(self):
        return self._inches / 12
        
    def _set_feet(self, feet):
        if feet >= 0:
            self._inches = feet * 12
            
    feet = property(_get_feet, _set_feet)
    
h = Height(5)
print(h.feet)  # 5.0

h.feet = 6
print(h._inches)  # 72

class Currency():
    def __init__(self, dollars):
        self._cents = dollars * 100
    
    @property
    def dollars(self):
        return self._cents / 100
    
    # To create a setter method with the same name as the getter method, @getter_method_name.setter could be used.
    @dollars.setter
    def dollars(self, dollars):
        if dollars >= 0:
            self._cents = dollars * 100
        
money = Currency(100)
print(money.dollars)  # 100.0

money.dollars = -200
print(money.dollars)  # 100.0 - As the value provided is negative, it'll not update.

# Declare a PizzaPie class that accepts a total_slices parameter. 
# In the instantiation process for an object, assign the parameter to an 
# attribute with the same name. 

class PizzaPie():
    def __init__(self, total_slices):
        self.total_slices = total_slices
        self._slices_eaten = 0

    @property
    def slices_eaten(self):
        return self._slices_eaten
    
    @slices_eaten.setter
    def slices_eaten(self, slices_eaten):
        if slices_eaten < self.total_slices:
            self._slices_eaten = slices_eaten
    
    @property
    def percentage(self):
        return self._slices_eaten / self.total_slices
    
# A PizzaPie object should also be initialized with a _slices_eaten 
# protected attribute set to 0.

# Define a slices_eaten property.
# The getter method should retrieve the value of the _slices_eaten attribute. 
# The setter method should set a new value for the _slices_eaten attribute
# but only if the argument is less than total_slices.

# Define a percentage property that calculates how much of the pie has been eaten 
# (the number of slices eaten divided by the total slices available). 
# The percentage property should be read-only.

# See sample execution below
#
cheese = PizzaPie(8)
cheese.slices_eaten = 2
print(cheese.percentage) # 0.25
#
cheese.slices_eaten = 4
print(cheese.percentage) # 0.5
#
cheese.slices_eaten = 10 # _slices_eaten should not change because there's only 8 slices in pie
print(cheese.percentage) # 0.5
#
# ERROR - AttributeError: can't set attribute
# cheese.percentage = 0.50

# The property name and attribute name can’t be the same, otherwise the program will go into recursion.

# getattr and setattr functions: To get / set the value of attribute.

# getattr - Consists of 3 values (object of the class created, the attribute through which iteration will be done,
# mandatory value - if attribute not found)
# setattr - Used to create / set value of a dynamic attribute on an object, consists of 3 values (self, key, value)

stats = {
    "name": "Dominos",
    "price": 300,
    "size": "Large",
    "ingredients": ["Oregano", "Chilli Flakes", "Cheese"]
}

class Pizza():
    def __init__(self, stats):
        for key, value in stats.items():
            setattr(self, key, value)
    
Peri = Pizza(stats)
print(Peri.size)  # Large
print(Peri.ingredients)  # ['Oregano', 'Chilli Flakes', 'Cheese']

for attr in ["price", "size", "diameter", "location"]:
    print(getattr(Peri, attr, "Unknown"))

# O/p:
# 300
# Large
# Unknown
# Unknown

# hasattr and delattr: To check whether the mentioned attribute is present and if yes, delete it.

# hasattr(class's object, the iterable object)
# delattr(class's object, the iterable object)

stats = {
    "name": "Dominos",
    "price": 300,
    "size": "Large",
    "ingredients": ["Oregano", "Chilli Flakes", "Cheese"]
}

class Pizza():
    def __init__(self, stats):
        for key, value in stats.items():
            setattr(self, key, value)
    
Peri = Pizza(stats)

stats_delete = ["size", "diameter", "location"]

for item in stats_delete:
    if hasattr(Peri, item):
        delattr(Peri, item)

print(Peri.size)  # AttributeError: 'Pizza' object has no attribute 'size'

# Class methods: It is a method that is invoked directly on the class rather than an instance of it.
# The @classmethod decorator placed above a method in a class body designates it as a class method.

class SushiPlatter():
    def _init_(self, salmon, tuna, shrimp, squid):
        self.salmon = salmon
        self.tuna = tuna
        self.shrimp = shrimp
        self.squid = squid

    @classmethod
    def lunch_special_A(cls):
        return cls(salmon = 2, tuna = 2, shrimp = 2, squid = 0)

    @classmethod
    def tuna_lover(cls):
        return cls(salmon = 0, tuna = 10, shrimp = 0, squid = 1)

boris = SushiPlatter(salmon = 8, tuna = 4, shrimp = 5, squid = 10)
print(boris.salmon)  # 8

lunch_eater = SushiPlatter.lunch_special_A()
print(lunch_eater.salmon)  # 2
print(lunch_eater.squid)  # 0

tuna_fan = SushiPlatter.tuna_lover()
print(tuna_fan.tuna)  # 10

# Class attributes:

class Counter():
    count = 0
    
    def __init__(self):
        Counter.count += 1
        
print(Counter.count)  # 0
c1 = Counter()
print(Counter.count)  # 1

# To access the class variable 'count' within the __init__ instance method (methods which are defined inside a class),
# class_name.variable_name is to be used.

# When an object of the class is created, the __init__ method will be invoked and hence,
# the value of the 'count' variable gets updated.

class Counter():
    count = 0
    
    def __init__(self):
        Counter.count += 1
        
    @classmethod
    def counters(cls):
        two_counters = [cls(), cls()]
        print(f"New number of counters: {cls.count}")
        return two_counters
        
print(Counter.count)  # 0
c1 = Counter()

c2, c3 = Counter.counters()  # New number of counters: 3
print(Counter.count)  # 3

class Counter():
    count = 0
    
    def __init__(self):
        Counter.count += 1
        
    @classmethod
    def counters(cls):
        two_counters = [cls(), cls()]
        print(f"New number of counters: {cls.count}")
        next_two_counters = [cls(), cls()]
        print(f"Next new number of counters: {cls.count}")        
        return two_counters, next_two_counters
        
print(Counter.count)  # 0
c1 = Counter()

c2, c3 = Counter.counters()  # New number of counters: 3
                             # Next new number of counters: 5
print(Counter.count)  # 5

class Counter():
    count = 0
    
    def __init__(self):
        Counter.count += 1
        
    @classmethod
    def counters(cls):
        two_counters = [cls(), cls()]
        print(f"New number of counters: {cls.count}")
        next_two_counters = [cls(), cls()]
        print(f"Next new number of counters: {cls.count}")        
        return two_counters, next_two_counters
        
print(Counter.count)  # 0
c1 = Counter()

c2, c3 = Counter.counters()  # New number of counters: 3
                             # Next new number of counters: 5
c4 = Counter.counters()  # New number of counters: 7
                         # Next new number of counters: 9
print(Counter.count)  # 9

print(f"Value of c4: {c4}")  # Value of c4: ([<__main__.Counter object at 0x72fb2daa6b10>, <__main__.Counter object at 0x72fb2da9ce20>], [<__main__.Counter object at 0x72fb2da9c5a0>, <__main__.Counter object at 0x72fb2daef550>])
print(f"Value of c2: {c2}")  # Value of c2: [<__main__.Counter object at 0x72fb2daa91d0>, <__main__.Counter object at 0x72fb2daaa990>]
print(f"Value of c1: {c1}")  # Value of c1: <__main__.Counter object at 0x72fb2db72a50>

# Attribute lookup order: If the variable / attribute is not at the instance (object) level, Python will look at the class level.

class Example():
    data = "Class attribute !"

e1 = Example()
e2 = Example()

print(e1.data)  # Class attribute !
print(e2.data)  # Class attribute !

class Example():
    data = "Class attribute !"

e1 = Example()
e2 = e1.data

print(e1.data)  # Class attribute !
print(e2.data)  # AttributeError: 'str' object has no attribute 'data'

class Example():
    data = "Class attribute !"

e1 = Example()
e2 = e1.data

print(e1.data)  # Class attribute !
print(e2.upper())  # CLASS ATTRIBUTE !

class Example():
    data = "Class attribute !"

e1 = Example()
e2 = e1.data

print(e1.data)  # Class attribute !
print(e2)  # Class attribute !

class Example():
    data = "Class attribute !"

e1 = Example()
e2 = Example()

print(e1.data)  # Class attribute !

e1.data = "Instance attribute !!"
print(e1.data)  # Instance attribute !!
print(e2.data)  # Class attribute !

# Updating the variable at the instance level (here, e1),
# it’ll not affect the value of the same variable at the class level (here, e2).

# What is a static method ? How do you designate a method as a static method ?
# It is a helper method that is defined inside a class body but accepts neither the instance nor the class an argument.
# The @staticmethod decorator is placed above a method in the class body to designate it as a class method.

class Weather():
    def __init__(self, temp):
        self.temp = temp
        
    @staticmethod
    def calculate(fahr):
        answer = (5/9) * (fahr - 32)
        return round(answer, 2)
        
    def in_celsius(self):
        return [self.calculate(ans) for ans in self.temp]

f = Weather([100, 90, 80, 70, 60])
print(f.in_celsius())  # [37.78, 32.22, 26.67, 21.11, 15.56]
print(Weather.calculate(100))  # 37.78

# The 'calculate' method is defined as a static method, but it’s still accessible via the class.

# Magic Methods in Python:

# __str__ & __repr__: At first, it’ll look for __str__, if not found, then __repr__

class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"
        
    def __repr__(self):
        return f'Card("{self.rank}", "{self.suit}")'
        
c = Card('Ace', 'Spades')
print(c)  # Ace of Spades
print(str(c))  # Ace of Spades
print(repr(c))  # Card("Ace", "Spades")

# __eq__: For equality

class Student():
    def __init__(self, maths, history, writing):
        self.maths = maths
        self.history = history
        self.writing = writing
    
    @property
    def grades(self):
        return self.maths + self.history + self.writing
        
    def __eq__(self, other_student):
        return self.grades == other_student.grades
        
Bob = Student(maths = 100, history = 90, writing = 89)
Joe = Student(maths = 90, history = 100, writing = 89)
Elias = Student(maths = 50, history = 65, writing = 75)

print(Bob == Joe)  # True
print(Bob == Elias)  # False

# Part A: Instantiation

# Define a BusTrip class that has three parameters: destination, 
# bus_company, and cost. 
# In the instantiation process, assign these to attributes on the object.
# You may choose whether or not to utilize protected attributes.

# Part B: String Representation

# The __str__ representation of a BusTrip instance should be a string in this format:
#    "You paid 24.99 to Greyhound to go to Boston."
# In this scenario, "Boston" represents the destination, "Greyhound" the company, and 24.99 the price.
# These values should be passed as arguments when the BusTrip object is initialized.
    
# Part C: Equality

# Implement the __eq__ logic to compare two BusTrip objects.
# Two instances are considered equal if:
#   -- they share an identical destination
#   -- their prices have a difference of 3 dollars or less
# HINT: Utilize the built-in abs() function to determine the absolute value.

class BusTrip():
    def __init__(self, destination, company, price):
        self.destination = destination
        self.company = company
        self.price = price
        
    def __str__(self):
        return f"You paid {self.price} to {self.company} to go to {self.destination}."
    
    def __eq__(self, other_bustrip):
        return self.destination == other_bustrip.destination and abs(self.price - other_bustrip.price) <= 3

# Sample Execution
boston1 = BusTrip(destination = "Boston", company = "Greyhound", price = 24.99)
boston2 = BusTrip(destination = "Boston", company = "Megabus", price = 22.99)
boston3 = BusTrip(destination = "Boston", company = "Megabus", price = 49.99)
philly  = BusTrip(destination = "Philadelphia", company = "Peter Pan", price = 12.99)

print(boston1)            # You paid 24.99 to Greyhound to go to Boston.
print(boston1 == philly)  # False - destinations do not match
print(boston1 == boston2) # True - same destination and price within threshold
print(boston1 == boston3) # False - price difference exceeds threshold

# __doc__ method: To get the documentation for a specified module.

import math
print(math.__doc__)  # This module provides access to the mathematical functions defined by the C standard.

class Hello():
    def __init__(self):
        """
        Hello World !
        """
    
    def sleep(self):
        """
        Sleep !
        """
        
h1 = Hello()
print(h1.sleep.__doc__)  # Sleep !

# help(math) - To get the details of the whole module.

# __bool__: To get a boolean value.

class Emotion():
    def __init__(self, positivity, negativity):
        self.positivity = positivity
        self.negativity = negativity
        
    def __bool__(self):
        return self.positivity > self.negativity

my_emotion = Emotion(positivity = 100, negativity = 40)

if my_emotion:
    print("Nice")  # Nice

# Named Tuple: It's a type of tuple which allows access to the values via both index position and key / name.
# Used to create new classes objects, instantiated from named tuples hold attributes, but no instance methods.

import collections

GymExercise = collections.namedtuple('GymExercise', ['name', 'weight', 'reps'])

squat = GymExercise('squat', 265, 3)
bench = GymExercise('benchpress', 185, 5)
deadlift = GymExercise('deadlift', 225, 6)
press = GymExercise('press', 120, 8)

print(squat.reps)  # 3
print(squat[2])  # 3

# Indexing with the __getitem__ and __setitem__ methods: It’s for objects.

class CrayonBox():
    def __init__(self):
        self.crayons = []
    
    def add(self, crayon):
        self.crayons.append(crayon)
    
cb = CrayonBox()
cb.add('Blue')
cb.add('Red')

print(cb[0])  # TypeError: 'CrayonBox' object is not subscriptable

class CrayonBox():
    def __init__(self):
        self.crayons = []
    
    def add(self, crayon):
        self.crayons.append(crayon)
    
    def __getitem__(self, index):
        return self.crayons[index]
    
cb = CrayonBox()
cb.add('Blue')
cb.add('Red')

print(cb[0])  # Blue

class CrayonBox():
    def __init__(self):
        self.crayons = []
    
    def add(self, crayon):
        self.crayons.append(crayon)
    
    def __getitem__(self, index):
        return self.crayons[index]
    
    def __setitem__(self, index, value):
        self.crayons[index] = value
    
cb = CrayonBox()
cb.add('Blue')
cb.add('Red')

cb[0] = "Yellow"
print(cb[0])  # O/p: Yellow

# Define a Car class that accepts a maker (string), model (string),
# and year (number) parameters and assigns them to respective
# attributes

class Car():
    def __init__(self, maker, model, year):
        self.maker = maker
        self.model = model
        self.year = year
        
# Define a Dealership class. Each Dealership object should instantiate
# with a "cars" attribute set to an empty list.

class Dealership():
    def __init__(self):
        self.cars = []
        
    def accept_delivery(self, cars):
        self.cars.append(cars)
        
    def __getitem__(self, index):
        return self.cars[index]
        
    def __setitem__(self, index, new_value):
        self.cars[index] = new_value

# A Dealership object should have a accept_delivery instance method
# that accepts a Car object and adds it to the Dealership's internal
# "cars" list

# Indexing into a Dealership with a number should access a specific
# Car object in the Dealership.

# An index position in a Dealership should also be overwriteable
# with a new Car object (see examples below)

f150 = Car(maker = "Ford", model = "F-150", year = 2019)
camry = Car(maker = "Toyota", model = "Camry", year = 2020)
porsche = Car (maker = "Porsche", model = "911 Carrera", year = 2021)

dealership = Dealership()

dealership.accept_delivery(f150)
dealership.accept_delivery(camry)

print(dealership[0].year) # 2019 -- the F150's year

dealership[0] = porsche

for car in dealership:
  print(car.maker) # Porsche, Toyota

# __del__:

class Garbage():
    def __del__(self):
        print("This is my last breath!")
g = Garbage()  # This is my last breath!

# Declare a Newspaper class. 
class Newspaper():
    def __init__(self, pages, sections):
        self.pages = pages
        self.sections = sections
        
    def __len__(self):
        return self.pages
        
    def __getitem__(self, index):
        return self.sections[index]
        
    def __eq__(self, other):
        return self.pages == other.pages and len(self.sections) == len(other.sections)

# Each Newspaper will have a 'pages' attribute set to an integer 
# and a 'sections' attribute set to a dictionary.
# The keys in 'sections' will be strings representing a section (i.e. "Politics") 
# and the values will be the starting page for that section (i.e. "A5").

# The length of a newspaper should be equal to the number of pages it holds.

# Indexing the newspaper by a section should return the starting pasge for that section.

# Make it so two newspapers are considered equal if they have the 
# same number of pages AND the same number of sections

# EXAMPLE:
monday_sections = {
  "Politics": "A5",
  "Sports": "B2",
  "Entertainment": "C3"
}

tuesday_sections = {
  "Travel": "A5",
  "Cooking": "B2",
}

wednesday_sections = {
  "Classifieds": "A5",
  "Weddings": "B2",
  "Weather": "C3"
}

np1 = Newspaper(pages = 80, sections = monday_sections)
np2 = Newspaper(pages = 60, sections = tuesday_sections)
np3 = Newspaper(pages = 80, sections = wednesday_sections)

print(len(np1))        # 80
print(len(np2))        # 60
print(np1 == np2)      # False -- np1 has 3 sections while np2 has 2 sections
print(np1 == np3)      # True -- both have 80 pages and 3 sections
print(np1["Politics"]) # "A5"
print(np2["Cooking"])  # "B2"

# When should you use a class attribute ?
# A class attribute can be used whenever there is a piece of data that does not need to be copied among all objects.
# An example is a constant value that will not be changed or mutated.

# Difference between getattr and __getitem__:

# 1. __getattr__(self, name)
# This is a fallback method that Python invokes whenever an attribute is not located within the instance dictionary.
# When obj.something is requested, the system searches the object first; if it’s missing, __getattr__ is called.
# Best for: Managing dynamic attributes, proxying objects, or supporting legacy property names.
# Note: This differs from __getattribute__, which executes for every access attempt, regardless of the attribute's existence.

# 2. __getitem__(self, key)
# This magic method enables an instance to emulate a container, such as a dictionary or a list.
# Optimal for: Accessing elements by index or associating keys with specific data points.
# Utility: It provides the underlying logic that supports the square bracket [] syntax on your own objects.

class MyData:
    def __init__(self):
        self.existing = "I exist"

    def __getattr__(self, name):
        return f"Dynamic attribute: {name}"

    def __getitem__(self, key):
        return f"Container item: {key}"

obj = MyData()

# Attribute access
print(obj.existing)  # "I exist" (normal lookup, __getattr__ NOT called)
print(obj.missing)   # "Dynamic attribute: missing" (__getattr__ triggered)

# Index/Key access
print(obj["any_key"])  # "Container item: any_key" (__getitem__ triggered)

# get / set instance methods: To keep a value in the system with different metrics than the world. (Eg: User wants weight in kg, but the business needs to store the weight in gram).
# __getitem__ / __setitem__ methods: To get / update the values via the object created for a class.

# getattr / setattr: To get / set the value of attribute.
# getattr - Consists of 3 values (object of the class created, the attribute through which iteration will be done,
# mandatory value - if attribute not found)
# setattr - Used to create / set value of a dynamic attribute on an object, consists of 3 values (self, key, value)
