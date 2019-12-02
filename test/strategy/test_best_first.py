import unittest

from model.board import Board
from model.node import Node
from model.state import State
from strategy.best_first import BestFirst
from strategy.heuristics import h0, h1, h2


class TestState(unittest.TestCase):
    rows = 4
    cols = 4
    board1 = Board(
        [
         Node(0),
         Node(1),
         Node(2),
         Node(3),
         Node(4),
         Node(5),
         Node(6),
         Node(7),
         Node(8),
         Node(9),
         Node(10),
         Node(11),
         Node(12),
         Node(13),
         Node(14),
         Node(15),
         ],
        rows,
        cols
    )
    board2 = Board(
        [Node(1),
         Node(0),
         Node(2),
         Node(3),
         Node(4),
         Node(5),
         Node(6),
         Node(7),
         Node(8),
         Node(9),
         Node(10),
         Node(11),
         Node(12),
         Node(13),
         Node(14),
         Node(15),
         ],
        rows,
        cols
    )
    board3 = Board(
        [Node(1),
         Node(0),
         Node(2),
         Node(3),
         Node(4),
         Node(5),
         Node(6),
         Node(7),
         Node(8),
         Node(9),
         Node(10),
         Node(11),
         Node(12),
         Node(13),
         Node(14),
         Node(15),
         ],
        rows,
        cols
    )
    state1 = State(board1)
    state2 = State(board2)
    state3 = State(board3)

    def test_board_only_h0(self):
        # given
        start_state = self.state2

        # when
        solved_state = BestFirst().solve(start_state, h0)

        # then
        self.assertEqual(self.state1.current_board.content, solved_state.current_board.content)

    def test_board_only_h1(self):
        # given
        start_state = self.state2

        # when
        solved_state = BestFirst().solve(start_state, h1)

        # then
        self.assertEqual(self.state1.current_board.content, solved_state.current_board.content)

    def test_board_only_h2(self):
        # given
        start_state = self.state2

        # when
        solved_state = BestFirst().solve(start_state, h2)

        # then
        self.assertEqual(self.state1.current_board.content, solved_state.current_board.content)
