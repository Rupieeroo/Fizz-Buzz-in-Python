class FizzBuzz(object):
    def __init__(self, number):
        if FizzBuzz.is_valid_number(number):
            self.number = number

    @property
    def result(self):
        if self.number == 3 or self.number == 6:
            return "Fizz"
        elif self.number == 5 or self.number == 10:
            return "Buzz"
        elif self.number == 15 or self.number == 30:
            return "FizzBuzz"
        return self.number

    @staticmethod
    def is_valid_number(number):
        if number <= 0 or number > 100:
            raise ValueError("Number must be between 0 and 101")
        return True
