from unittest import TestCase, main

from game import Game, GameState, GameError
from player import Player, DiskColor
from board import Board


class TestGame(TestCase):
    def setUp(self):
        self.player1 = player1 = Player(1, DiskColor.RED)
        self.player2 = player2 = Player(2, DiskColor.YELLOW)
        self.board = board = Board()
        self.game = Game(board, player1, player2)

    def test_make_move_after_draw(self):
        game = self.game
        game.game_status = GameState.DRAW
        with self.assertRaises(GameError):
            game.make_move(self.player1, 1, 1)

    def test_wrong_player_turn(self):
        with self.assertRaises(GameError):
            self.game.make_move(self.player2, 1, 1)


if __name__ == "__main__":
    main()
