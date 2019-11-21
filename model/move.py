from abc import ABC, abstractmethod
from enum import Enum

from model.board import Board


class Step(Enum):
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"


class IllegalMoveException(Exception):
    pass


class Move(ABC):
    def __init__(self, step: Step):
        self.step: Step = step

    @abstractmethod
    def apply(self, board: Board) -> Board:
        ...

    @staticmethod
    def _flip_positions(board: Board, old_pos: int, new_pos: int) -> Board:
        new_board = list(board.content)
        new_board[old_pos], new_board[new_pos] = new_board[new_pos], new_board[old_pos]
        return Board(new_board, board.rows, board.columns)

    def __str__(self) -> str:
        return str(self.step)

    def __repr__(self) -> str:
        return str(self.step)

    def __eq__(self, o: object) -> bool:
        return isinstance(o, self.__class__) and self.step == o.step


class MoveUp(Move):
    def __init__(self):
        super().__init__(Step.UP)

    def apply(self, board: Board) -> Board:
        pos = board.free_node_position()
        if pos in board.top_row():
            raise IllegalMoveException(f"Cannot apply move {self.step}")
        return super()._flip_positions(board, pos, pos - board.columns)


class MoveDown(Move):
    def __init__(self):
        super().__init__(Step.DOWN)

    def apply(self, board: Board) -> Board:
        pos = board.free_node_position()
        if pos in board.bottom_row():
            raise IllegalMoveException(f"Cannot apply move {self.step}")
        return super()._flip_positions(board, pos, pos + board.columns)


class MoveLeft(Move):
    def __init__(self):
        super().__init__(Step.LEFT)

    def apply(self, board: Board) -> Board:
        pos = board.free_node_position()
        if pos in board.left_col():
            raise IllegalMoveException(f"Cannot apply move {self.step}")
        return super()._flip_positions(board, pos, pos - 1)


class MoveRight(Move):
    def __init__(self):
        super().__init__(Step.RIGHT)

    def apply(self, board: Board) -> Board:
        pos = board.free_node_position()
        if pos in board.right_col():
            raise IllegalMoveException(f"Cannot apply move {self.step}")
        return super()._flip_positions(board, pos, pos + 1)
