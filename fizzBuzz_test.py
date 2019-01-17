import unittest
from fizzBuzz import FizzBuzz

class FizzBuzzTest(unittest.TestCase):

    def test_0_raises_value_error(self):
        with self.assertRaises(ValueError):
            FizzBuzz(0)

    def test_1_does_not_raise_value_error(self):
        assert FizzBuzz(1).number == 1

    def test_101_raises_value_error(self):
        with self.assertRaises(ValueError):
            FizzBuzz(101)

    def test_1_returns_1(self):
        assert FizzBuzz(1).result == 1

    def test_2_returns_2(self):
        assert FizzBuzz(2).result == 2

    def test_3_returns_Fizz(self):
        assert FizzBuzz(3).result == "Fizz"

    def test_6_returns_Fizz(self):
        assert FizzBuzz(6).result == "Fizz"

    def test_5_returns_Buzz(self):
        assert FizzBuzz(5).result == "Buzz"

    def test_15_returns_FizzBizz(self):
        assert FizzBuzz(15).result == "FizzBuzz"
