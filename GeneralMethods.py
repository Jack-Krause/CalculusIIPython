from fractions import Fraction


class Sol:
    def __init__(self, n, a):
        self.a = a
        self.n = n
        self.sequence = []

    def x(self):
        if self.n == 0:
            self.sequence.append(0.5)
            return 0.5
        return self.g(self.n)

    def g(self, n):
        if n == 0:
            return 0.5

        x_previous = self.g(n - 1)
        x_n = self.a * x_previous * (1 - x_previous)
        self.sequence.append(format(x_n, '.4f'))
        return x_n

    def fShow(self):
        print(Fraction.from_float(self.x()))

    def show(self):
        print(str(self.n) + ": " + format(self.x(), '.4f'))




