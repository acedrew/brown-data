import math
import itertools


class sine:
    def __init__(self, scale=1, steps=360, pos=False):
        self.steps = steps
        self.scale = scale
        self.num = 0
        self.stepn = 0
        self.pos = pos

    def step(self):
        angle = math.radians((360 / self.steps) * self.stepn)
        self.num = math.sin(angle) * self.scale
        self.stepn += 1
        if self.stepn == self.steps:
            self.stepn = 0
        if self.pos:
            self.num = self.num + self.scale
        return self.num

if __name__ == "__main__":
    test = sine(100)
    for _ in itertools.repeat(1, 200):
        print test.step()
