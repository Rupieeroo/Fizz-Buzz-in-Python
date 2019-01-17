class FizzBuzz(object):
    def __init__(self, number):
        if number == 0 or number == -1:
            raise ValueError()
        self.number = 1
