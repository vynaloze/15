from dataclasses import dataclass


@dataclass(frozen=True)
class Node:
    value: int


FreeNode = Node(0)
