import sys
import time

from utils import format_time, read_plain_txt_file


puzzle = {}


def load_puzzle_from_args():
    for arg in sys.argv:
        k = arg.split("=")
        if len(k) == 2:
            puzzle[k[0]] = k[1]

    assert puzzle["year"] is not None
    assert puzzle["day"] is not None
    assert puzzle["title"] is not None
    assert puzzle["input_file"] is not None
    assert puzzle["part1_solved"] is not None
    assert puzzle["part1_output_file"] is not None
    assert puzzle["part2_solved"] is not None
    assert puzzle["part2_output_file"] is not None


load_puzzle_from_args()
sys.path.append(f"{puzzle['year']}/day{puzzle['day']}")

from part1 import part1
from part2 import part2


def run_part1(puzzle_input):
    start_time1 = time.time()
    part1_received_answer = part1(puzzle_input)
    end_time1 = time.time()
    execution_time1 = end_time1 - start_time1
    print(
        f"\033[35mPart 1: \033[32m{part1_received_answer} "
        + f"\033[3;90m(executed in {format_time(execution_time1)}) \033[0m"
    )

    if puzzle["part1_solved"]:
        part1_expected_answer = read_plain_txt_file(puzzle["part1_output_file"])
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

    if puzzle["part2_solved"]:
        part2_expected_answer = read_plain_txt_file(puzzle["part2_output_file"])
        assert str(part2_expected_answer) == str(part2_received_answer)


def run():
    print(
        f"python: Running AoC {puzzle['year']} Day {puzzle['day']} - {puzzle['title']}"
    )
    puzzle_input = read_plain_txt_file(puzzle["input_file"])

    run_part1(puzzle_input)
    run_part2(puzzle_input)


if __name__ == "__main__":
    run()
