import unittest

from model.board import Board
from model.node import Node
from model.state import State
from strategy.best_first import BestFirst
from strategy.sma import SMA
from model.move import MoveRight, MoveUp, MoveLeft, MoveDown
from strategy.heuristics import h0, h1, h2


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

    def test_whole_state_h0(self):
        # given
        start_state = self.state2
        target_state = State(
            self.board1,
            [MoveLeft()],
            [self.board2]
        )

        # when
        solved_state = BestFirst().solve(start_state, h0)

        # then
        self.assertEqual(target_state, solved_state)

    def test_longer_h1(self):
        # given
        start_state = self.state3

        # when
        solved_state = BestFirst().solve(start_state, h1)

        # then
        self.assertEqual(sorted(start_state.current_board.content), solved_state.current_board.content)

    def test_longer_h2(self):
        # given
        start_state = self.state3

        # when
        solved_state = BestFirst().solve(start_state, h2)

        # then
        self.assertEqual(sorted(start_state.current_board.content), solved_state.current_board.content)

    def text_3x3_h0(self):
        # given
        start_state = self.state33

        # when
        solved_state = BestFirst().solve(start_state, h0)

        # then
        self.assertEqual(sorted(start_state.current_board.content), solved_state.current_board.content)

    def test_3x3_h1(self):
        start_state = self.state33

        # when
        solved_state = BestFirst().solve(start_state, h1)

        # then
        self.assertEqual(sorted(start_state.current_board.content), solved_state.current_board.content)

    def test_3x3_h2(self):
        # given
        start_state = self.state33

        # when
        solved_state = BestFirst().solve(start_state, h2)

        # then
        self.assertEqual(sorted(start_state.current_board.content), solved_state.current_board.content)
