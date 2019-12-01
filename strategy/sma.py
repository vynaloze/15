from sortedcontainers import SortedKeyList

from strategy.api import SearchStrategy
from model.state import State
from strategy.heuristics import h0, h1, h2


def list_to_string(list):
    return ','.join(str(node.value) for node in list)


class SMA(SearchStrategy):
    def solve(self, initial_state: State, heuristic: callable) -> State:

        def smart_heuristic(state: State):
            value = len(state.board_history) / 100 + heuristic(state)
            return value

        state_list = SortedKeyList(key=smart_heuristic)

        state_list.add(initial_state)
        visited = dict()

        while len(state_list) > 0:
            curr: State = state_list.pop(0)
            key = list_to_string(curr.current_board.content)

            visited[key] = True

            if curr.current_board.content == sorted(curr.current_board.content):
                return curr

            for child in curr.next_states():
                new_state = child
                new_key = list_to_string(new_state.current_board.content)

                if not visited.get(new_key, False):
                    if len(state_list) > 100:
                        state_list = state_list[:100]

                    state_list.add(new_state)
        return None
