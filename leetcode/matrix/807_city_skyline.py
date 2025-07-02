from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        N = len(grid)
        maxRows = [0] * N
        for i in range(N):
            maxRows[i] = max(grid[i])
        maxCols = [0] * N
        for i in range(N):
            maxCols[i] = max(grid[j][i] for j in range(N))

        result = 0
        for i in range(N):
            for j in range(N):
                result += min(maxRows[i], maxCols[j]) - grid[i][j]

        return result
