from math import ceil

class Solution:
    def __init__(self):
        self.state = {}

    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n < 0: x = 1/x

        n = abs(n)
        if n == 1: return x
        self.state = {}

        return self.my_pow_recursive(x, n // 2) * self.my_pow_recursive(x, (ceil(n / 2)))

    def my_pow_recursive(self, x: int, n: int) -> float:
        if n == 1: return x

        if n in self.state:
            return self.state[n]
         
        self.state[n] = self.my_pow_recursive(x, abs(n // 2)) * self.my_pow_recursive(x, (ceil(abs(n / 2) ) ))
        return self.state[n]

        