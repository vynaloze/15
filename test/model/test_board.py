import unittest

from model.board import Board
from model.node import Node
from model.state import State


class TestState(unittest.TestCase):
    rows = 2
    cols = 2
    board1 = Board([Node(2), Node(1), Node(0), Node(3)], rows, cols)
    board2 = Board([Node(2), Node(1), Node(3), Node(0)], rows, cols)

    def test_solvable(self):
        # given
        initial_state = State(self.board1)

        # when
        solvability = initial_state.is_solvable()
        # then
        self.assertEqual(solvability, True)

    def test_unsolvable(self):
        # given
        initial_state = State(self.board2)

        # when
        solvability = initial_state.is_solvable()
        # then
        self.assertEqual(solvability, False)
