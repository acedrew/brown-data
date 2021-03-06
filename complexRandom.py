import brown
import sine
import itertools
import saw
import triangle


class brown_sine:

    """Provides the sum of a sine wave with amplitude n(scale), with resolution
    n(steps) and random component with amplitude n(brown_scale) and maximum
    step delta of random of n(max_brown) either centered around zero(pos=False)
    or centered around amplitude/2(pos=True)"""

    def __init__(self, scale, brown_scale, steps, max_brown, pos=False):
        self.brown = brown.brown_data(brown_scale, max_brown)
        self.sine = sine.sine(scale, steps, pos)
        self.num = 0

    def step(self):
        self.num = self.sine.step() + self.brown.random()
        return self.num


class brown_saw:

    """Provides the sum of a saw function of amplitude n(scale) with
    resolution n(steps) and random component with amplitude n(brown_scale) and
    maximum step delta of random n(max_brown) either centered around
    zero(pos=False) or centered on amplitude/2(pos=False)"""

    def __init__(self, scale, brown_scale, steps, max_brown, pos=True):
        self.brown = brown.brown_data(brown_scale, max_brown)
        self.saw = saw.saw(scale, steps, pos)
        self.num = 0

    def step(self):
        self.num = self.saw.step() + self.brown.random()
        return self.num


class brown_triangle:

    """Provides the sum of a triangle function of amplitude n(scale) with
    resolution n(steps) and random component with amplitude n(brown_scale) and
    maximum step delta of random n(max_brown) either centered around
    zero(pos=False) or centered on amplitude/2(pos=False), direction of
    triangletooth is reversible(forward=True)"""

    def __init__(self, scale, brown_scale, steps,
                 max_brown, pos=True, forward=True):
        self.brown = brown.brown_data(brown_scale, max_brown)
        self.triangle = triangle.triangle(scale, steps, pos, forward)
        self.num = 0

    def step(self):
        self.num = self.triangle.step() + self.brown.random()
        return self.num

if __name__ == "__main__":
    import timeit

    def runTest():
        test_sine = brown_sine(1, 0.2, 100, 0.02, False)
        for _ in itertools.repeat(None, 1300):
            print(test_sine.step())
        test_saw = brown_saw(1, 0.2, 100, 0.02, False)
        for _ in itertools.repeat(None, 1300):
            print(test_saw.step())
        test_triangle = brown_triangle(1, 0.2, 100, 0.02, False, False)
        for _ in itertools.repeat(None, 1300):
            print(test_triangle.step())
    print(timeit.timeit('runTest()',
                        'from __main__ import runTest', number=100))
