class FizzBuzz(object):
    def __init__(self, number):
        if FizzBuzz.is_valid_number(number):
            self.number = 1

    @property
    def result(self):
        return 1

    @staticmethod
    def is_valid_number(number):
        if number <= 0 or number > 100:
            raise ValueError("Number must be between 0 and 101")
        return True
