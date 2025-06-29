import sys

sys.setrecursionlimit(6000)


MOD = (10**9) + 7


class Solution:
    def __init__(self):
        self.memory = {}

    def nextPosition(self, currLocation):
        if currLocation == 1:
            return [6, 8]
        if currLocation == 2:
            return [7, 9]
        if currLocation == 3:
            return [4, 8]
        if currLocation == 4:
            return [3, 9, 0]
        if currLocation == 5:
            return []
        if currLocation == 6:
            return [1, 7, 0]
        if currLocation == 7:
            return [2, 6]
        if currLocation == 8:
            return [1, 3]
        if currLocation == 9:
            return [2, 4]
        if currLocation == 0:
            return [4, 6]
        return []

    def helper(self, currLocation, steps):
        if steps <= 0:
            return 0
        if steps == 1:
            return 1
        key = (currLocation, steps)
        if key in self.memory:
            return self.memory[key]
        result = 0
        for neighbor in self.nextPosition(currLocation):
            result += self.helper(neighbor, steps - 1)
        result = result % MOD
        self.memory[key] = result
        return result

    def knightDialer(self, n: int) -> int:
        self.memory = {}
        result = 0
        for i in range(10):
            result += self.helper(i, n)
        return result % MOD


s = Solution()
res = s.knightDialer(3131)
print(res)
