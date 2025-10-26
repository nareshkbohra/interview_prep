from typing import List
import heapq
from functools import partial


class Solution:
    def _neighbors(self, rows, cols, i, j):
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for x, y in dirs:
            new_i, new_j = i + x, j + y
            if 0 <= new_i < rows and 0 <= new_j < cols:
                yield new_i, new_j

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        distance = [[float("inf")] * cols for _ in range(rows)]
        queue = [(0, (0, 0))]
        distance[0][0] = 0
        neighbors = partial(self._neighbors, rows, cols)
        while len(queue):
            curr_effort, (curr_x, curr_y) = heapq.heappop(queue)
            curr_height = heights[curr_x][curr_y]
            for neigh_x, neigh_y in neighbors(curr_x, curr_y):
                effort = max(curr_effort, abs(curr_height - heights[neigh_x][neigh_y]))
                if effort < distance[neigh_x][neigh_y]:
                    distance[neigh_x][neigh_y] = effort
                    heapq.heappush(queue, (effort, (neigh_x, neigh_y)))
        return int(distance[rows - 1][cols - 1])


heights = [[1, 10, 6, 7, 9, 10, 4, 9]]
s = Solution()
res = s.minimumEffortPath(heights)
print(res)
