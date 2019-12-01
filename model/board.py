from dataclasses import dataclass
from typing import List, Iterable

from model.node import Node, FreeNode


@dataclass(frozen=True)
class Board:
    content: List[Node]
    rows: int
    columns: int

    def free_node_position(self) -> int:
        return self.content.index(FreeNode)

    def free_node_row(self) -> int:
        for i in range(self.rows):
            if self.free_node_position() < self.columns * (i+1):
                return i

    def top_row(self) -> Iterable[int]:
        return range(self.rows)

    def bottom_row(self) -> Iterable[int]:
        bottom_left = (self.rows - 1) * self.columns
        return range(bottom_left, self.rows * self.columns)

    def left_col(self) -> Iterable[int]:
        return range(0, self.rows * self.columns, self.columns)

    def right_col(self) -> Iterable[int]:
        return range(self.columns - 1, self.columns * self.rows, self.columns)
