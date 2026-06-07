import unittest

class TestProduct(unittest.TestCase):
    def test_multiply_two_numbers_together(self):
        self.assertEqual(
            product(3, 5),
            15
        )

if __name__ == "__main__":
    unittest.main()

# The above test will fail as the function "product" is not yet defined which is the first stage of Test Driven Development (TDD).

import unittest

def product():
    pass

class TestProduct(unittest.TestCase):
    def test_multiply_two_numbers_together(self):
        self.assertEqual(
            product(3, 5),
            15
        )

if __name__ == "__main__":
    unittest.main()

# The above test will fail as the function "product" is now defined but not taking any arguments.

import unittest

def product(a, b):
    return a * b

class TestProduct(unittest.TestCase):
    def test_multiply_two_numbers_together(self):
        self.assertEqual(
            product(3, 5),
            15
        )

if __name__ == "__main__":
    unittest.main()
    
# Now, the test is passed as the "product" is defined and also it takes the arguments.
