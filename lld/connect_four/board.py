from enum import Enum
from typing import Tuple

from player import DiskColor


class SlotState(Enum):
    EMPTY = 0
    RED = 1
    YELLOW = 2


class BoardException(Exception):
    pass


class Direction(Enum):
    LEFT_UP = (-1, -1)
    RIGHT_UP = (-1, 1)
    LEFT_DOWN = (1, -1)
    RIGHT_DOWN = (1, 1)
    LEFT = (0, -1)
    RIGHT = (0, 0)
    UP = (-1, 0)
    DOWN = (1, 0)


class Board:
    DIR_PAIRS = [
        (Direction.UP, Direction.DOWN),
        (Direction.LEFT, Direction.RIGHT),
        (Direction.LEFT_UP, Direction.RIGHT_DOWN),
        (Direction.LEFT_DOWN, Direction.RIGHT_UP),
    ]

    def __init__(self, rows: int = 6, cols: int = 7):
        self.n_rows = rows
        self.n_cols = cols
        self.board = [[SlotState.EMPTY] * cols for _ in range(rows)]
        self.available_slots = rows * cols

    def _is_valid_move(self, row: int, col: int):
        if not self._is_valid_coordinates(row, col):
            return False

        if self.board[row][col] != SlotState.EMPTY:
            return False

        return True

    def _is_valid_coordinates(self, row: int, col: int):
        return 0 <= row < self.n_rows and 0 <= col < self.n_cols

    def _count_in_dir(self, color: SlotState, row: int, col: int, direction: Direction):
        if not self._is_valid_coordinates(row, col):
            return 0

        if self.board[row][col] != color:
            return 0

        return 1 + self._count_in_dir(color, row + direction.value[0], col + direction.value[1], direction)

    def is_full(self) -> bool:
        return self.available_slots == 0

    def place_disk(self, row: int, col: int, disk_color: DiskColor) -> Tuple[int, int]:
        if not self._is_valid_move(row, col):
            raise BoardException("This move is not valid")

        curr_row = row
        while True:
            if curr_row == 0:
                break
            if self.board[curr_row - 1][col] != SlotState.EMPTY:
                break
            curr_row -= 1

        if disk_color == DiskColor.YELLOW:
            self.board[curr_row][col] = SlotState.YELLOW
        else:
            self.board[curr_row][col] = SlotState.RED

        self.available_slots -= 1
        return (curr_row, col)

    def is_four_in_row(self, row: int, col: int) -> bool:
        curr_color = self.board[row][col]
        for first, second in self.DIR_PAIRS:
            first_count = self._count_in_dir(curr_color, row, col, first)
            second_count = self._count_in_dir(curr_color, row, col, second)

            # It need to be more than 4 as current one is counted twice.
            if first_count + second_count > 4:
                return True

        return False
