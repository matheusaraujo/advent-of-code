import sys
from aocd.models import Puzzle as AocdPuzzle
from utils import number_to_string
from utils_json import write_puzzle_to_json
from utils_txt_file import write_plain_txt_file
from models import Puzzle, Part, Example


def load_puzzle(year, day):
    aocd_puzzle = AocdPuzzle(year, day)

    file_prefix = f"data/{aocd_puzzle.year:04d}/day{aocd_puzzle.day:02d}"

    puzzle = Puzzle(
        title=aocd_puzzle.title,
        year=f"{aocd_puzzle.year:04d}",
        day=f"{aocd_puzzle.day:02d}",
        input_file=f"{file_prefix}/puzzle.in",
        part1=Part(
            solved=aocd_puzzle.answered_a,
            output_file=f"{file_prefix}/part1.out" if aocd_puzzle.answered_a else None,
            examples=[],
        ),
        part2=Part(
            solved=aocd_puzzle.answered_b,
            output_file=f"{file_prefix}/part2.out" if aocd_puzzle.answered_b else None,
            examples=[],
        ),
    )

    for example in aocd_puzzle.examples:
        if example.answer_a is not None:
            idx = len(puzzle.part1.examples)
            input_file = f"{file_prefix}/part1.example-{number_to_string(idx)}.in"
            output_file = f"{file_prefix}/part1.example-{number_to_string(idx)}.out"
            write_plain_txt_file(input_file, example.input_data)
            write_plain_txt_file(output_file, example.answer_a)

        if example.answer_b is not None:
            idx = len(puzzle.part2.examples)
            input_file = f"{file_prefix}/part2.example-{number_to_string(idx)}.in"
            output_file = f"{file_prefix}/part2.example-{number_to_string(idx)}.out"
            write_plain_txt_file(input_file, example.input_data)
            write_plain_txt_file(output_file, example.answer_b)

    write_plain_txt_file(puzzle.input_file, aocd_puzzle.input_data)

    if aocd_puzzle.answered_a:
        write_plain_txt_file(f"{file_prefix}/part1.out", aocd_puzzle.answer_a)

    if aocd_puzzle.answered_b:
        write_plain_txt_file(f"{file_prefix}/part2.out", aocd_puzzle.answer_b)

    write_puzzle_to_json(f"{file_prefix}/data.json", puzzle)

    print(f"Puzzle loaded!\n{puzzle}")


if __name__ == "__main__":
    arg_year, arg_day = sys.argv[1], sys.argv[2]
    load_puzzle(int(arg_year), int(arg_day))
