class Solution:
    def __init__(self):
        self.memory = {}

    def helper(self, n):
        if n == 0:
            return 0
        if n in self.memory:
            return self.memory[n]

        result = float("inf")
        for i in range(1, n + 1):
            if i * i > n:
                break
            result = min(result, 1 + self.helper(n - (i * i)))

        self.memory[n] = result
        return result

    def numSquares(self, n: int) -> int:
        self.memory = {}
        return self.helper(n)


s = Solution()
res = s.numSquares(1)
print(res)
