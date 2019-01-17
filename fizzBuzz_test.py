import unittest
from fizzBuzz import FizzBuzz

class FizzBuzzTest(unittest.TestCase):

    def test_0_raises_value_error(self):
        with self.assertRaises(ValueError):
            FizzBuzz(0)

    def test_1_does_not_raise_value_error(self):
        assert FizzBuzz(1).number == 1
