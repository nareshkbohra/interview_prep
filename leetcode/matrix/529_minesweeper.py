from typing import List
from collections import deque


class Solution:
    def __init__(self):
        self.board = []

    def getNeighbors(self, x, y):
        rows, cols = len(self.board), len(self.board[0])
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for inc_x, inc_y in dirs:
            new_x, new_y = x + inc_x, y + inc_y
            if 0 <= new_x < rows and 0 <= new_y < cols:
                yield new_x, new_y

    def countOnes(self, x, y):
        result = 0
        for i, j in self.getNeighbors(x, y):
            if self.board[i][j] == "M":
                result += 1
        return result

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.board = board

        x, y = click
        item = board[x][y]
        if item == "M":
            board[x][y] = "X"
            return board

        queue = deque((x, y))
        while len(queue):
            currX, currY = queue.popleft()
            if board[currX][currY] != "E":
                continue

            ones = self.countOnes(currX, currY)
            if ones > 0:
                board[currX][currY] = str(ones)
                continue

            board[currX][currY] = "B"

            for neighbor in self.getNeighbors(currX, currY):
                queue.append(neighbor)

        return board
