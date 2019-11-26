import os
import platform
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
    board_rows = [" ".join(row) for row in board_splitted]
    board = "\n".join(board_rows)

    os.system(clean_cmd)
    print(moves)
    print(message)
    print(board)
