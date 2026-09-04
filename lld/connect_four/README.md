## Problem statement
You need to create a game similar to connect four where there are players which take turn on putting disks
in a board from above. Whoever put four disk in a line, wins. If board is full, game is draw.

## Questions which can be asked
1. How to handle error input, for e.g wrong player taking turn or putting disk at already placed disk. 
2. At a time only one game will be played or we need to handle concurrent game as well?
3. How to tell a game has been won?
4. Do I need to handle UI operation as well?
5. Do we need to handle undo operation?
6. Is board size or number of player configurable?

## Requirements
1. In game, player should be able to take turn and place their disk.
2. In case a wrong move is made, error should be thrown.
3. Game need to track already placed disk.
4. Game should be done if either four disk are in line or board is full.


## Core entities and relationship
1. Game
2. Board
3. Player


## Class design
### Game
- board
- player1
- player2
- current_player
- winner
- state

+ game(board, player1, player2)
+ make_move(player, row, col)
   - check_valid_player
   - board.place_disk(row, col, player.disk)
   - board.is_four_in_row(row, col)
   - board.is_full()
+ get_state()
+ get_winner()

### board
- board(rows, cols)
- rows
- cols

+ is_valid_move(row, col)
+ place_disk(row, col, disk_color) -> (row, col)
+ is_four_in_row(row, col)
+ is_full()

### Player
- id
- disk_color
