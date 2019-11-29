from dataclasses import dataclass


@dataclass(frozen=True)
class Node:
    value: int

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


FreeNode = Node(0)
