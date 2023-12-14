from collections import Counter
from fractions import Fraction
import sympy as sym
from GeneralMethods import Sol
from GeneralMethods import Sequence
import matplotlib.pyplot as pl

a = 3.49

def showComparison(start, iterations, terms):

    for i in range(iterations + 1):
        start = round(start + 0.01, 2)
        a_x = Sol(terms, start)
        a_x.x()
        seq_a = Sequence(a_x.sequence)
        occurrences, visual = seq_a.findOccurrences()

        occurrences_str = ""
        for key, value in occurrences.items():
            occurrences_str += "|" + str(key) + ":" + str(value) + "| "

        print("<< a = " + str(start) + ">>")
        print(occurrences_str)
        print(a_x.sequence)
        print(visual)
        print()


# showComparison(3.72, 3, 200)
# showComparison(a, 25, 200)

p_sol = Sol(200, 3.75)
p_sol.x()
p_sequence = p_sol.sequence
print(p_sequence)
pl.figure(figsize=(8, 6))
pl.plot(p_sequence, linestyle='-', marker='o', color='red')
pl.grid(True)
pl.show()

