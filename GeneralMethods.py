from fractions import Fraction


class Sol:
    def __init__(self, n, a):
        self.a = a
        self.n = n
        self.sequence = [0.5]

    def x(self):
        if self.n == 0:
            return 0.5

        return self.g(self.n)

    def g(self, n):
        if n == 0:
            return 0.5

        x_previous = self.g(n - 1)
        x_n = self.a * x_previous * (1 - x_previous)
        app_x_n = round(x_n, 4)
        self.sequence.append(app_x_n)
        return x_n

    def fShow(self):
        print(Fraction.from_float(self.x()))

    def show(self):
        print(str(self.n) + ": " + format(self.x(), '.4f'))


class Sequence:
    def __init__(self, seq):
        self.seq = seq

    def findOccurrences(self, target):
        show_list = ['------'] * len(self.seq)

        for i, value in enumerate(self.seq):
            if -0.3 < (value - target) < 0.3:
                show_list[i] = value

        return show_list
