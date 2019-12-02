import argparse
from typing import Dict

from model.state import State
from solver.input import InputParser
from solver.output import OutputParser
from strategy.api import SearchStrategy
from strategy.astar import AStar
from strategy.best_first import BestFirst
from strategy.bfs import BFS
from strategy.dfs import DFS
from strategy.heuristics import h0, h1, h2
from strategy.idfs import IDFS
from strategy.sma import SMA


def strategies() -> Dict[str, SearchStrategy]:
    return {
        "bfs": BFS(),
        "dfs": DFS(),
        "idfs": IDFS(),
        "bf": BestFirst(),
        "astar": AStar(),
        "sma": SMA(),
    }


def heuristics() -> Dict[str, callable]:
    return {
        "h0": h0,
        "h1": h1,
        "h2": h2,
    }


def main():
    parser = argparse.ArgumentParser(add_help=False)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-b", "--bfs", dest="bfs", nargs='*', help="Breadth-first search")
    group.add_argument("-d", "--dfs", dest="dfs", nargs='*', help="Depth-first search")
    group.add_argument("-i", "--idfs", dest="idfs", nargs='*', help="Iterative deepenening DFS")
    group.add_argument("-h", "--bf", dest="bf", help="Breadth-first search")
    group.add_argument("-a", "--astar", dest="astar", help="A* strategy")
    group.add_argument("-s", "--sma", dest="sma", help="SMA* strategy")
    args = parser.parse_args()
    params = [(key, value) for key, value in vars(args).items() if value]
    if not params:
        raise ValueError(f"Did not choose any option.\n{parser.format_help()}")
    strategy_name, value = params[0]
    strategy = strategies().get(strategy_name)
    input_parser = InputParser()
    order = input_parser.parse_order(value) if strategy_name in ["bfs", "dfs", "idfs"] else None
    heuristic = heuristics().get(value) if strategy_name in ["bf", "astar", "sma"] else None
    initial_state = State(input_parser.parse_board(), move_order=order)

    output = strategy.solve(initial_state, heuristic)
    print(OutputParser.parse(output))


if __name__ == '__main__':
    main()
