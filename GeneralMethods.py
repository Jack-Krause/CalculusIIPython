from collections import Counter
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
        app_x_n = round(x_n, 3)
        self.sequence.append(app_x_n)
        return x_n

    def fShow(self):
        print(Fraction.from_float(self.x()))

    def show(self):
        print(str(self.n) + ": " + format(self.x(), '.4f'))


class Sequence:
    def __init__(self, seq):
        self.seq = seq

    def findOccurrences(self):
        show_list = ['------'] * len(self.seq)
        counter = Counter(self.seq)
        target = counter.most_common(1)[0][0]
        occurrences = 0

        for i, value in enumerate(self.seq):
            if value == target:
                show_list[i] = value
                occurrences += 1

        return occurrences, show_list
