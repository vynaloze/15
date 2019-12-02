from strategy.api import SearchStrategy
from model.state import State


class AStar(SearchStrategy):
    def solve(self, initial_state: State, heuristic) -> State:
        to_visit = [initial_state]
        while to_visit:
            new_to_visit = []
            new_best_score = 10000
            for state in to_visit:
                if state.current_board.content == sorted(initial_state.current_board.content):
                    return state
                else:
                    for child in state.next_states():
                        score = len(child.board_history) + heuristic(child)
                        if score < new_best_score and child.current_board not in child.board_history:
                            new_best_score = score
                            new_to_visit = [child]
                        elif score == new_best_score and child.current_board not in child.board_history:
                            new_to_visit.append(child)
                        else:
                            pass
            to_visit = new_to_visit
        return None
