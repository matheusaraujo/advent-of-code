import subprocess
from aocd.models import Puzzle


def run_example_part1_js(puzzle: Puzzle):
    print(f"> Running example cases for part 1 - js")

    for idx, example in enumerate(puzzle.examples):
        if example.answer_a is not None:
            process = subprocess.Popen(
                [
                    "node",
                    "/Users/matheus.araujo/github/advent-of-code/2015/day01/part1.js",
                ],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

            stdout, _ = process.communicate(input=example.input_data)

            output = stdout.strip()

            assert process.returncode == 0
            assert output == example.answer_a

            print(f">> Example {idx}, success")


def run_example_part1_python(puzzle: Puzzle):
    print(f"> Running example cases for part 1 - python")

    for idx, example in enumerate(puzzle.examples):
        if example.answer_a is not None:
            process = subprocess.Popen(
                [
                    "python3",
                    "/Users/matheus.araujo/github/advent-of-code/2015/day01/part1.py",
                ],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

            stdout, _ = process.communicate(input=example.input_data)

            output = stdout.strip()

            assert process.returncode == 0
            assert output == example.answer_a

            print(f">> Example {idx}, success")


if __name__ == "__main__":
    puzzle = Puzzle(2015, 1)

    print(f"AOC - {puzzle.year} Day {puzzle.day:02d} - {puzzle.title}")

    run_example_part1_python(puzzle)
    run_example_part1_js(puzzle)
