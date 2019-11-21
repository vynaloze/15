from abc import ABC

from model.state import State


class SearchStrategy(ABC):
    def solve(self, initial_state: State) -> State:
        ...
