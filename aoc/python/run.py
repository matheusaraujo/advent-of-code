import sys
import time

from models import Puzzle, Part
from utils import format_time
from utils_json import read_puzzle_from_json
from utils_txt_file import read_plain_txt_file

puzzle = read_puzzle_from_json(sys.argv[1])


sys.path.append(f"solutions/{puzzle.year}/day{puzzle.day}")

from part1 import part1
from part2 import part2


def run():
    print(f"python: Running {puzzle}")
    puzzle_input = read_plain_txt_file(puzzle.input_file)
    run_part1(puzzle_input)
    run_part2(puzzle_input)


def run_part1(puzzle_input):
    start_time1 = time.time()
    part1_received_answer = part1(puzzle_input)
    end_time1 = time.time()
    execution_time1 = end_time1 - start_time1
    print(
        f"\033[35mPart 1: \033[32m{part1_received_answer} "
        + f"\033[3;90m(executed in {format_time(execution_time1)}) \033[0m"
    )

    if puzzle.part1.solved:
        part1_expected_answer = read_plain_txt_file(puzzle.part1.output_file)
        assert str(part1_expected_answer) == str(part1_received_answer)


def run_part2(puzzle_input):
    start_time2 = time.time()
    part2_received_answer = part2(puzzle_input)
    end_time2 = time.time()
    execution_time2 = end_time2 - start_time2

    print(
        f"\033[35mPart 2: \033[32m{part2_received_answer} "
        + f"\033[3;90m(executed in {format_time(execution_time2)}) \033[0m"
    )

    if puzzle.part2.solved:
        part2_expected_answer = read_plain_txt_file(puzzle.part2.output_file)
        assert str(part2_expected_answer) == str(part2_received_answer)


if __name__ == "__main__":
    run()
