import unittest
from fizzBuzz import FizzBuzz

class FizzBuzzTest(unittest.TestCase):

    def test_0_raises_value_error(self):
        with self.assertRaises(ValueError):
            FizzBuzz(0)
