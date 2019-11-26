from typing import List

from model import parser
from model.board import Board
from model.move import Move


class InputParser:
    def parse_moves(self, filename: str) -> List[Move]:
        lines = []
        with open(filename, "r") as f:
            [lines.append(line) for line in f]
        solution_line = lines[1]
        return parser.parse_moves(list(solution_line), True)

    def parse_board(self, filename: str) -> Board:
        lines = []
        with open(filename, "r") as f:
            [lines.append(line) for line in f]
        return parser.parse_board(lines)
