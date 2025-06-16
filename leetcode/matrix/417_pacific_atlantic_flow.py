from typing import List


class Solution:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.matrix = []

    def directions(self, i, j):
        for dir in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            new_i, new_j = i + dir[0], j + dir[1]
            if 0 <= new_i < self.rows and 0 <= new_j < self.cols:
                yield (new_i, new_j)

    def dfs(self, i, j, visited):
        if (i, j) in visited:
            return
        visited.add((i, j))
        for new_i, new_j in self.directions(i, j):
            if self.matrix[new_i][new_j] >= self.matrix[i][j]:
                self.dfs(new_i, new_j, visited)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.rows = len(heights)
        self.cols = len(heights[0])
        self.matrix = heights
        pVisited = set()
        aVisited = set()
        for i in range(self.rows):
            self.dfs(i, 0, pVisited)
            self.dfs(i, self.cols - 1, aVisited)

        for j in range(self.cols):
            self.dfs(0, j, pVisited)
            self.dfs(self.rows - 1, j, aVisited)

        result = []
        for i in range(self.rows):
            for j in range(self.cols):
                if (i, j) in pVisited and (i, j) in aVisited:
                    result.append([i, j])
        return result


s = Solution()
heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
res = s.pacificAtlantic(heights)
print(res)
