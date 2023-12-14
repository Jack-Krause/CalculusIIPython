from fractions import Fraction
import sympy as sym
from GeneralMethods import Sol
from GeneralMethods import Sequence

a = 3.49
x_100 = Sol(100, a)
x_100.x()
print(x_100.sequence)
seq_x = Sequence(x_100.sequence)
print(seq_x.findOccurrences())

for i in range(11):
    a = round(a+0.01, 2)
    a_x = Sol(100, a)
    a_x.x()
    print("--" + str(a) + "--")
    print(a_x.sequence)
    seq_a = Sequence(a_x.sequence)
    print(seq_a.findOccurrences())
    print()


