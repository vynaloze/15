from strategy.api import SearchStrategy
from model.state import State


class DFS(SearchStrategy):
    def solve(self, initial_state: State, heuristic) -> State:
        to_visit = [initial_state]
        while to_visit:
            curr = to_visit.pop()
            if curr.current_board.content == sorted(initial_state.current_board.content):
                return curr
            else:
                children = curr.next_states()
                for child in children:
                    if child.current_board not in child.board_history:
                        to_visit.append(child)
                    else:
                        pass
