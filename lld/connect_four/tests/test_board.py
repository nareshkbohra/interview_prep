from unittest import TestCase, main
from board import Board
from player import DiskColor


class TestBoard(TestCase):
    def setUp(self):
        self.board = Board()

    def test_is_full(self):
        board = Board(2, 2)
        self.assertFalse(board.is_full())

        board.place_disk(1, 0, DiskColor.YELLOW)
        board.place_disk(1, 0, DiskColor.YELLOW)
        board.place_disk(1, 1, DiskColor.YELLOW)
        board.place_disk(1, 1, DiskColor.YELLOW)
        self.assertTrue(board.is_full())

    def test_is_four_in_row(self):
        board = self.board

        (final_row, final_col) = (3, 6)
        self.assertTrue(board.is_four_in_row(final_row, final_col))

        board.place_disk(5, 6, DiskColor.YELLOW)
        board.place_disk(5, 6, DiskColor.YELLOW)
        board.place_disk(5, 6, DiskColor.YELLOW)
        (row, col) = board.place_disk(5, 6, DiskColor.YELLOW)

        self.assertEqual(row, final_row)
        self.assertEqual(col, final_col)
        self.assertTrue(board.is_four_in_row(final_row, final_col))


if __name__ == "__main__":
    main()
