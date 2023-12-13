import sympy as sym
from GeneralMethods import Solution

a = 0.5
x1 = Solution(1, a).x()
x2 = Solution(2, a).x()


print(x1, x2)

