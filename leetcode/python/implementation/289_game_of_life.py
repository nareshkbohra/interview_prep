from typing import List
from functools import partial


class Solution:
    def get_neighbors(self, rows, cols, i, j):
        for dir in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            new_i, new_j = i + dir[0], j + dir[1]
            if 0 <= new_i < rows and 0 <= new_j < cols:
                yield new_i, new_j

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        neighbor_counts = [[0] * cols for _ in range(rows)]
        neighbors = partial(self.get_neighbors, rows, cols)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 0:
                    continue
                for x, y in neighbors(i, j):
                    neighbor_counts[x][y] += 1

        for i in range(rows):
            for j in range(cols):
                neigh_count = neighbor_counts[i][j]
                if board[i][j] == 0:
                    if neigh_count == 3:
                        board[i][j] = 1
                    continue

                if neigh_count != 2 and neigh_count != 3:
                    board[i][j] = 0

        return


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
for row in board:
    print(" ".join(str(i) for i in row))
print("-----------")
s = Solution()
s.gameOfLife(board)
for row in board:
    print(" ".join(str(i) for i in row))
