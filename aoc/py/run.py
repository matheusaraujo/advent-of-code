from utils import (
    import_puzzle_code,
    get_puzzle,
    read_json_file,
    read_plain_txt_file,
    format_time,
)
import time

arg_year, arg_day = get_puzzle()
import_puzzle_code(arg_year, arg_day)


from part1 import part1
from part2 import part2


def run(year, day):
    puzzle = read_json_file(f"data/{year}-{day:02d}.json")

    print(f"Running AOC {puzzle['year']} Day {puzzle['day']} - {puzzle['title']}")

    puzzle_input = read_plain_txt_file(puzzle["input_file"])

    part1_expected_answer = read_plain_txt_file(puzzle["part1"]["output_file"])

    start_time = time.time()
    part1_received_answer = part1(puzzle_input)
    end_time = time.time()

    execution_time = end_time - start_time
    print(
        f"\033[35mPart 1: \033[32m{part1_received_answer} \033[3;90m(executed in {format_time(execution_time)}) \033[0m"
    )

    assert str(part1_expected_answer) == str(part1_received_answer)

    part2_expected_answer = read_plain_txt_file(puzzle["part2"]["output_file"])

    start_time = time.time()
    part2_received_answer = part2(puzzle_input)
    end_time = time.time()

    print(
        f"\033[35mPart 2: \033[32m{part2_received_answer} \033[3;90m(executed in {format_time(execution_time)}) \033[0m"
    )

    assert str(part2_expected_answer) == str(part2_received_answer)


if __name__ == "__main__":
    run(arg_year, arg_day)
