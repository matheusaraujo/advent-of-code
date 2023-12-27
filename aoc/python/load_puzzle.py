import sys
from aocd.models import Puzzle
from utils import number_to_string, write_json_file, write_plain_txt_file


def load_puzzle(year, day):
    puzzle = Puzzle(year, day)

    file_prefix = f"data/{puzzle.year:04d}/day{puzzle.day:02d}"

    puzzle_json = {
        "title": puzzle.title,
        "year": f"{puzzle.year:04d}",
        "day": f"{puzzle.day:02d}",
        "part1": {
            "solved": puzzle.answered_a,
            "output_file": f"{file_prefix}/part1.out" if puzzle.answered_a else None,
            "examples": [],
        },
        "part2": {
            "solved": puzzle.answered_b,
            "output_file": f"{file_prefix}/part2.out" if puzzle.answered_b else None,
            "examples": [],
        },
        "input_file": f"{file_prefix}/puzzle.in",
    }

    for idx, example in enumerate(puzzle.examples):
        if example.answer_a is not None:
            input_file = f"{file_prefix}/part1.example-{number_to_string(idx)}.in"
            output_file = f"{file_prefix}/part1.example-{number_to_string(idx)}.out"
            write_plain_txt_file(input_file, example.input_data)
            write_plain_txt_file(output_file, example.answer_a)

            puzzle_json["part1"]["examples"].append(
                {
                    "example": number_to_string(idx),
                    "input_file": input_file,
                    "output_file": output_file,
                }
            )
        if example.answer_b is not None:
            input_file = f"{file_prefix}/part2.example-{number_to_string(idx)}.in"
            output_file = f"{file_prefix}/part2.example-{number_to_string(idx)}.out"
            write_plain_txt_file(input_file, example.input_data)
            write_plain_txt_file(output_file, example.answer_b)

            puzzle_json["part2"]["examples"].append(
                {
                    "example": number_to_string(idx),
                    "input_file": input_file,
                    "output_file": output_file,
                }
            )

    write_plain_txt_file(puzzle_json["input_file"], puzzle.input_data)

    if puzzle.answered_a:
        write_plain_txt_file(f"{file_prefix}/part1.out", puzzle.answer_a)

    if puzzle.answered_b:
        write_plain_txt_file(f"{file_prefix}/part2.out", puzzle.answer_b)

    write_json_file(f"{file_prefix}/data.json", puzzle_json)

    print("Puzzle loaded!")
    print(
        f"AoC {puzzle_json['year']} Day {puzzle_json['day']} - {puzzle_json['title']}"
    )


if __name__ == "__main__":
    arg_year, arg_day = sys.argv[1], sys.argv[2]
    load_puzzle(int(arg_year), int(arg_day))
