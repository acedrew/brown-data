import itertools


class ramp:
    def __init__(self, scale=1, steps=100, pos=True):
        self.scale = scale
        self.steps = steps
        self.stepval = self.scale / float(self.steps)
        self.num = 0
        self.stepn = 0
        if pos:
            self.pos = 0
        else:
            self.pos = -self.steps
        self.up = True

    def step(self):
        self.num = self.stepn * self.stepval
        if self.stepn == self.steps:
            self.up = False
        elif self.stepn == self.pos:
            self.up = True
        if self.up:
            self.stepn += 1
        else:
            self.stepn -= 1
        return self.num

if(__name__ == "__main__"):
    test = ramp(10, 40, False)
    for _ in itertools.repeat(None, 200):
        print test.step()
