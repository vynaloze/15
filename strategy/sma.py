from sortedcontainers import SortedKeyList, SortedList

from strategy.api import SearchStrategy
from model.state import State


def list_to_string(var):
    return ','.join(str(node.value) for node in var)


class SMA(SearchStrategy):
    def solve(self, initial_state: State, heuristic: callable) -> State:

        def smart_heuristic(state: State):
            value = len(state.board_history) / 10 + heuristic(state)
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
                new_key = list_to_string(child.current_board.content)

                if not visited.get(new_key, False):
                    while len(state_list) > 100:
                        state_list.pop(-1)

                    state_list.add(child)
        return None
