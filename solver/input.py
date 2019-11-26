import random
import sys
from typing import List

from model import parser
from model.board import Board
from model.move import Move, MoveUp, MoveDown, MoveLeft, MoveRight


class InputParser:
    _default_moves: List[Move] = [MoveUp(), MoveDown(), MoveLeft(), MoveRight()]

    def parse_order(self, input: List[str]) -> List[Move]:
        if input == ['R']:
            moves = list(self._default_moves)
            random.shuffle(moves)
            return moves
        if len(input) != 4:
            raise ValueError(f"Invalid number of moves: expected=4, actual={len(input)}. Input:{input}")
        return parser.parse_moves(input, False)

    def parse_board(self) -> Board:
        lines = [line for line in sys.stdin if sys.stdin]
        return parser.parse_board(lines)
