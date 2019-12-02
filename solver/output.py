from typing import Optional

from model.state import State


class OutputParser:
    @staticmethod
    def parse(state: Optional[State]) -> str:
        if not state:
            return "-1\n\n"
        length = str(len(state.move_history))
        moves = "".join([move.step.value for move in state.move_history])
        return f"{length}\n{moves}"
