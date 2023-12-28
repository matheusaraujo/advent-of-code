import sys
import time

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
    print(f"python: {puzzle.full_title}")
    puzzle_input = read_plain_txt_file(puzzle.input_file)

    run("Part 1", puzzle_input, part1, puzzle.part1.output_file)
    run("Part 2", puzzle_input, part2, puzzle.part2.output_file)


def run(part, puzzle_input, f, output_file):
    start_time1 = time.time()
    received_answer = f(puzzle_input)
    end_time1 = time.time()
    execution_time1 = end_time1 - start_time1

    checked, expected_answer = "", ""

    if output_file is not None:
        expected_answer = read_plain_txt_file(output_file)
        checked = (
            CHECK_SYMBOL
            if str(expected_answer) == str(received_answer)
            else CROSS_SYMBOL
        )

    print(
        f"{PURPLE}{part}: {GREEN}{received_answer} "
        + f"{GREY}(executed in {format_time(execution_time1)}) {RESET}"
        + checked
    )

    if checked is CROSS_SYMBOL:
        print(f"Failed! Expected result: {expected_answer}")
        sys.exit(1)


if __name__ == "__main__":
    main()
