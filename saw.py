import itertools
import ramp
import operator as o


class saw(ramp.ramp):
    def __init__(self, scale=1, steps=100, pos=True, forward=True):
        ramp.ramp.__init__(self, scale, steps, pos)
        self.forward = forward
        if forward:
            self.oper = o.ge
            if pos:
                self.comp = scale * 2
                self.reset = 0
            else:
                self.comp = scale
                self.reset = -steps
        else:
            self.oper = o.le
            if pos:
                self.comp = 0
                self.reset = steps * 2
            else:
                self.comp = -scale
                self.reset = steps
        self.stepn = self.reset

    def step(self):
        newNum = ramp.ramp.step(self)
        if self.oper(newNum, self.comp):
            self.stepn = self.reset
        self.num = newNum
        return self.num

if(__name__ == "__main__"):
    test = ramp(10, 40, False)
    for _ in itertools.repeat(None, 200):
        print test.step()
