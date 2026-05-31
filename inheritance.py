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


