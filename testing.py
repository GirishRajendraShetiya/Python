# What is testing ?
# The goal of testing is writing code that validates the functionality of other code.
# Tests prevent regression. A regression is when a feature that used to work no longer does.

# Terms:
# 1. A test suite is a collection of tests that target related functionality.
# 2. Code coverage or test coverage refers to the percentage of the codebase that is tested by tests.

# In practice, no program is 100 % accurate, there are always some flaws.
# The goal is to test the most important part of the business applications.

# assert statement: Used to validate if a condition in the program is True (it'll return nothing),
# if not, an Assertion error will be raised.

def add(x, y):
    assert isinstance(x, int) and isinstance(y, int), "Both of the provided numbers should belong to the <int> class"
    return x + y

print(add(3, "5"))

# O/p:
# Traceback (most recent call last):
#   File "/home/repl668/main.py", line 5, in <module>
#     print(add(3, "5"))
#           ^^^^^^^^^^^
#   File "/home/repl668/main.py", line 2, in add
#     assert isinstance(x, int) and isinstance(y, int), "Both of the provided numbers should belong to the <int> class"
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# AssertionError: Both of the provided numbers should belong to the <int> class
# ** Process exited - Return Code: 1 **

# doctest module: To validate the changes written in the documented string with the written code.

def sum_of_list(numbers):
    """
    >>> sum_of_list([1, 2, 3])
    6
    >>> sum_of_list([3, 6, 10])
    19
    """
    total = 0
    for num in numbers:
        total += num
    return num

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# O/p:
# **********************************************************************
# File "/home/repl807/main.py", line 3, in __main__.sum_of_list
# Failed example:
#     sum_of_list([1, 2, 3])
# Expected:
#     6
# Got:
#     3
# **********************************************************************
# File "/home/repl807/main.py", line 5, in __main__.sum_of_list
# Failed example:
#     sum_of_list([3, 6, 10])
# Expected:
#     19
# Got:
#     10
# **********************************************************************
# 1 items had failures:
#    2 of   2 in __main__.sum_of_list
# ***Test Failed*** 2 failures.
# ** Process exited - Return Code: 0 **

def sum_of_list(numbers):
    """
    >>> sum_of_list([1, 2, 3])
    6
    >>> sum_of_list([3, 6, 10])
    19
    """
    total = 0
    for num in numbers:
        total += num
    return total

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# O/p: ** Process exited - Return Code: 0 ** (The return is carrying the correct variable)

# In this, it'll keep double quotes and single quotes as different.

# unittest module: To test / validate a chunk / unit (a class, a function, a module) of code.

import unittest
class TestString(unittest.TestCase):
    def test_split(self):
        pass

if __name__ == "__main__":
    unittest.main()

# O/p:
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.001s
# OK
# ** Process exited - Return Code: 0 **

# assertEqual method: In the bracket, first term is the operation that needs to be performed by the system
# and second is the expected output.

import unittest
class TestString(unittest.TestCase):
    def test_split(self):
        self.assertEqual("a-b-c".split("-"), ["a", "b", "c"])

if __name__ == "__main__":
    unittest.main()

# O/p:
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
# OK
# ** Process exited - Return Code: 0 **

# A single dot at the start in the output means a single test has been ran and it was successful

import unittest
class TestString(unittest.TestCase):
    def test_split(self):
        self.assertEqual("a-b-c".split("-"), ["a-", "b-", "c"])

if __name__ == "__main__":
    unittest.main()

# O/p:
# F
# ======================================================================
# FAIL: test_split (__main__.TestString.test_split)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/repl789/main.py", line 5, in test_split
#     self.assertEqual("a-b-c".split("-"), ["a-", "b-", "c"])
# AssertionError: Lists differ: ['a', 'b', 'c'] != ['a-', 'b-', 'c']

# First differing element 0:
# 'a'
# 'a-'

# - ['a', 'b', 'c']
# + ['a-', 'b-', 'c']
# ?    +     +

# ----------------------------------------------------------------------
# Ran 1 test in 0.001s
# FAILED (failures=1)
# ** Process exited - Return Code: 1 **

import unittest
class TestString(unittest.TestCase):
    def test_split(self):
        self.assertEqual("a-b-c".split("-"), ["a", "b", "c"])
        
    def test_count(self):
        self.assertEqual("beautiful".count("u"), 2)

if __name__ == "__main__":
    unittest.main()

# O/p:
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
# OK
# ** Process exited - Return Code: 0 **

# The name of the instance methods created in our class should start with 'test', nothing other than that.
# In the case of unit test, it’ll NOT crash the code while testing, but in assert, it'll.

# Skipping test: To focus on a specific part of a code, the tests for the other parts need to be skipped.
# It's to be used only for development.

import unittest
class TestString(unittest.TestCase):
    def test_split(self):
        self.assertEqual("a-b-c".split("-"), ["a", "b", "c"])
        
    def test_count(self):
        pass

if __name__ == "__main__":
    unittest.main()

# O/p:
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
# OK
# ** Process exited - Return Code: 0 **

# It ran 2 tests, even when the 2nd test has nothing, it's a false positive

import unittest
class TestString(unittest.TestCase):
    def test_split(self):
        self.assertEqual("a-b-c".split("-"), ["a", "b", "c"])
        
    @unittest.skip("To be implemented later")
    def test_count(self):
        pass

if __name__ == "__main__":
    unittest.main()

# O/p:
# s.
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
# OK (skipped=1)
# ** Process exited - Return Code: 0 **

# The output represents the test which is skipped

# assertNotEqual method: Complement to assertEqual method.

import unittest
class TestString(unittest.TestCase):
    def test_equality(self):
        self.assertNotEqual(1, 2)
        self.assertNotEqual([1, 2], [2, 1])
        self.assertNotEqual(True, False)
        
if __name__ == "__main__":
    unittest.main()

# O/p:
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
# OK
# ** Process exited - Return Code: 0 **

import unittest
def copy_and_add_element(values, element):
    copy = values[:]
    copy.append(element)
    return copy

class TestString(unittest.TestCase):
    def test_equality(self):
        self.assertNotEqual(1, 2)
        self.assertNotEqual([1, 2], [2, 1])
        self.assertNotEqual(True, False)
        

    def test_copy_and_add_element(self):
        values = [1, 2, 3]
        result = copy_and_add_element(values, 4)
        
        self.assertEqual(result, [1, 2, 3, 4])
        
        self.assertNotEqual(
            values,
            [1, 2, 3, 4],
            "The copy_and_add_element function is mutating the original list, kindly validate the code once."
            )
        
if __name__ == "__main__":
    unittest.main()

# O/p:
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
# OK
# ** Process exited - Return Code: 0 **

# The output will not represent the highlighted statement as all the test cases passed

# copy = values (Not mentioning the [:] will generate an error)

# F.
# ======================================================================
# FAIL: test_copy_and_add_element (__main__.TestString.test_copy_and_add_element)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/repl118/main.py", line 20, in test_copy_and_add_element
#     self.assertNotEqual(
# AssertionError: [1, 2, 3, 4] == [1, 2, 3, 4] : The copy_and_add_element function is mutating the original list, kindly validate the code once.
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
# FAILED (failures=1)
# ** Process exited - Return Code: 1 **

# assertIs and assertIsNot methods: To validate identity of an object.

import unittest
class IdentityTest(unittest.TestCase):
    def test_identity_check(self):
        a = [1, 2, 3]
        b = a
        c = [1, 2, 3]
        
        self.assertEqual(a, b)
        self.assertEqual(b, c)

        self.assertIs(a, b)
        self.assertIsNot(b, c)
        self.assertIsNot(a, c)

if __name__ == "__main__":
    unittest.main()

# O/p:
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
# OK
# ** Process exited - Return Code: 0 **

# assertTrue and assertFalse methods:

import unittest
class TrueFalseTest(unittest.TestCase):
    def test_truth(self):
        self.assertTrue(3 < 5)
    
    def test_false(self):
        self.assertFalse(4 < 2)
        self.assertFalse([])
        self.assertFalse({})
        # self.assertFalse([{}])

if __name__ == "__main__":
    unittest.main()

# O/p:
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
# OK
# ** Process exited - Return Code: 0 **

import unittest
class TrueFalseTest(unittest.TestCase):
    def test_truth(self):
        self.assertTrue(3 < 5)
    
    def test_false(self):
        self.assertFalse(4 < 2)
        self.assertFalse([])
        self.assertFalse({})
        self.assertFalse([{}])

if __name__ == "__main__":
    unittest.main()

# O/p:
# F.
# ======================================================================
# FAIL: test_false (__main__.TrueFalseTest.test_false)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/repl604/main.py", line 11, in test_false
#     self.assertFalse([{}])
# AssertionError: [{}] is not false
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
# FAILED (failures=1)
# ** Process exited - Return Code: 1 **

# assertIsNone and assertIsNotNone methods:

import unittest
def explicit_return_sum(a, b):
    return a + b

def implicit_return_sum(c, d):
    return c + d

class TestNone(unittest.TestCase):
    def test_none_not_none(self):
        self.assertIsNone(implicit_return_sum(3, 5))
        self.assertIsNotNone(explicit_return_sum(10, 4))

if __name__ == "__main__":
    unittest.main()

# O/p:
# F
# ======================================================================
# FAIL: test_none_not_none (__main__.TestNone.test_none_not_none)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/repl663/main.py", line 11, in test_none_not_none
#     self.assertIsNone(implicit_return_sum(3, 5))
# AssertionError: 8 is not None
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
# FAILED (failures=1)
# ** Process exited - Return Code: 1 **

import unittest
def explicit_return_sum(a, b):
    return a + b

def implicit_return_sum(c, d):
    print(c + d)

class TestNone(unittest.TestCase):
    def test_none_not_none(self):
        self.assertIsNone(implicit_return_sum(3, 5))
        self.assertIsNotNone(explicit_return_sum(10, 4))

if __name__ == "__main__":
    unittest.main()

# O/p:
# 8
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
# OK
# ** Process exited - Return Code: 0 **

# assertIn and assertNotIn methods:

import unittest
class InclusionTests(unittest.TestCase):
    def test_inclusion(self):
        # self.assertTrue("k" in "king")
        
        self.assertIn("k", "king")
        self.assertIn(1, [1, 2, 3])
        self.assertIn(5, (6, 5, 7))
        self.assertIn("a", { "a": 1, "b": 2})
        self.assertIn("a", { "a": 1, "b": 2}.keys())
        self.assertIn(2, { "a": 1, "b": 2}.values())
        self.assertIn(55, range(50, 59))
    
    def test_not_inclusion(self):
        # self.assertTrue("k" in "king")
        
        self.assertNotIn("w", "king")
        self.assertNotIn(5, [1, 2, 3])
        self.assertNotIn(15, (6, 5, 7))
        self.assertNotIn("aa", { "a": 1, "b": 2})
        self.assertNotIn("aa", { "a": 1, "b": 2}.keys())
        self.assertNotIn(21, { "a": 1, "b": 2}.values())
        self.assertNotIn(5, range(50, 59))

if __name__ == "__main__":
    unittest.main()

# O/p:
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
# OK
# ** Process exited - Return Code: 0 **

# assertIsInstance and assertNotIsInstance methods:

import unittest
class ObjectTypeTests(unittest. TestCase):
    def test_is_instance(self):
        self.assertIsInstance(1, int)
        self.assertIsInstance(8.765, float)
        self.assertIsInstance([], list)
        self.assertIsInstance({ "a": 1 }, dict)

        # self.assertIsInstance({ "a": 1 }, list)

    def test_not_is_instance(self):
        self.assertNotIsInstance(5, list)
        self.assertNotIsInstance(5, float)
        self.assertNotIsInstance(5, set)
        self.assertNotIsInstance(5, dict)

        # self.assertNotIsInstance(5, int)

if __name__ == "__main__":
    unittest.main()

# O/p:
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
# OK
# ** Process exited - Return Code: 0 **

# assertRaises method:

import unittest
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError
    return x / y

class DivideTestCase(unittest.TestCase):
    def test_divide(self):
        self.assertRaises(ZeroDivisionError, divide, 10, 5)

if __name__ == "__main__":
    unittest.main()

# O/p:
# F
# ======================================================================
# FAIL: test_divide (__main__.DivideTestCase.test_divide)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/repl406/main.py", line 10, in test_divide
#     self.assertRaises(ZeroDivisionError, divide, 10, 5)
# AssertionError: ZeroDivisionError not raised by divide
# ----------------------------------------------------------------------
# Ran 1 test in 0.001s
# FAILED (failures=1)
# ** Process exited - Return Code: 1 **

import unittest
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError
    return x / y

class DivideTestCase(unittest.TestCase):
    def test_divide(self):
        self.assertRaises(ZeroDivisionError, divide, 10, 0)

if __name__ == "__main__":
    unittest.main()

# O/p:
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
# OK
# ** Process exited - Return Code: 0 **

# In both the above scenarios, the divide function is passed to the assertRaises method
# as an argument with its inputs as 10 & 0, 5 respectively.

import unittest
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError
    return x / y

class DivideTestCase(unittest.TestCase):
    def test_divide(self):
        self.assertRaises(ZeroDivisionError, divide, 10, 0)
        
    def test_divide_another_way(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

if __name__ == "__main__":
    unittest.main()

# O/p:
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s
# OK
# ** Process exited - Return Code: 0 **

# setUp and tearDown methods: It runs before and after every test.

import unittest
class Address():
    def __init__(self, city, state):
        self.city = city
        self.state = state

class Owner():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Restaurant():
    def __init__(self, address, owner):
        self.address = address
        self.owner = owner

    @property
    def owner_age(self):
        return self.owner.age

    def summary(self):
        return f"This restaurant is owned by {self.owner.name} and is located in {self.address.city}."

class TestRestaurant(unittest.TestCase):
    def setUp(self):
        print("This will run before each test!")
        address = Address(city = "New York", state = "New York")
        owner = Owner(name = "Jackie", age = 60)
        self.golden_palace = Restaurant(address, owner)

    def tearDown(self):
        print("This will run after each test!")

    def test_owner_age(self):
        self.assertEqual(self.golden_palace.owner_age, 60)

    def test_summary(self):
        self.assertEqual(
        self.golden_palace.summary(), "This restaurant is owned by Jackie and is located in New York."
        )

if __name__ == "__main__":
    unittest.main()

# O/p:
# This will run before each test!
# This will run after each test!
# This will run before each test!
# This will run after each test!
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
# OK
# ** Process exited - Return Code: 0 **

# setUpClass and tearDownClass methods: They run once before and after all the tests.
# Used mostly for a database connection.

import unittest
class TestOperations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("This will run ONCE before the test suite starts")

    def setUp(self):
        print("This will run before EACH test")

    def tearDown(self):
        print("This will run after EACH test")

    @classmethod
    def tearDownClass(cls):
        print("This will run ONCE after the test suite finishes")

    def test_stuff(self):
        self.assertEqual(1, 1)

    def test_more_stuff(self):
        self.assertEqual([], [])

if __name__ == "__main__":
    unittest.main()

# O/p:
# This will run ONCE before the test suite starts
# This will run before EACH test
# This will run after EACH test
# This will run before EACH test
# This will run after EACH test
# This will run ONCE after the test suite finishes
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
# OK
# ** Process exited - Return Code: 0 **

# Mocking: An object that takes the place of another object in a test.

from unittest.mock import Mock

pizza = Mock()
print(pizza)  # <Mock id='140011661912656'>
print(type(pizza))  # <class 'unittest.mock.Mock'>

pizza.size = "Large"
pizza.price = 19.99
pizza.toppings = ["Pepperoni", "Mushroom", "Sausage"]

print(pizza.size)  # Large
print(pizza.price)  # 19.99
print(pizza.toppings)  # ["Pepperoni", "Mushroom", "Sausage"]

print(pizza.anything)  # <Mock name='mock.anything' id='140011661912608'>
print(pizza.nonsense)  # <Mock name='mock.nonsense' id='140011657354448'>

# The attributes anything and nonsense got created due to Mock

print(pizza.anything)  # <Mock name='mock.anything' id='140156312249616'>
print(pizza.anything)  # <Mock name='mock.anything' id='140156312249616'>

# After the creation of the attribute at the first time, it’ll return the same ID everytime

print(pizza.cover_with_cheese())  # <Mock name='mock.cover_with_cheese()' id='140524827929984'>
print(pizza.cover_with_cheese())  # <Mock name='mock.cover_with_cheese()' id='140524827929984'>

# Mock methods could also be created

from unittest.mock import Mock

pizza = Mock()
print(pizza)  # <Mock id='139825800227024'>
print(type(pizza))  # <class 'unittest.mock.Mock'>

pizza.configure_mock(
    size = "Large",
    price = 19.99,
    toppings = ["Pepperoni", "Mushroom", "Sausage"]
)
# pizza.size = "Large"
# pizza.price = 19.99
# pizza.toppings = ["Pepperoni", "Mushroom", "Sausage"]

print(pizza.size)  # Large
print(pizza.price)  # 19.99
print(pizza.toppings)  # ['Pepperoni', 'Mushroom', 'Sausage']

# return_value attribute:

from unittest.mock import Mock

mock = Mock()

print(mock)  # <Mock id='140438550992688'>
print(mock())  # <Mock name='mock()' id='140438548382592'>

# Both the above highlighted print statements are different as they’re having different mock IDs

from unittest.mock import Mock

mock = Mock()
mock.return_value = mock  # Tell the mock to return itself

print(mock)    # <Mock id='...'>  <Mock id='140220933789008'>
print(mock())  # <Mock id='...'> (The IDs will now match!)  <Mock id='140220933789008'>

from unittest.mock import Mock

mock = Mock()

print(mock.return_value)  # <Mock name='mock()' id='139710951955760'>
print(mock())  # <Mock name='mock()' id='139710951955760'>

# Both the above highlighted print statements are the same as they’re having the same mock IDs

from unittest.mock import Mock

mock = Mock()

mock.return_value = 25
print(mock())  # 25 (return_value is same as ())

from unittest.mock import Mock

mock = Mock()

mock.return_value = 25
print(mock())  # 25

stuntman = Mock()
stuntman.jump_off_building.return_value = "Oh No ! My legs"
stuntman.light_on_fire.return_value = "Rapid Fire"

print(stuntman.jump_off_building)  # <Mock name='mock.jump_off_building' id='140099592105392'>

from unittest.mock import Mock

mock = Mock()

mock.return_value = 25
print(mock())  # 25

stuntman = Mock()
stuntman.jump_off_building.return_value = "Oh No ! My legs"
stuntman.light_on_fire.return_value = "Rapid Fire"

print(stuntman.jump_off_building())  # Oh No ! My legs

# When a consistent value is to be returned, return_value can be used,
# but for dynamic, side_effect needs to be used.

# side_effect attribute:

from unittest.mock import Mock
from random import randint

def generate_number():
    return randint(1, 10)

call_me_maybe = Mock()
print(call_me_maybe.side_effect)  # None

call_me_maybe.side_effect = generate_number
print(call_me_maybe())  # 9
print(call_me_maybe())  # 7
print(call_me_maybe())  # 8

from unittest.mock import Mock
from random import randint

def generate_number():
    return randint(1, 10)

call_me_maybe = Mock(side_effect = generate_number)

print(call_me_maybe())  # 7
print(call_me_maybe())  # 1
print(call_me_maybe())  # 9

from unittest.mock import Mock
from random import randint

def generate_number():
    return randint(1, 10)

call_me_maybe = Mock(return_value = 10, side_effect = generate_number)

print(call_me_maybe())  # 8
print(call_me_maybe())  # 2
print(call_me_maybe())  # 10

# Even if both the return_value and side_effect are given at a time, side_effect will win

from unittest.mock import Mock

three_item_list = Mock()
three_item_list.pop.side_effect = [3, 2, 1, IndexError("pop from empty list")]

print(three_item_list.pop())  # 3
print(three_item_list.pop())  # 2
print(three_item_list.pop())  # 1
print(three_item_list.pop())  # IndexError: pop from empty list

mock = Mock(side_effect = NameError("Some error message"))
# mock()

from unittest.mock import Mock

three_item_list = Mock()
three_item_list.pop.side_effect = [3, 2, 1, IndexError("pop from empty list")]

print(three_item_list.pop())  # 3
print(three_item_list.pop())  # 2
print(three_item_list.pop())  # 1
# print(three_item_list.pop())

mock = Mock(side_effect = NameError("Some error message"))
mock()  # NameError: Some error message

# Let's mock a fake Airport object.
# Create a Mock object and assign it to a variable called 'airport'. 

from unittest.mock import Mock

airport = Mock()

# The airport mock should have a 'gates' attribute set to a list of the strings “A1”, “B2”, and “C3”.

airport.gates = ["A1", "B2", "C3"]

# The airport mock should have a 'departures' attribute set to a dictionary where 
# the keys are strings representing cities and the 
# values are strings representating their departure times.

airport.departures = {
  "Atlanta": "12:00PM",
  "Nashville": "04:30PM"
}

# The airport mock should have a 'close' attribute that is callable (i.e. an instance method). 
# When invoked, it should return the string “Closing”.

airport.close.return_value = "Closing"

# The airport should have an 'open' attribute that is callable (i.e. an instance method). .
# When invoked the first time, it should return “Opening…”. 
# When invoked the second time, it should return “Already open”.

airport.open.side_effect = ["Opening...", "Already open"]

# EXAMPLE
#
# Given an airport Mock...
#
print(airport.gates)      # ["A1", "B2", "C3"]
print(airport.departures) # { "Atlanta": "12:00PM", "Nashville": "04:30PM" }
print(airport.close())    # Closing
print(airport.open())     # Opening...
print(airport.open())     # Already open

# MagicMock objects: It supports the magic methods (dunder methods), unlike the Mock object,
# which can't support these types of methods.

from unittest.mock import Mock, MagicMock
plain_mock = Mock()
magic_mock = MagicMock()

print(len(magic_mock))  # 0
print(len(plain_mock))  # TypeError: object of type 'Mock' has no len()

# MagicMock object also supports indexing, while the Mock object doesn't.

from unittest.mock import Mock, MagicMock
plain_mock = Mock()
magic_mock = MagicMock()

print(magic_mock[3])  # <MagicMock name='mock.__getitem__()' id='139633804934032'>
print(plain_mock[3])  # TypeError: 'Mock' object is not subscriptable

from unittest.mock import Mock, MagicMock
plain_mock = Mock()
magic_mock = MagicMock()

print(len(magic_mock))  # 0
# print(magic_mock[3])
# print(plain_mock[3])

magic_mock.__len__.return_value = 50
print(len(magic_mock))  # 50

# MagicMock calls:

import unittest
from unittest.mock import MagicMock

class MockTest(unittest.TestCase):
    def test_mock(self):
        mock = MagicMock()
        mock()
        mock.assert_called()

    def test_mock_not_called(self):
        mock = MagicMock()
        mock()
        mock.assert_not_called()

if __name__ == "__main__":
    unittest.main()

# O/p:
# .F
# ======================================================================
# FAIL: test_mock_not_called (__main__.MockTest.test_mock_not_called)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/repl500/main.py", line 13, in test_mock_not_called
#     mock.assert_not_called()
#   File "/usr/lib/python3.12/unittest/mock.py", line 910, in assert_not_called
#     raise AssertionError(msg)
# AssertionError: Expected 'mock' to not have been called. Called 1 times.
# Calls: [call()].
# ----------------------------------------------------------------------
# Ran 2 tests in 0.004s
# FAILED (failures=1)
# ** Process exited - Return Code: 1 **

import unittest
from unittest.mock import MagicMock

class MockTest(unittest.TestCase):
    def test_mock(self):
        mock = MagicMock()
        mock()
        mock.assert_called()

    def test_mock_not_called(self):
        mock = MagicMock()
        mock.assert_not_called()

if __name__ == "__main__":
    unittest.main()

# O/p:
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.050s
# OK
# ** Process exited - Return Code: 0 **

import unittest
from unittest.mock import MagicMock

class MockTest(unittest.TestCase):
    def test_mock(self):
        mock = MagicMock()
        mock()
        mock.assert_called()

    def test_mock_not_called(self):
        mock = MagicMock()
        mock.assert_not_called()
        
    def test_called_with(self):
        mock = MagicMock()
        mock(1, 2, 3)
        mock.assert_called_with(1, 2, 3)

if __name__ == "__main__":
    unittest.main()

# O/p:
# ...
# ----------------------------------------------------------------------
# Ran 3 tests in 0.003s
# OK
# ** Process exited - Return Code: 0 **

import unittest
from unittest.mock import MagicMock

class MockTest(unittest.TestCase):
    def test_mock(self):
        mock = MagicMock()
        mock()
        mock.assert_called()

    def test_mock_not_called(self):
        mock = MagicMock()
        mock.assert_not_called()
        
    def test_called_with(self):
        mock = MagicMock()
        mock(1, 2, 3)
        mock.assert_called_with(1, 2, 3)
        
    def test_mock_attribute(self):
        mock = MagicMock()
        mock()
        mock(1, 3)
        print(mock.called)  # True
        print(mock.call_count)  # 2

if __name__ == "__main__":
    unittest.main()

# O/p:
# ..True
# 2
# ..
# ----------------------------------------------------------------------
# Ran 4 tests in 0.004s
# OK
# ** Process exited - Return Code: 0 **

import unittest
from unittest.mock import MagicMock

class MockTest(unittest.TestCase):
    def test_mock(self):
        mock = MagicMock()
        mock()
        mock.assert_called()

    def test_mock_not_called(self):
        mock = MagicMock()
        mock.assert_not_called()
        
    def test_called_with(self):
        mock = MagicMock()
        mock(1, 2, 3)
        mock.assert_called_with(1, 2, 3)
        
    def test_mock_attribute(self):
        mock = MagicMock()
        mock()
        mock(1, 3)
        print(mock.called)  # True
        print(mock.call_count)  # 2
        print(mock.mock_calls)  # [call(), call(1, 3)]

if __name__ == "__main__":
    unittest.main()

# O/p:
# ..True
# 2
# [call(), call(1, 3)]
# ..
# ----------------------------------------------------------------------
# Ran 4 tests in 0.005s
# OK
# ** Process exited - Return Code: 0 **

# Putting it all together:

import unittest
from unittest.mock import MagicMock

class Actor():
    def jump_out_of_helicopter(self):
        return "Nope, not doing it!"

    def light_on_fire(self):
        return "Heck no, where's my agent?"

class Movie():
    def __init__(self, actor):
        self.actor = actor

    def start_filming(self):
        self.actor.jump_out_of_helicopter()
        self.actor.light_on_fire()

class MovieTest(unittest.TestCase):
    def test_start_filming(self):
        stuntman = MagicMock()
        movie = Movie(stuntman)

        movie.start_filming()
        stuntman.jump_out_of_helicopter.assert_called()
        stuntman.light_on_fire.assert_called()

    if __name__ == "__main__":
        unittest.main()

# O/p:
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.065s
# OK
# ** Process exited - Return Code: 0 **

# Verifying Doubles:

from unittest.mock import MagicMock

class BurritoBowl():
    restaurant_name = "Bobo's Burritos"

    @classmethod
    def steak_special(cls):
        return cls("Steak", "White", 1)

    def __init__(self, protein, rice, guacamole_portions):
        self.protein = protein
        self.rice = rice
        self.guacamole_portions = guacamole_portions

    def add_guac(self):
        self.guacamole_portions += 1

lunch = BurritoBowl.steak_special()
print(lunch.protein)  # Steak
lunch.add_guac()
print(lunch.guacamole_portions)  # 2

# spec in MagicMock:

from unittest.mock import MagicMock

class BurritoBowl():
    restaurant_name = "Bobo's Burritos"

    @classmethod
    def steak_special(cls):
        return cls("Steak", "White", 1)

    def __init__(self, protein, rice, guacamole_portions):
        self.protein = protein
        self.rice = rice
        self.guacamole_portions = guacamole_portions

    def add_guac(self):
        self.guacamole_portions += 1

# lunch = BurritoBowl.steak_special()
# print(lunch.protein)
# lunch.add_guac()
# print(lunch.guacamole_portions)

class_mock = MagicMock(spec = BurritoBowl)
print(class_mock.restaurant_name)  # <MagicMock name='mock.restaurant_name' id='140443211324288'>
print(class_mock.steak_special())  # <MagicMock name='mock.steak_special()' id='140443196807152'>

# print(class_mock.chicken_special())
# print(class_mock.city)

# instance_mock = MagicMock(spec = BurritoBowl.steak_special())
# print(instance_mock.protein)
# print(instance_mock.rice)
# print(instance_mock.guacamole_portions)
# print(instance_mock.add_guac())
# print(instance_mock.add_cheese())
# print(instance_mock.beans)
# instance_mock.beans = True
# print(instance_mock.beans)

# As the spec for the Mock object is defined only and only for the BurritoBowl class,
# it'll not entertain any other methods like chicken_special, city, etc.).
# An AttributeError will be raised.

# The values mentioned will not be displayed as it's a Mock class, a fake one.

from unittest.mock import MagicMock

class BurritoBowl():
    restaurant_name = "Bobo's Burritos"

    @classmethod
    def steak_special(cls):
        return cls("Steak", "White", 1)

    def __init__(self, protein, rice, guacamole_portions):
        self.protein = protein
        self.rice = rice
        self.guacamole_portions = guacamole_portions

    def add_guac(self):
        self.guacamole_portions += 1

# lunch = BurritoBowl.steak_special()
# print(lunch.protein)
# lunch.add_guac()
# print(lunch.guacamole_portions)

class_mock = MagicMock(spec = BurritoBowl)
print(class_mock.restaurant_name)  # <MagicMock name='mock.restaurant_name' id='140172625906432'>
print(class_mock.steak_special())  # <MagicMock name='mock.steak_special()' id='140172615902048'>

# print(class_mock.chicken_special())
# print(class_mock.city)

instance_mock = MagicMock(spec = BurritoBowl.steak_special())
print(instance_mock.protein)  # <MagicMock name='mock.protein' id='140172616227376'>
print(instance_mock.rice)  # <MagicMock name='mock.rice' id='140172615903392'>
print(instance_mock.guacamole_portions)  # <MagicMock name='mock.guacamole_portions' id='140172614397264'>
print(instance_mock.add_guac())  # <MagicMock name='mock.add_guac()' id='140172614441424'>

print(instance_mock.add_cheese())  # AttributeError: Mock object has no attribute 'add_cheese'
# print(instance_mock.beans)
# instance_mock.beans = True
# print(instance_mock.beans)

from unittest.mock import MagicMock

class BurritoBowl():
    restaurant_name = "Bobo's Burritos"

    @classmethod
    def steak_special(cls):
        return cls("Steak", "White", 1)

    def __init__(self, protein, rice, guacamole_portions):
        self.protein = protein
        self.rice = rice
        self.guacamole_portions = guacamole_portions
        # self.beans = False

    def add_guac(self):
        self.guacamole_portions += 1

# lunch = BurritoBowl.steak_special()
# print(lunch.protein)
# lunch.add_guac()
# print(lunch.guacamole_portions)

class_mock = MagicMock(spec = BurritoBowl)
print(class_mock.restaurant_name)  # <MagicMock name='mock.restaurant_name' id='140091170249744'>
print(class_mock.steak_special())  # <MagicMock name='mock.steak_special()' id='140091182918560'>

# print(class_mock.chicken_special())
# print(class_mock.city)

instance_mock = MagicMock(spec = BurritoBowl.steak_special())
print(instance_mock.protein)  # <MagicMock name='mock.protein' id='140091183442944'>
print(instance_mock.rice)  # <MagicMock name='mock.rice' id='140091168210912'>
print(instance_mock.guacamole_portions)  # <MagicMock name='mock.guacamole_portions' id='140091168238736'>
print(instance_mock.add_guac())  # <MagicMock name='mock.add_guac()' id='140091179515200'>

# print(instance_mock.add_cheese())
# print(instance_mock.beans)
instance_mock.beans = True
print(instance_mock.beans)  # True

# The value for the 'beans' variable got displayed even it's not maintained in the 'BurritoBowl' class

# spec_set: A stricter version of spec where new variables are also not allowed to add and access.

from unittest.mock import MagicMock

class BurritoBowl():
    restaurant_name = "Bobo's Burritos"

    @classmethod
    def steak_special(cls):
        return cls("Steak", "White", 1)

    def __init__(self, protein, rice, guacamole_portions):
        self.protein = protein
        self.rice = rice
        self.guacamole_portions = guacamole_portions

    def add_guac(self):
        self.guacamole_portions += 1

# lunch = BurritoBowl.steak_special()
# print(lunch.protein)
# lunch.add_guac()
# print(lunch.guacamole_portions)

class_mock = MagicMock(spec = BurritoBowl)
print(class_mock.restaurant_name)  # <MagicMock name='mock.restaurant_name' id='139824896663600'>
print(class_mock.steak_special())  # <MagicMock name='mock.steak_special()' id='139824897105056'>

# print(class_mock.chicken_special())
# print(class_mock.city)

instance_mock = MagicMock(spec_set = BurritoBowl.steak_special())
print(instance_mock.protein)  # <MagicMock name='mock.protein' id='139824883792448'>
print(instance_mock.rice)  # <MagicMock name='mock.rice' id='139824883786688'>
print(instance_mock.guacamole_portions)  # <MagicMock name='mock.guacamole_portions' id='139824891477120'>
print(instance_mock.add_guac())  # <MagicMock name='mock.add_guac()' id='139824883441520'>

# print(instance_mock.add_cheese())
print(instance_mock.beans)  # AttributeError: Mock object has no attribute 'beans'
instance_mock.beans = True
print(instance_mock.beans)

# To overcome the above error, the newly mentioned variable 'beans' should be defined in the BurritoBowl class.

from unittest.mock import MagicMock

class BurritoBowl():
    restaurant_name = "Bobo's Burritos"

    @classmethod
    def steak_special(cls):
        return cls("Steak", "White", 1)

    def __init__(self, protein, rice, guacamole_portions):
        self.protein = protein
        self.rice = rice
        self.guacamole_portions = guacamole_portions
        self.beans = False

    def add_guac(self):
        self.guacamole_portions += 1

# lunch = BurritoBowl.steak_special()
# print(lunch.protein)
# lunch.add_guac()
# print(lunch.guacamole_portions)

class_mock = MagicMock(spec = BurritoBowl)
print(class_mock.restaurant_name)  # <MagicMock name='mock.restaurant_name' id='140223113597376'>
print(class_mock.steak_special())  # <MagicMock name='mock.steak_special()' id='140223112042912'>

# print(class_mock.chicken_special())
# print(class_mock.city)

instance_mock = MagicMock(spec_set = BurritoBowl.steak_special())
print(instance_mock.protein)  # <MagicMock name='mock.protein' id='140223114240576'>
print(instance_mock.rice)  # <MagicMock name='mock.rice' id='140223121777168'>
print(instance_mock.guacamole_portions)  # <MagicMock name='mock.guacamole_portions' id='140223112065584'>
print(instance_mock.add_guac())  # <MagicMock name='mock.add_guac()' id='140223112109552'>

# print(instance_mock.add_cheese())
print(instance_mock.beans)  # <MagicMock name='mock.beans' id='140223112117088'>
instance_mock.beans = True
print(instance_mock.beans)  # True

# patch function: Patch can be used as either a function or as a decorator that will automatically
# create a magic mock object in place of an existing object in some module.
# Once the test concludes, patch reverts the original object to its prior state.
# This facilitates the isolation of tested code from external factors, including databases, file systems, or APIs.

import urllib.request
import unittest
from unittest.mock import patch

class WebRequest():
    def __init__(self, url):
        self.url = url

    def execute(self):
        response = urllib.request.urlopen(self.url)
        if response.status == 200:
            return "SUCCESS"

        return "FAILURE"

# wr = WebRequest("http://www.google.com")
# wr.execute()

class WebRequestTest(unittest.TestCase):
    def test_execute_with_success_response(self):
        with patch('urllib.request.urlopen') as mock_urlopen:
            mock_urlopen.return_value.status = 200
            wr = WebRequest("http://www.google.com")
            self.assertEqual(wr.execute(), "SUCCESS")

    def test_execute_with_failure_response(self):
        with patch('urllib.request.urlopen') as mock_urlopen:
            mock_urlopen.return_value.status = 404
            wr = WebRequest("http://www.google.com")
            self.assertEqual(wr.execute(), "FAILURE")

if __name__ == "__main__":
    unittest.main()

# O/p:
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s
# OK
# ** Process exited - Return Code: 0 **

# Using the patch function as a decorator:

import urllib.request
import unittest
from unittest.mock import patch

class WebRequest():
    def __init__(self, url):
        self.url = url

    def execute(self):
        response = urllib.request.urlopen(self.url)
        if response.status == 200:
            return "SUCCESS"

        return "FAILURE"

# wr = WebRequest("http://www.google.com")
# wr.execute()

class WebRequestTest(unittest.TestCase):
    @patch('urllib.request.urlopen')
    def test_execute_with_success_response(self, mock_urlopen):
        mock_urlopen.return_value.status = 200
        wr = WebRequest("http://www.google.com")
        self.assertEqual(wr.execute(), "SUCCESS")

    @patch('urllib.request.urlopen')
    def test_execute_with_failure_response(self, mock_urlopen):
        mock_urlopen.return_value.status = 404
        wr = WebRequest("http://www.google.com")
        self.assertEqual(wr.execute(), "FAILURE")

if __name__ == "__main__":
    unittest.main()

# O/p:
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.004s
# OK
# ** Process exited - Return Code: 0 **

# What patch patches:

# web_request.py

# import urllib.request
from urllib.request import urlopen

class WebRequest():
    def __init__(self, url):
        self.url = url

    def execute(self):
        response = urlopen(self.url)
        if response.status == 200:
            return "SUCCESS"

        return "FAILURE"

# patch-III.py

import unittest
from unittest.mock import patch
from web_request import WebRequest

class WebRequestTest(unittest.TestCase):
    @patch('web_request.urlopen')
    def test_execute_with_success_response(self, mock_urlopen):
        mock_urlopen.return_value.status = 200
        wr = WebRequest("http://www.google.com")
        self.assertEqual(wr.execute(), "SUCCESS")

    @patch('web_request.urlopen')
    def test_execute_with_failure_response(self, mock_urlopen):
        mock_urlopen.return_value.status = 404
        wr = WebRequest("http://www.google.com")
        self.assertEqual(wr.execute(), "FAILURE")

if __name__ == "__main__":
    unittest.main()

# O/p:
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.004s
# OK
# ** Process exited - Return Code: 0 **
