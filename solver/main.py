import argparse
from typing import Dict

from model.state import State
from solver.input import InputParser
from strategy.api import SearchStrategy


def strategies() -> Dict[str, SearchStrategy]:
    return {
        "bfs": SearchStrategy(),
        "dfs": SearchStrategy(),
        "idfs": SearchStrategy(),
        "bf": SearchStrategy(),
        "astar": SearchStrategy(),
        "sma": SearchStrategy(),
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
    # TODO parse id_of_heurisic
    initial_state = State(input_parser.parse_board(), move_order=order)

    print(initial_state)
    # TODO output = strategy.solve(initial_state)

    # TODO print output


if __name__ == '__main__':
    main()
