class Solution:
    def __init__(self, n, a):
        self.a = a
        self.n = n

    def x(self):
        if self.n == 1:
            return 0.5
        return Solution.g(self.n-1, self.a)

    @staticmethod
    def g(n, a):
        if n == 0:
            return 0.5

        num = Solution.g(n-1, a)
        return a * num * (1 - num)

