from typing import List
from typing import LiteralString
from random import randint
from collections import deque
import logging

logger = logging.getLogger(__name__)


class Cell:
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y

	def __eq__(self, other: "Cell") -> bool:
		return self.x == other.x and self.y == other.y

	def __repr__(self) -> str:
		return f"({self.x},{self.y})"

	def __hash__(self) -> int:
		return hash((self.x, self.y))


class Jumper:
	def __init__(self, start: Cell, end: Cell):
		self.start = start
		self.end = end

	def __repr__(self) -> str:
		return f"{self.start}->{self.end}"


class Board:
	def __init__(self, rows: int, cols: int, jumpers: List[Jumper]):
		self.rows = rows
		self.cols = cols

		self.jumps = {}
		for jump in jumpers:
			start, end = jump.start, jump.end
			self.verify_cell(start)
			self.verify_cell(end)

			if start in self.jumps:
				# We already have a jump here, cant add another
				raise ValueError(
					"Either a snake or ladder is already present at {start}"
				)

			self.jumps[start] = end

	def next(self, curr_cell: Cell, roll: int) -> Cell:
		next_row = curr_cell.x + ((curr_cell.y + roll) // self.cols)
		if next_row >= self.rows:
			return curr_cell

		next_col = (curr_cell.y + roll) % self.cols
		next_pos = Cell(next_row, next_col)
		if next_pos in self.jumps:
			logger.info(f"You have hit a jumper {next_pos}")
			return self.jumps[next_pos]

		return next_pos

	def verify_cell(self, cell: Cell):
		if cell.x < 0 or cell.y < 0 or cell.y >= self.cols or cell.x >= self.rows:
			raise ValueError(f"{cell} is not valid")


class Dice:
	def __init__(self, count: int):
		self.count = count

	def roll(self) -> int:
		result = 0
		for _ in range(self.count):
			result += randint(1, 6)
		return result


class Player:
	def __init__(self, name: LiteralString, pid: int):
		self.name = name
		self.pid = pid
		self.position = Cell(0, 0)


class SnakeAndLadder:
	def __init__(self, players: List[Player], dice: Dice, board: Board):
		self.players = players
		self.dice = dice

		self.board = board
		self.turns = deque(players[:])
		self.final_position = Cell(board.rows - 1, board.cols - 1)

	def start(self):
		"""Actual game loop"""
		winning_order = []

		while self.turns:
			player = self.turns.popleft()
			roll = self.dice.roll()
			logger.info(f"Player {player.name} is taking turn and has rolled {roll}")
			orig_position = player.position

			new_position = self.board.next(player.position, roll)

			min_new_position = self.board.next(new_position, self.dice.count)
			if (
				min_new_position != self.final_position
				and min_new_position == new_position
			):
				logger.info("Player will get stuck on next position, not advancing")
				self.turns.append(player)
				continue

			player.position = new_position

			logger.info(
				f"Player {player.name} {orig_position} is going to position {player.position}"
			)

			if player.position == self.final_position:
				logger.info(f"Player {player.name} has won, congrats!!!")
				winning_order.append(player.name)
				continue

			if roll == self.dice.count * 6:
				logger.info(f"Player {player.name} is getting one more turn")
				self.turns.appendleft(player)
			else:
				self.turns.append(player)

		logger.info(f"Winning order is {'->'.join(winning_order)}")
