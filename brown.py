import random
import itertools


class brown_data:
    def __init__(self, scale=1, max_change=0.1):
        self.num = None
        self.scale = scale
        self.max_change = max_change

    def random(self):
        if self.num is not None:
            self.num = self.next()
            return self.num
        else:
            factor = self.scale * 2
            self.num = (random.random() * factor) - self.scale
            return self.num

    def next(self):
        factor = self.max_change * 2
        difference = self.max_change - (random.random() * factor)
        newNum = self.num + difference
        if newNum < -self.scale or newNum > self.scale:
            self.num = self.num - difference
        else:
            self.num = newNum
        return self.num

if(__name__ == "__main__"):
    test = brown_data(10)
    for _ in itertools.repeat(None, 2000):
        print test.random()
