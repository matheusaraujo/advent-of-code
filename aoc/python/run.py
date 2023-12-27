import sys
import time

from utils import format_time
from utils_json import read_puzzle_from_json
from utils_txt_file import read_plain_txt_file

sys.path.append(sys.argv[1])

from part1 import part1
from part2 import part2


def main():
    puzzle = read_puzzle_from_json(sys.argv[2])
    print(f"python: {puzzle.full_title}")
    puzzle_input = read_plain_txt_file(puzzle.input_file)

    run("Part 1", puzzle_input, part1, puzzle.part1.output_file, puzzle.part1.solved)
    run("Part 2", puzzle_input, part2, puzzle.part2.output_file, puzzle.part2.solved)


def run(part, puzzle_input, f, output_file, solved):
    start_time1 = time.time()
    received_answer = f(puzzle_input)
    end_time1 = time.time()
    execution_time1 = end_time1 - start_time1
    print(
        f"\033[35m{part}: \033[32m{received_answer} "
        + f"\033[3;90m(executed in {format_time(execution_time1)}) \033[0m"
    )

    if solved:
        expected_answer = read_plain_txt_file(output_file)
        assert str(expected_answer) == str(received_answer)


if __name__ == "__main__":
    main()
