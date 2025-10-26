class Solution:
    def __init__(self):
        self.memory = {}

    def helper(self, start, end):
        if start >= end:
            return 0

        key = (start, end)
        if key in self.memory:
            return self.memory[key]
        result = float("inf")
        for i in range(start, end + 1):
            maxCost = i + max(self.helper(start, i - 1), self.helper(i + 1, end))
            result = min(result, maxCost)

        self.memory[key] = result
        return result

    def getMoneyAmount(self, n: int) -> int:
        self.memory = {}
        return self.helper(1, n)


s = Solution()
res = s.getMoneyAmount(2)
print(res)
