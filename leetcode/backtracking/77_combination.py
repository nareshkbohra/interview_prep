from typing import List


class Solution:
    def __init__(self):
        self.target = 0
        self.n = 0
        self.results = []

    def dfs(self, curr_path: List[int], start):
        if len(curr_path) == self.target:
            self.results.append(list(curr_path))
            return

        for i in range(start, self.n + 1):
            curr_path.append(i)
            self.dfs(curr_path, i + 1)
            curr_path.pop()
        return

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.target = k
        self.n = n
        self.results = []
        self.dfs([], 1)
        return self.results


s = Solution()
res = s.combine(4, 2)
print(res)
