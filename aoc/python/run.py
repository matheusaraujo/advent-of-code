import sys
import time
from models import Puzzle, Part

from utils import format_time
from utils_json import read_puzzle_from_json
from utils_txt_file import read_plain_txt_file

sys.path.append(sys.argv[1])

from part1 import part1
from part2 import part2

PURPLE = "\033[35m"
GREEN = "\033[32m"
GREY = "\033[3;90m"
RESET = "\033[0m"
RED = "\033[91m"
CHECK_SYMBOL = f"{GREEN}\u2714\uFE0E{RESET}"
CROSS_SYMBOL = f"{RED}\u2717\uFE0E{RESET}"


def main():
    puzzle = read_puzzle_from_json(sys.argv[2])
    mode = sys.argv[3]

    print(f"python({mode}): {puzzle.full_title}")

    modes_dict = {"part1": run_part1, "part2": run_part2, "solved": run_solved}

    modes_dict[mode](puzzle)


def run_part1(puzzle: Puzzle):
    run_part(puzzle.part1, part1)
    run(puzzle.part1.part, puzzle.input_file, part1)


def run_part2(puzzle: Puzzle):
    run_part(puzzle.part2, part2)
    run(puzzle.part2.part, puzzle.input_file, part2)


def run_part(part: Part, f):
    for example in part.examples:
        run(example.example, example.input_file, f, example.output_file)


def run_solved(puzzle: Puzzle):
    run(puzzle.part1.part, puzzle.input_file, part1, puzzle.part1.output_file)
    run(puzzle.part2.part, puzzle.input_file, part2, puzzle.part2.output_file)


def run(title, input_file, f, output_file=None):
    start_time = time.time()
    puzzle_input = read_plain_txt_file(input_file)
    received_answer = f(puzzle_input)
    end_time = time.time()
    execution_time = end_time - start_time

    if output_file is None:
        print_result(title, received_answer, execution_time)
    else:
        handle_expected_result(
            title, puzzle_input, output_file, received_answer, execution_time
        )


def handle_expected_result(
    part,
    puzzle_input,
    output_file,
    received_answer,
    execution_time,
):
    expected_answer = read_plain_txt_file(output_file)
    if str(received_answer) == str(expected_answer):
        print_result(part, received_answer, execution_time, CHECK_SYMBOL)
    else:
        print_result(part, received_answer, execution_time, CROSS_SYMBOL)
        print("Failed!")
        print(f"Input: {puzzle_input}")
        print(f"Expected: {expected_answer}")
        print(f"Received: {received_answer}")
        sys.exit(1)


def print_result(part, received_answer, execution_time, checked=None):
    print(
        f"{PURPLE}{part} "
        + f"{GREY}(executed in {format_time(execution_time)}) {RESET}"
        + f"{GREEN}{received_answer} "
        + (checked if checked is not None else "")
    )


if __name__ == "__main__":
    main()
