from dataclasses import dataclass
from typing import List

from model.board import Board
from model.move import Move


@dataclass
class Stepper:
    board: Board
    moves: List[Move]
    current_move: int

    def next(self, step: int = 1):
        if step + self.current_move > len(self.moves):
            raise ValueError(
                f"Too large step (wanted to move {step} steps, but there is only {len(self.moves) - self.current_move} left")
        for i in range(step):
            move = self.moves[self.current_move]
            self.board = move.apply(self.board)
            self.current_move += 1
