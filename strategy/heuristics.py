from model.state import State
import numpy as np


def getf(func):
    def f(state: State):
        return g(state) + func(state)

    return f


def g(state: State):
    return len(state.board_history)


# The h(x) = 0 heuristic
def h0(state: State):
    return 0


# The "number of misplaced tiles" heuristic
def h1(state: State):
    board_sequence = state.current_board.content
    count = 0
    for i in range(len(board_sequence)):
        if i != board_sequence[i].value:
            count += 1
    return count


# Sums the distances of all tiles from their correct positions (see: taxicab geometry)
def h2(state: State):
    rows = state.current_board.rows
    cols = state.current_board.columns
    board_sequence = np.array(state.current_board.content)
    board_sequence = np.reshape(board_sequence, (rows, cols))
    count = 0
    for i in range(rows):
        for j in range(cols):
            if board_sequence[i][j].value != 0:
                count += abs(i - ((board_sequence[i][j].value - 1) // rows)) + abs(j - ((board_sequence[i][j].value - 1) % cols))
    return count
