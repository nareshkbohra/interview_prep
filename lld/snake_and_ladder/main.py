import logging
import os
from game import SnakeAndLadder, Board, Jumper, Cell, Player, Dice


logger = logging.getLogger(__name__)


def setup_logging():
	log_level = os.environ.get("LOG_LEVEL") or "INFO"
	numeric_level = getattr(logging, log_level.upper(), None)

	if not isinstance(numeric_level, int):
		raise ValueError(f"Invalid log level: {log_level}")

	logging.basicConfig(level=numeric_level)


def main():
	setup_logging()
	logger.debug("Hello from snake-and-ladder!")

	snake_1 = Jumper(Cell(3, 5), Cell(1, 2))
	snake_2 = Jumper(Cell(8, 9), Cell(3, 9))
	ladder_1 = Jumper(Cell(4, 4), Cell(8, 8))
	ladder_2 = Jumper(Cell(8, 4), Cell(9, 9))
	jumpers = [snake_1, snake_2, ladder_1, ladder_2]
	board = Board(rows=10, cols=10, jumpers=jumpers)

	player_1 = Player(name="daksha", pid=1)
	player_2 = Player(name="naresh", pid=2)
	player_3 = Player(name="suresh", pid=3)
	players = [player_1, player_2, player_3]

	dice = Dice(7)
	snake_game = SnakeAndLadder(players=players, board=board, dice=dice)
	snake_game.start()


if __name__ == "__main__":
	main()
