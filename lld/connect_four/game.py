from enum import Enum
from typing import Optional

from player import Player
from board import Board, BoardException


class GameError(Exception):
    pass


class GameState(Enum):
    IN_PROGRESS = 1
    DRAW = 2
    WON = 3


class Game:
    def __init__(self, board: Board, player1: Player, player2: Player):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.game_status = GameState.IN_PROGRESS
        self.winner: Optional[Player] = None
        self.current_player = player1

    def make_move(self, player: Player, row: int, col: int):
        if self.game_status != GameState.IN_PROGRESS:
            raise GameError("Game is already completed")

        if self.current_player is not player:
            raise GameError(f"Current player {player} cannot take a turn now.")

        try:
            (placed_row, placed_col) = self.board.place_disk(row, col, player.color)
        except BoardException as ex:
            raise GameError(f"Error in making move {ex}")

        if self.board.is_four_in_row(placed_row, placed_col):
            self.winner = player
            self.game_status = GameState.WON
            return

        if self.board.is_full():
            self.game_status = GameState.DRAW
            return

        if player is self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def get_state(self) -> GameState:
        return self.game_status

    def get_winner(self) -> Optional[Player]:
        return self.winner
