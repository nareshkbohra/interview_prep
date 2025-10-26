from typing import List


class Solution:
    def __init__(self):
        self.grid = []
        self.rows = 0
        self.cols = 0
        self.memory = {}

    def helper(self, x, y):
        if x >= self.rows or y >= self.cols or min(x, y) < 0 or self.grid[x][y] == 1:
            return 0

        if x == self.rows - 1 and y == self.cols - 1:
            return 1

        key = (x, y)
        if key in self.memory:
            return self.memory[key]

        dirs = [(0, 1), (1, 0)]
        result = 0
        for dir in dirs:
            nextX, nextY = x + dir[0], y + dir[1]
            result += self.helper(nextX, nextY)

        self.memory[key] = result
        return result

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.grid = obstacleGrid
        self.rows = len(obstacleGrid)
        self.cols = len(obstacleGrid[0])
        self.memory = {}
        return self.helper(0, 0)
