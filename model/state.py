from dataclasses import dataclass
from typing import List, Iterable

from model.board import Board
from model.move import Move, MoveUp, MoveDown, MoveLeft, MoveRight, IllegalMoveException


@dataclass
class State:
    move_history: List[Move]
    board_history: List[Board]
    current_board: Board
    _move_order: List[Move]

    def __init__(self, current_board: Board,
                 move_history: List[Move] = None,
                 board_history: List[Board] = None,
                 move_order: List[Move] = None):
        self.current_board = current_board
        self.move_history = move_history if move_history else []
        self.board_history = board_history if board_history else []
        self._move_order = move_order if move_order else [MoveUp(), MoveDown(), MoveLeft(), MoveRight()]

    def is_solvable(self) -> bool:
        inversions = self._inversions_count()
        rows, cols = self.current_board.rows, self.current_board.columns

        if rows % 2 == 1 and inversions % 2 == 0:
            return True
        else:
            if inversions % 2 == 1 and self.current_board.free_node_row() % 2 == 1:
                return True
            elif inversions % 2 == 0 and self.current_board.free_node_row() % 2 == 0:
                return True
        return False

    def _inversions_count(self) -> int:
        inversions = 0
        for i in range(len(self.current_board.content)):
            for j in range(i + 1, len(self.current_board.content)):
                if self.current_board.content[i] > self.current_board.content[j]:
                    inversions += 1
        return inversions

    def next_states(self) -> Iterable['State']:
        for move in self._move_order:
            try:
                yield self._next_state(move)
            except IllegalMoveException:
                pass

    def _next_state(self, move: Move) -> 'State':
        return State(
            move.apply(self.current_board),
            self.move_history + [move],
            self.board_history + [self.current_board],
            self._move_order
        )
