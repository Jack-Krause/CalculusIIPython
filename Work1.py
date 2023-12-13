import sympy as sym
a = sym.var("a")


def x(i):
    if i == 1:
        return 0.5

    return x(i-1) + 0.5








