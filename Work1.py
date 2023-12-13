from fractions import Fraction

import sympy as sym
from GeneralMethods import Sol

a = 0.5
x1 = Sol(1, a)
x2 = Sol(2, a)
# x1 = Fraction.from_float(x1)

x1.show()
x2.show()
x3 = Sol(3, a).show()
x4 = Sol(4, a).show()
x5 = Sol(5, a).show()
