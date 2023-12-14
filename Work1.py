from fractions import Fraction
import sympy as sym
from GeneralMethods import Sol
from GeneralMethods import Sequence


a = 3.6
x_100 = Sol(100, a)
x_100.x()
print(x_100.sequence)

seq_x = Sequence(x_100.sequence)
print(seq_x.findOccurrences())

