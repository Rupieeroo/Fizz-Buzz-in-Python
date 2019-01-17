class FizzBuzz(object):
    def __init__(self, number):
        if number <= 0 or number > 100:
            raise ValueError()
        self.number = 1
