from typing import List
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        queue = []
        found = 0
        queue.append((matrix[0][0], 0, 0))
        seen = set()
        rows = len(matrix)
        cols = len(matrix[0])
        while len(queue):
            currValue, x, y = heapq.heappop(queue)
            if (x, y) in seen:
                continue
            seen.add((x, y))
            found += 1
            if found == k:
                return currValue

            if x + 1 < rows:
                heapq.heappush(queue, (matrix[x + 1][y], x + 1, y))
            if y + 1 < cols:
                heap.heappush(queue, (matrix[x][y + 1], x, y + 1))

        return -1
