from typing import List, Tuple

from model.board import Board
from model.move import Move, Step, MoveUp, MoveDown, MoveLeft, MoveRight
from model.node import Node


def parse_moves(input: List[str], allow_duplicates: bool) -> List[Move]:
    _default_moves: List[Move] = [MoveUp(), MoveDown(), MoveLeft(), MoveRight()]
    steps = [Step(s) for s in input]
    if not allow_duplicates and len(steps) != len(set(steps)):
        raise ValueError(f"Duplicate steps found: {steps}")
    return [m for step in steps for m in _default_moves if m.step == step]


def parse_board(lines: List[str]) -> Board:
    if len(lines) < 2:
        raise ValueError(f"Too short input. Expected at least 2 lines. Input:\n{lines}")
    rows, cols = _parse_counts(lines[0])
    content = [node for line in lines[1:] for node in _parse_content_row(line, cols)]
    if len(content) / cols != rows:
        raise ValueError(f"Invalid number of rows: expected={rows}, actual={len(content)}")
    return Board(content, rows, cols)


def _parse_counts(line: str) -> Tuple[int, int]:
    if len(line.split()) != 2:
        raise ValueError(f"Invalid input for row count and column count. Input:{line.rstrip()}")
    return int(line.split()[0]), int(line.split()[1])


def _parse_content_row(line: str, expected_cols: int) -> List[Node]:
    if len(line.split()) != expected_cols:
        raise ValueError(f"Invalid number of columns: expected={expected_cols}, actual={len(line.split())}")
    return [Node(int(x)) for x in line.split()]
