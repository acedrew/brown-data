import brown
import sine
import itertools
import ramp


class brown_sine:
    def __init__(self, scale, brown_scale, steps, max_brown, pos):
        self.brown = brown.brown_data(brown_scale, max_brown)
        self.sine = sine.sine(scale, steps, pos)
        self.num = 0

    def step(self):
        self.num = self.sine.step() + self.brown.random()
        return self.num


class brown_ramp:
    def __init__(self, scale, brown_scale, steps, max_brown, pos=True):
        self.brown = brown.brown_data(brown_scale, max_brown)
        self.ramp = ramp.ramp(scale, steps, pos)
        self.num = 0

    def step(self):
        self.num = self.ramp.step() + self.brown.random()
        return self.num

if __name__ == "__main__":
    test = brown_ramp(1, 0.1, 100, 0.05, False)
    for _ in itertools.repeat(None, 500):
        print test.step()
