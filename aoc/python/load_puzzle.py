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
        full_title=f"AoC {aocd_puzzle.year:04d} Day {aocd_puzzle.day:02d} - {aocd_puzzle.title}",
        year=f"{aocd_puzzle.year:04d}",
        day=f"{aocd_puzzle.day:02d}",
        input_file=f"{file_prefix}/puzzle.in",
        part1=Part(
            part="Part 1",
            solved=aocd_puzzle.answered_a,
            output_file=f"{file_prefix}/part1.out" if aocd_puzzle.answered_a else None,
            examples=[],
        ),
        part2=Part(
            part="Part 2",
            solved=aocd_puzzle.answered_b,
            output_file=f"{file_prefix}/part2.out" if aocd_puzzle.answered_b else None,
            examples=[],
        ),
    )

    for example in aocd_puzzle.examples:
        if example.answer_a is not None:
            idx = number_to_string(len(puzzle.part1.examples))
            input_file = f"{file_prefix}/part1.example-{idx}.in"
            output_file = f"{file_prefix}/part1.example-{idx}.out"
            write_plain_txt_file(input_file, example.input_data)
            write_plain_txt_file(output_file, example.answer_a)
            puzzle.part1.examples.append(
                Example(f"Part 1 - Example {idx.upper()}", input_file, output_file)
            )

        if example.answer_b is not None:
            idx = number_to_string(len(puzzle.part2.examples))
            input_file = f"{file_prefix}/part2.example-{idx}.in"
            output_file = f"{file_prefix}/part2.example-{idx}.out"
            write_plain_txt_file(input_file, example.input_data)
            write_plain_txt_file(output_file, example.answer_b)
            puzzle.part2.examples.append(
                Example(f"Part 2 - Example {idx.upper()}", input_file, output_file)
            )

    write_plain_txt_file(puzzle.input_file, aocd_puzzle.input_data)

    if aocd_puzzle.answered_a:
        write_plain_txt_file(f"{file_prefix}/part1.out", aocd_puzzle.answer_a)

    if aocd_puzzle.answered_b:
        write_plain_txt_file(f"{file_prefix}/part2.out", aocd_puzzle.answer_b)

    write_puzzle_to_json(f"{file_prefix}/data.json", puzzle)

    print(puzzle.full_title)
    print("Puzzle loaded!")


if __name__ == "__main__":
    arg_year, arg_day = sys.argv[1], sys.argv[2]
    load_puzzle(int(arg_year), int(arg_day))
