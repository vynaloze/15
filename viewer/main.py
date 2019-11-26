import argparse

from model.move import IllegalMoveException
from viewer import drawer
from viewer.input_parser import InputParser
from viewer.stepper import Stepper


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--board", dest="board", required=True, help="Board file location")
    parser.add_argument("-s", "--solution", dest="solution", required=True, help="Solution file location")
    args = parser.parse_args()

    input_parser = InputParser()
    board = input_parser.parse_board(args.board)
    solution_moves = input_parser.parse_moves(args.solution)

    stepper = Stepper(board, solution_moves, 0)

    msg = [""]
    drawer.draw(stepper.board, stepper.moves[:stepper.current_move], stepper.moves[stepper.current_move:], msg[0])
    while stepper.current_move < len(solution_moves):
        step = input("\nNext step (default 1): ")
        try:
            if step == "":
                stepper.next()
            else:
                stepper.next(int(step))
            msg[0] = ""
        except (ValueError, IllegalMoveException) as e:
            msg[0] = str(e)
        drawer.draw(stepper.board, stepper.moves[:stepper.current_move], stepper.moves[stepper.current_move:], msg[0])


if __name__ == '__main__':
    main()
