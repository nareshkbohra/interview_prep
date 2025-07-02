class Solution:
    def __init__(self):
        self.memory = {}

    def helper(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x

        key = (x, n)
        if key in self.memory:
            return self.memory[key]
        squareRoot = self.helper(x, n // 2)
        result = squareRoot * squareRoot

        if n % 2 == 1:
            result *= x

        return result

    def myPow(self, x: float, n: int) -> float:
        self.memory = {}
        isNegative = n < 0
        result = self.helper(x, abs(n))
        if isNegative:
            result = 1 / result
        return result


s = Solution()
res = s.myPow(2, 1)
print(res)
