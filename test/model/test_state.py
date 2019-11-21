import unittest
from typing import List

from model.board import Board
from model.move import MoveRight, MoveDown, MoveUp, MoveLeft
from model.node import Node
from model.state import State


class TestState(unittest.TestCase):
    rows = 2
    cols = 2
    board1 = Board([Node(0), Node(1), Node(2), Node(3)], rows, cols)
    board11 = Board([Node(1), Node(0), Node(2), Node(3)], rows, cols)
    board12 = Board([Node(2), Node(1), Node(0), Node(3)], rows, cols)
    board111 = Board([Node(0), Node(1), Node(2), Node(3)], rows, cols)
    board112 = Board([Node(1), Node(3), Node(2), Node(0)], rows, cols)
    board121 = Board([Node(0), Node(1), Node(2), Node(3)], rows, cols)
    board122 = Board([Node(2), Node(1), Node(3), Node(0)], rows, cols)

    def test_single_iteration(self):
        # given
        initial_state = State(self.board1)
        expected_states = [
            State(
                self.board12,
                [MoveDown()],
                [self.board1]
            ),
            State(
                self.board11,
                [MoveRight()],
                [self.board1]
            ),
        ]
        # when
        states = self._iterate(initial_state)
        # then
        self.assertListEqual(states, expected_states)

    def test_two_iterations(self):
        # given
        initial_state = State(self.board1)
        expected_states = [
            State(
                self.board121,
                [MoveDown(), MoveUp()],
                [self.board1, self.board12]
            ),
            State(
                self.board122,
                [MoveDown(), MoveRight()],
                [self.board1, self.board12]
            ),
            State(
                self.board112,
                [MoveRight(), MoveDown()],
                [self.board1, self.board11]
            ),
            State(
                self.board111,
                [MoveRight(), MoveLeft()],
                [self.board1, self.board11]
            ),
        ]
        # when
        states1 = self._iterate(initial_state)
        states2 = [s for states in states1 for s in self._iterate(states)]
        # then
        self.assertListEqual(states2, expected_states)

    def _iterate(self, state: State) -> List[State]:
        states = []
        for s in state.next_states():
            states.append(s)
        return states
