import random
import sys
from typing import Tuple, List

from model.board import Board
from model.move import Move, Step, MoveUp, MoveDown, MoveLeft, MoveRight
from model.node import Node


class InputParser:
    _default_moves: List[Move] = [MoveUp(), MoveDown(), MoveLeft(), MoveRight()]

    def parse_order(self, input: List[str]) -> List[Move]:
        if input == ['R']:
            moves = list(self._default_moves)
            random.shuffle(moves)
            return moves

        if len(input) != 4:
            raise ValueError(f"Invalid number of moves: expected=4, actual={len(input)}. Input:{input}")
        steps = [Step(s) for s in input]
        if len(steps) != len(set(steps)):
            raise ValueError(f"Duplicate steps found: {steps}")
        return [m for step in steps for m in self._default_moves if m.step == step]

    def parse_board(self) -> Board:
        lines = [line for line in sys.stdin if sys.stdin]
        if len(lines) < 2:
            raise ValueError(f"Too short input. Expected at least 2 lines. Input:\n{lines}")
        rows, cols = self._parse_counts(lines[0])
        content = [node for line in lines[1:] for node in self._parse_content_row(line, cols)]
        if len(content) / cols != rows:
            raise ValueError(f"Invalid number of rows: expected={rows}, actual={len(content)}")
        return Board(content, rows, cols)

    @staticmethod
    def _parse_counts(line: str) -> Tuple[int, int]:
        if len(line.split()) != 2:
            raise ValueError(f"Invalid input for row count and column count. Input:{line.rstrip()}")
        return int(line.split()[0]), int(line.split()[1])

    @staticmethod
    def _parse_content_row(line: str, expected_cols: int) -> List[Node]:
        if len(line.split()) != expected_cols:
            raise ValueError(f"Invalid number of columns: expected={expected_cols}, actual={len(line.split())}")
        return [Node(int(x)) for x in line.split()]
