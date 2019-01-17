class FizzBuzz(object):
    def __init__(self, number):
        if number <= 0:
            raise ValueError()
        self.number = 1
