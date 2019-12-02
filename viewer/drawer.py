import os
import platform
import functools
from typing import List

from model.board import Board
from model.move import Move


def draw(board: Board, prev_moves: List[Move], next_moves: List[Move], message: str = None):
    clean_cmd = "cls" if platform.system() == "Windows" else "clear"

    moves = " ".join(
        [move.step.value.lower() for move in prev_moves] + [">"] + [move.step.value for move in next_moves])
    message = "ERROR: " + message if message else ""
    board_splitted = [[str(node.value) for node in board.content[x:x + board.columns]] for x in
                      range(0, len(board.content), board.columns)]
    border = ["+-----------+"]
    board_rows = border
    for row in board_splitted:
        board_row = functools.reduce(lambda prev, curr: prev + curr + "|" if int(curr) > 9 else prev + "0" + curr + "|", row, "|")
        board_rows.append(board_row)

    board = "\n".join(board_rows + ["+-----------+"])
    os.system(clean_cmd)
    print(moves)
    print(message)
    print(board)
