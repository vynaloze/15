import unittest

from model.board import Board
from model.node import Node
from model.state import State
from strategy.idfs import IDFS
from model.move import MoveRight, MoveUp, MoveLeft, MoveDown


class TestState(unittest.TestCase):
    rows = 2
    cols = 2
    board1 = Board([Node(0), Node(1), Node(2), Node(3)], rows, cols)
    board2 = Board([Node(1), Node(0), Node(2), Node(3)], rows, cols)
    board3 = Board([Node(1), Node(3), Node(0), Node(2)], rows, cols)
    board33 = Board([Node(0), Node(2), Node(3), Node(4), Node(6), Node(5), Node(7), Node(8), Node(1)], 3, 3)
    state1 = State(board1)
    state2 = State(board2)
    state3 = State(board3)
    state33 = State(board33)

    def test_board_only(self):
        # given
        start_state = self.state2

        # when
        solved_state = IDFS().solve(start_state)

        # then
        self.assertListEqual(self.board1.content, solved_state.current_board.content)

    def test_whole_state(self):
        # given
        start_state = self.state2
        target_state = State(
            self.board1,
            [MoveLeft()],
            [self.board2]
        )

        # when
        solved_state = IDFS().solve(start_state)

        # then
        self.assertEqual(target_state, solved_state)

    def test_longer(self):
        start_state = self.state3

        # when
        solved_state = IDFS().solve(start_state)

        # then
        self.assertEqual(sorted(start_state.current_board.content), solved_state.current_board.content)

    def test_3x3(self):
        start_state = self.state33

        # when
        solved_state = IDFS().solve(start_state)

        # then
        self.assertEqual(sorted(start_state.current_board.content), solved_state.current_board.content)
