from fractions import Fraction


class Sol:
    def __init__(self, n, a):
        self.a = a
        self.n = n

    def x(self):
        if self.n == 1:
            return 0.5
        return Sol.g(self.n, self.a)

    @staticmethod
    def g(n, a):
        if n == 0:
            return 0.5

        x_n = Sol.g(n-1, a)
        return a * x_n * (1 - x_n)

    def fShow(self):
        print(Fraction.from_float(self.x()))

    def show(self):
        print(format(self.x(), '.5f'))


