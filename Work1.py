from fractions import Fraction
import sympy as sym
from GeneralMethods import Sol
from GeneralMethods import Sequence

a = 3.49

def showComparison(start, iterations):

    for i in range(iterations + 1):
        start = round(start + 0.01, 2)
        a_x = Sol(100, start)
        a_x.x()
        seq_a = Sequence(a_x.sequence)
        occurrences, visual = seq_a.findOccurrences()

        occurrences_str = ""
        for key, value in occurrences.items():
            occurrences_str += "|" + str(key) + ":" + str(value) + "| "

        print("<<" + str(start) + ">>")
        print(occurrences_str)
        print(a_x.sequence)
        print(visual)
        print()


showComparison(a, 25)

