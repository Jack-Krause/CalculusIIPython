from fractions import Fraction

import sympy as sym
from GeneralMethods import Sol

a = 3.5
x1 = Sol(1, a)
x2 = Sol(2, a)
# x1 = Fraction.from_float(x1)

for i in range(101):
    Sol(i, a).show()
    print("---")

