from typing import List


class Solution:
    def __init__(self):
        self.grid = []
        self.rows = 0
        self.cols = 0
        self.memory = {}

    def helper(self, x, y):
        if x == self.rows - 1 and y == self.cols - 1:
            return self.grid[x][y]
        key = (x, y)
        if key in self.memory:
            return self.memory[key]
        dirs = [(0, 1), (1, 0)]
        minDist = float("inf")
        for dir in dirs:
            nextX, nextY = x + dir[0], y + dir[1]
            if 0 <= nextX < self.rows and 0 <= nextY < self.cols:
                minDist = min(minDist, self.helper(nextX, nextY))
        result = minDist + self.grid[x][y]
        self.memory[key] = result
        return result

    def minPathSum(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.memory = {}
        return self.helper(0, 0)
