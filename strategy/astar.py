from strategy.api import SearchStrategy
from model.state import State


class AStar(SearchStrategy):
    def solve(self, initial_state: State, heuristic) -> State:
        to_visit = [initial_state]
        depth = 0
        while to_visit:
            new_to_visit = []
            for state in to_visit:
                if state.current_board.content == sorted(initial_state.current_board.content):
                    return state
                else:
                    depth += 1
                    best_states = []
                    best_score = 1000000
                    for child in state.next_states():
                        score = depth + heuristic(child)
                        print(score)
                        if score < best_score:
                            best_score = score
                            best_states = [child]
                        elif score == best_score:
                            best_states.append(child)
                        else:
                            pass
                new_to_visit = new_to_visit + best_states
            to_visit = new_to_visit
        return None
