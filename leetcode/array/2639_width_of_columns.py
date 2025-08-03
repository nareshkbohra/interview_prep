from typing import List


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        cols = len(grid[0])
        result = [0] * cols
        for i in range(cols):
            result[i] = max(len(str(grid[j][i])) for j in range(len(grid)))
        return result
