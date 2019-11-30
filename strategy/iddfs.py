from strategy.api import SearchStrategy
from model.state import State


class IDDFS(SearchStrategy):
    def solve(self, initial_state: State) -> State:
        for level in range(0, 101): # change 101 to some overhead memory limit
            to_visit = [initial_state]
            while to_visit:
                curr = to_visit.pop()
                if len(curr.board_history) > level:
                    continue
                if curr.current_board.content == sorted(initial_state.current_board.content):
                    return curr
                else:
                    children = curr.next_states()
                    for child in children:
                        if child.current_board not in child.board_history:
                            if len(child.board_history) < level:
                                to_visit.append(child)
