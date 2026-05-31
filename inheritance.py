# It's a design pattern in which a class inherits (receives) attributes and methods from one or more other classes.

# The class being inherited from is called the parent, superclass or base class.
# The class that inherits is called the child, subclass or derived class.

# Public (normal) and Protected (the one with an underscore at the start) attributes are inherited by the sub class.
# PRIVATE ATTRIBUTES (BEGIN WITH DOUBLE UNDERSCORES) ARE NOT INHERITED BY THE SUB CLASS.

class Store():
    def __init__(self):
        self.owner = "Girish"
    
    def det_1(self):
        return f"Hello {self.owner} !"

class Shop1(Store):
    pass

shop_1 = Shop1()

print(shop_1.owner)  # Girish
print(shop_1.det_1)  # <bound method Store.det_1 of <__main__.Shop1 object at 0x7f8b66c32f10>>

class Store():
    def __init__(self):
        self.owner = "Girish"
    
    def det_1(self):
        return f"Hello {self.owner} !"

class Shop1(Store):
    pass

shop_1 = Shop1()

print(shop_1.owner)  # Girish
print(shop_1.det_1())  # Hello Girish !

class Employee():
    def do_work(self):
        print("I'm working")
        
class Manager(Employee):
    def have_fun(self):
        print("This is a great time-pass")

class Director(Manager):
    def get_out(self):
        print("You've been fired")
        
e = Employee()
m = Manager()
d = Director()

e.have_fun()  # AttributeError: 'Employee' object has no attribute 'have_fun'

class Employee():
    def do_work(self):
        print("I'm working")
        
class Manager(Employee):
    def have_fun(self):
        print("This is a great time-pass")

class Director(Manager):
    def get_out(self):
        print("You've been fired")
        
e = Employee()
m = Manager()
d = Director()

m.do_work()  # I'm working

class Employee():
    def do_work(self):
        print("I'm working")
        
class Manager(Employee):
    def have_fun(self):
        print("This is a great time-pass")

class Director(Manager):
    def get_out(self):
        print("You've been fired")
        
e = Employee()
m = Manager()
d = Director()

d.do_work()  # I'm working
d.have_fun()  # This is a great time-pass

# Method overriding: If a class has a method with the same name as its super class method,
# it'll first use its own method and if not found, it'll go for the super class method.

class Employee():
    def do_work(self):
        print("I'm working")
    
    def go_for_lunch(self):
        print("Having lunch.")

class Manager(Employee):
    def have_fun(self):
        print("This is a great time-pass")
        
    def go_for_lunch(self):
        print("I had my lunch.")

class Director(Manager):
    def get_out(self):
        print("You've been fired")
        
e = Employee()
m = Manager()
d = Director()

m.go_for_lunch()  # I had my lunch.
d.go_for_lunch()  # I had my lunch.

class Animal():
    def __init__(self, name):
        self.name = name
    
    def eat_food(self, food):
        print(f"{self.name} is having {self.food}")
        
class Dog(Animal):
    pass

animal_1 = Dog()  # TypeError: __init__() missing 1 required positional argument: 'name'

class Animal():
    def __init__(self, name):
        self.name = name
    
    def eat_food(self, food):
        print(f"{self.name} is having {food}")
        
class Dog(Animal):
    pass

animal_1 = Dog("Tom")
animal_1.eat_food("Predigree")  # Tom is having Predigree

# super() keyword: If only one / specific number of sub-classes want some changes in their own class,
# but have to use the __init__ method of super class, super() keyword is used.

class Animal():
    def __init__(self, name):
        self.name = name
    
    def eat_food(self, food):
        print (f"{self.name} is having {food}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

animal_1 = Dog("Tom", "Doberman")
print(animal_1.name)  # Tom
print(animal_1.breed)  # Doberman

# When the name of the super class is updated, it needs to be updated in the sub class definition line within the parenthesis.
# To avoid this, the following could be implemented.

class Animal():
    def __init__(self, name):
        self.name = name
    
    def eat_food(self, food):
        print (f"{self.name} is having {food}")

ParentClass = Animal        
        
class Dog(ParentClass):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

animal_1 = Dog("Tom", "Doberman")
print(animal_1.name)  # Tom
print(animal_1.breed)  # Doberman

# Parent class name changed from Animal to Creature, no need to change everywhere instead of the alias link.

class Creature():
    def __init__(self, name):
        self.name = name
    
    def eat_food(self, food):
        print (f"{self.name} is having {food}")

ParentClass = Creature

class Dog(ParentClass):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

animal_1 = Dog("Tom", "Doberman")
print(animal_1.name)  # Tom
print(animal_1.breed)  # Doberman

class Musician():
    def __init__(self, name):
        self.name = name
        self.albums = []
    
    def release_album(self, string_1):
        return self.albums.append(string_1)

ParentClass = Musician

class Drummer(ParentClass):
    def __init__(self, name, stamina):
        super().__init__(name)
        self.stamina = stamina

d = Drummer(name = "Girish", stamina = 2)
print(d.name)  # Girish
print(d.stamina)  # 2
print(d.albums)  # []

d.release_album("Ride the Lightning")
print(d.albums)  # ['Ride the Lightning']

d.release_album("Master of Puppets")
print(d.albums)  # ['Ride the Lightning', 'Master of Puppets']

# Polymorphism: Multiple objects can react to the same method invocation.

class Pokemon():
    def __init__(self, name, special, health = 100):
        self.name = name
        self.special = special
        self.health = health
    
    def roar(self):
        print("Roarrrr")
        
    def damage_happen(self, level):
        self.health -= level
        
pookie_1 = Pokemon("Singer", "Water")
pookie_2 = Pokemon("Dancer", "Energy", health = 110)

pookie_1.roar()  # Roarrrr
pookie_2.roar()  # Roarrrr

pookie_1.damage_happen(20)
pookie_2.damage_happen(20)

print(pookie_1.health)  # 80
print(pookie_2.health)  # 90

values = [
    "Girish",
    [1, 2, 3],
    (4, 5, 6, 7),
    {"a": 1, "b": 2}
]
for value in values:
    print(len(value))

# O/p:
# 6
# 3
# 4
# 2

class Person():
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def __len__(self):
        return self.height
    
values = [
    "Girish",
    [1, 2, 3],
    (4, 5, 6, 7),
    {"a": 1, "b": 2},
    Person("Girish", 51)
]
for value in values:
    print(len(value))

# O/p:
# 6
# 3
# 4
# 2
# 51

import random

class Player():
    def __init__(self, games_played, victories):
        self.games_played = games_played
        self.victories = victories
        
    def win_ratio(self):
        return self.victories / self.games_played
        
class HumanPlayer(Player):
    def make_move(self):
        print("Human")
        
class ComputerPlayer(Player):
    def make_move(self):
        print("Computer")
        
hp = HumanPlayer(30, 15)
cp = ComputerPlayer(1000, 800)

print(hp.win_ratio())  # 0.5
print(cp.win_ratio())  # 0.8

game_players = [hp, cp]

starting_player = random.choice(game_players)
starting_player.make_move()  # Human

# In this exercise, we'll be modelling a routine for proper dental health,
# which includes brushing our teeth, flossing, and using mouthwash.
# The order of these three varies from person to person.

# Declare a DentalHealthItem class. Its initialization should set a "price"
# attribute.

import random

class DentalHealthItem():
    def __init__(self, price):
        self.price = price

# Declare a Toothbrush subclass that inherits from DentalHealthItem.
# On it, define a "use" instance method that returns "Brushing the teeth"

ParentClass = DentalHealthItem

class Toothbrush(ParentClass):
    def use(self):
        return "Brushing the teeth"

# Declare a Floss subclass that inherits from DentalHealthItem.
# On it, define a "use" instance method that returns "Flossing the teeth"

class Floss(ParentClass):
    def use(self):
        return "Flossing the teeth"

# Declare a Mouthwash subclass that inherits from DentalHealthItem.
# On it, define a "use" instance method that returns "Washing the teeth"

class Mouthwash(ParentClass):
    def use(self):
        return "Washing the teeth"

# Instantiate an instance of a Toothbrush and assign it a "toothbrush" variable.
# Instantiate an instance of a Floss and assign it a "floss" variable.
# Instantiate an instance of a Mouthwash and assign it a "mouthwash" variable.

toothbrush = Toothbrush(price = 5)
floss = Floss(price = 7)
mouthwash = Mouthwash(price = 10)

# Declare a "dental_health_kit" variable. It should be a list that stores the three objects.

dental_health_kit = [toothbrush, floss, mouthwash]

# Import the "random" module (see last lesson for reference). 
# Invoke the "shuffle" function from the module, passing in the dental_health_kit list. 
# This will mutate the list, randomizing the order of its elements.

random.shuffle(dental_health_kit)

# Use list comprehension to invoke the "use" method on all three objects in "dental_health_kit".
# Assign the resulting list of strings to an "actions" variable.

actions = [step.use for step in dental_health_kit]
print(actions)  # [<bound method Mouthwash.use of <__main__.Mouthwash object at 0x7d6350307380>>, <bound method Floss.use of <__main__.Floss object at 0x7d63503074d0>>,
                # <bound method Toothbrush.use of <__main__.Toothbrush object at 0x7d6350306a50>>]
                # (The instance method “use” is only passed, not invoked).

actions = [step.use() for step in dental_health_kit]
print(actions)  # ['Brushing the teeth', 'Washing the teeth', 'Flossing the teeth']

# Name Mangling for Privacy: Double underscore is used to make an object’s attribute mangle.
# Use if the subclass is going to accidentally overwrite something in the superclass and break the API.

class Nonsense():
    def __init__(self):
        self.__some_attribute = "Hello"
        
    def __some_method(self):
        print("This is coming from the __some_method !")

ParentClass = Nonsense       
class AnotherNonsense(ParentClass):
    pass

n = Nonsense()
an = AnotherNonsense()

n.__some_attribute  # AttributeError: 'Nonsense' object has no attribute '__some_attribute'

class Nonsense():
    def __init__(self):
        self.__some_attribute = "Hello"
        
    def __some_method(self):
        print("This is coming from the __some_method !")
        
class AnotherNonsense(Nonsense):
    pass

n = Nonsense()
an = AnotherNonsense()

# n.__some_attribute

# object._ClassName__attribute_name / object._ClassName__instance_method_name
print(n._Nonsense__some_attribute)  # Hello
print(an._Nonsense__some_attribute)  # Hello
an._Nonsense__some_method()  # This is coming from the __some_method !

# Multiple Inheritance: To inherit from more than one super class.
# If both the super classes have a method with the same name, it’ll check for the order it is fed into the subclass.

class School():
    def grades(self, grade):
        print(f"You've got {grade} grade")
    
    def distance(self):
        print("What is the distance to school ?")
        
class College():
    def professor(self):
        print("Who is the professor for this subject ?")
        
    def distance(self):
        print("What is the distance to college ?")
        
class Student(School, College):
    pass

student = Student()
student.distance()  # What is the distance to school ?

class School():
    def grades(self, grade):
        print(f"You've got {grade} grade")
    
    def distance(self):
        print("What is the distance to school ?")
        
class College():
    def professor(self):
        print("Who is the professor for this subject ?")
        
    def distance(self):
        print("What is the distance to college ?")
        
class Student(College, School):
    pass

student = Student()
student.distance()  # What is the distance to college ?

# MRO (Method Resolution Order): It means the order in which Python resolves which method will be called / invoked.

print(Student.mro())  # [<class '__main__.Student'>, <class '__main__.College'>, <class '__main__.School'>, <class 'object'>]

# 2 ways of searching - DFS (Depth First Search) and BFS (Breadth First Search)
# By default, Python uses DFS (Depth First Search)

class Restaurant():
    def make_reservations(self, party_size):
        print(f"Booked a table for {party_size}")
        
class Steakhouse(Restaurant):
    pass

class Bar():
    def make_reservations(self, party_size):
        print(f"Booked a lounge for {party_size}")
        
class BarAndGrill(Steakhouse, Bar):
    pass

bag = BarAndGrill()
bag.make_reservations(2)  # Booked a table for 2

class Restaurant():
    def make_reservations(self, party_size):
        print(f"Booked a table for {party_size}")
        
class Steakhouse(Restaurant):
    pass

class Bar():
    def make_reservations(self, party_size):
        print(f"Booked a lounge for {party_size}")
        
class BarAndGrill(Bar, Steakhouse):
    pass

bag = BarAndGrill()
bag.make_reservations(2)  # Booked a lounge for 2

# Diamond-Shaped inheritance - If we see two or more occurrences of the same super class in the search priority,
# Python will remove all the earlier occurrences of the class and will keep the latest one.

class FilmMaker():
    def give_interview(self):
        print("I love making movies")
        
class Director(FilmMaker):
    pass

class ScreenWriter(FilmMaker):
    def give_interview(self):
        print("I love writing scripts")
        
class JackOfAllTrades(Director, ScreenWriter):
    pass

jack = JackOfAllTrades()
jack.give_interview()  # I love writing scripts
print(JackOfAllTrades.mro())  # [<class '__main__.JackOfAllTrades'>, <class '__main__.Director'>,
                              # <class '__main__.ScreenWriter'>, <class '__main__.FilmMaker'>, <class 'object'>]

# isinstance: To check whether an object belongs to a class mentioned in the second argument.

print(isinstance(1, int))  # True
print(isinstance("Hello", str))  # True
print(isinstance([], (list, dict, str)))  # True

class Person():
    pass

class Superhero(Person):
    pass

P = Person()
S = Superhero()

print(isinstance(P, Person))  # True
print(isinstance(P, Superhero))  # False
print(isinstance(S, Person))  # True
print(isinstance(S, Superhero))  # True

# issubclass: To check whether the first mentioned class is a sub class of the second mentioned class.

class Person():
    pass

class Superhero(Person):
    pass

P = Person()
S = Superhero()

print(issubclass(Superhero, Person))  # True
print(issubclass(Person, Superhero))  # False

# Composition: Composition is a design pattern where an object stores another object as an attribute.
# That way, a specific responsibility can be delegated to a separate object.
# Many developers argue this leads to more stable architecture than using inheritance.

class Engine():
    def __init__(self, horse_power):
        self.horse_power = horse_power
    
class Wheel():
    def __init__(self, size):
        self.size = size
        
class Car():
    def __init__(self, make, model, power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(power)
        self.wheels = [Wheel(wheel_size) for _ in range(4)]
        
    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power} (hp) {self.wheels[0].size} (in)"

car1 = Car(make='Aston Martin', model='DB5', power = 500, wheel_size = 20)
car2 = Car(make='BMW', model='M4', power = 485, wheel_size = 20)

print(car1.display_car())  # Aston Martin DB5 500 (hp) 20 (in)
print(car2.display_car())  # BMW M4 485 (hp) 20 (in)
