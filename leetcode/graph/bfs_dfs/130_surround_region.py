from typing import List
from collections import deque


class Solution:
	def solve(self, board: List[List[str]]) -> None:
		"""
		Do not return anything, modify board in-place instead.
		"""
		rows = len(board)
		cols = len(board[0])
		queue = deque()

		def locs(x, y):
			dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
			for i, j in dirs:
				new_x, new_y = x + i, y + j
				if 0 <= new_x < rows and 0 <= new_y < cols:
					yield (new_x, new_y)

		def mark(x, y):
			curr_element = board[x][y]
			if curr_element in ("X", "#"):
				return
			print(f"Starting mark {x} {y}")
			queue.append((x, y))
			while len(queue):
				(curr_i, curr_j) = queue.pop()
				board[curr_i][curr_j] = "#"
				for loc_i, loc_j in locs(curr_i, curr_j):
					if board[loc_i][loc_j] == "O":
						queue.append((loc_i, loc_j))
			self.print_board(board)

		for i in range(cols):
			mark(0, i)
			mark(rows - 1, i)

		for i in range(rows):
			mark(i, 0)
			mark(i, cols - 1)

		for i in range(rows):
			for j in range(cols):
				if board[i][j] == "#":
					board[i][j] = "O"
				else:
					board[i][j] = "X"

		return

	def print_board(self, b):
		for row in b:
			for col in row:
				print(col, end=" ")
			print()


s = Solution()
board = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
s.solve(board)
