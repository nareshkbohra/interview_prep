from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        healthy = 0
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    healthy += 1

        def neighbors(i, j):
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for x, y in dirs:
                new_x, new_y = x + i, y + j
                if 0 <= new_x < rows and 0 <= new_y < cols:
                    yield new_x, new_y

        minutes = -1
        while len(queue):
            queue_size = len(queue)
            for _ in range(queue_size):
                curr_item = queue.popleft()
                for i, j in neighbors(curr_item[0], curr_item[1]):
                    if grid[i][j] == 1:
                        grid[i][j] = 2
                        healthy -= 1
                        queue.append((i, j))
            minutes += 1

        if healthy:
            return -1
        return minutes


s = Solution()
grid = [[2, 1, 1], [1, 1, 1], [0, 1, 2]]
for row in grid:
    print(" ".join(str(i) for i in row))
res = s.orangesRotting(grid)
print(res)
