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
