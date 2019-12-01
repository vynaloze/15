from strategy.api import SearchStrategy
from model.state import State


class BFS(SearchStrategy):
    def solve(self, initial_state: State, heuristic) -> State:
        to_visit = [initial_state]
        while to_visit:
            new_to_visit = []
            for state in to_visit:
                if state.current_board.content == sorted(initial_state.current_board.content):
                    return state
                else:
                    for child in state.next_states():
                        new_to_visit.append(child)
            to_visit = new_to_visit
