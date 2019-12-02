from strategy.api import SearchStrategy
from model.state import State


class BestFirst(SearchStrategy):
    def solve(self, initial_state: State, heuristic) -> State:
        initial_state_score = {
            "state": initial_state,
            "score": 1000000
        }
        open_set = [initial_state_score]
        while open_set:
            scores = list(map(lambda x: x["score"], open_set))
            min_score = min(scores)
            best_states = list(filter(lambda x: x["score"] == min_score, open_set))
            new_open_set = list(filter(lambda x: x["score"] != min_score, open_set))
            for state in best_states:
                if state["state"].current_board.content == sorted(initial_state.current_board.content):
                    return state["state"]
                else:
                    for child in state["state"].next_states():
                        if child.current_board not in child.board_history:
                            new_open_set.append({
                                "state": child,
                                "score": heuristic(child)
                            })
                        else:
                            pass
            open_set = new_open_set
        return None
