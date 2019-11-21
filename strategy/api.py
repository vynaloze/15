from typing import Protocol

from model.state import State


class SearchStrategy(Protocol):
    def solve(self, initial_state: State) -> State:
        ...
