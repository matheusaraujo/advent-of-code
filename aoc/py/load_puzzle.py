from aocd.models import Puzzle
from utils import (
    write_plain_txt_file,
    write_json_file,
    number_to_string,
    get_puzzle,
)


def load_puzzle(year, day):
    puzzle = Puzzle(year, day)

    file_prefix = f"data/{puzzle.year:04d}-{puzzle.day:02d}"

    puzzle_json = {
        "title": puzzle.title,
        "year": f"{puzzle.year:04d}",
        "day": f"{puzzle.day:02d}",
        "part1": {
            "solved": puzzle.answered_a,
            "output_file": f"{file_prefix}-part1.out" if puzzle.answered_a else None,
        },
        "part2": {
            "solved": puzzle.answered_b,
            "output_file": f"{file_prefix}-part2.out" if puzzle.answered_b else None,
        },
        "input_file": f"{file_prefix}.in",
    }

    for idx, example in enumerate(puzzle.examples):
        if example.answer_a is not None:
            write_plain_txt_file(
                f"{file_prefix}-part1-example-{number_to_string(idx)}.in",
                example.input_data,
            )
            write_plain_txt_file(
                f"{file_prefix}-part1-example-{number_to_string(idx)}.out",
                example.answer_a,
            )
        if example.answer_b is not None:
            write_plain_txt_file(
                f"{file_prefix}-part2-example-{number_to_string(idx)}.in",
                example.input_data,
            )
            write_plain_txt_file(
                f"{file_prefix}-part2-example-{number_to_string(idx)}.out",
                example.answer_b,
            )

    write_plain_txt_file(puzzle_json["input_file"], puzzle.input_data)

    if puzzle.answered_a:
        write_plain_txt_file(f"{file_prefix}-part1.out", puzzle.answer_a)

    if puzzle.answered_b:
        write_plain_txt_file(f"{file_prefix}-part2.out", puzzle.answer_b)

    write_json_file(f"{file_prefix}.json", puzzle_json)

    print("Puzzle loaded!")
    print(
        f"AOC {puzzle_json['year']} Day {puzzle_json['day']} - {puzzle_json['title']}"
    )


if __name__ == "__main__":
    arg_year, arg_day = get_puzzle()
    load_puzzle(arg_year, arg_day)
