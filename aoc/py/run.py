import time

from utils import (
    format_time,
    get_puzzle,
    import_puzzle_code,
    read_json_file,
    read_plain_txt_file,
)


arg_year, arg_day = get_puzzle()
import_puzzle_code(arg_year, arg_day)


from part1 import part1
from part2 import part2


def run(year, day):
    puzzle = read_json_file(f"data/{year}-{day:02d}.json")

    print(
        f"python: Running AoC {puzzle['year']} Day {puzzle['day']} - {puzzle['title']}"
    )

    puzzle_input = read_plain_txt_file(puzzle["inputFile"])

    part1_expected_answer = read_plain_txt_file(puzzle["part1"]["outputFile"])

    start_time1 = time.time()
    part1_received_answer = part1(puzzle_input)
    end_time1 = time.time()

    execution_time1 = end_time1 - start_time1
    print(
        f"\033[35mPart 1: \033[32m{part1_received_answer} "
        + f"\033[3;90m(executed in {format_time(execution_time1)}) \033[0m"
    )

    assert str(part1_expected_answer) == str(part1_received_answer)

    part2_expected_answer = read_plain_txt_file(puzzle["part2"]["outputFile"])

    start_time2 = time.time()
    part2_received_answer = part2(puzzle_input)
    end_time2 = time.time()
    execution_time2 = end_time2 - start_time2

    print(
        f"\033[35mPart 2: \033[32m{part2_received_answer} "
        + f"\033[3;90m(executed in {format_time(execution_time2)}) \033[0m"
    )

    assert str(part2_expected_answer) == str(part2_received_answer)


if __name__ == "__main__":
    print()
    # run(arg_year, arg_day)
