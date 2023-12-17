import sys
import time

from aocd import get_data, submit
from aocd.models import Puzzle

if len(sys.argv) < 3:
    print("year and day must be specified")
    print("  usage: python run.py [year] [day]")
    sys.exit(1)

year = sys.argv[1]
day = sys.argv[2]

if not year.isnumeric() or not 2015 <= int(year) <= 2023:
    print("invalid [year]")
    sys.exit(1)

if not day.isnumeric() or not 1 <= int(day) <= 25:
    print("invalid [day]")
    sys.exit(1)

year, day = int(year), int(day)

sys.path.append(f"{year}/day{day:02d}")

from part1 import part1
from part2 import part2


def format_time(execution_time):
    if execution_time >= 1:
        return f"{execution_time:.2f}s"
    return f"{(execution_time * 1000):.2f}ms"


def timing_call(func, input_data):
    start_time = time.time()
    answer = func(input_data)
    end_time = time.time()
    return (answer, format_time(end_time - start_time))


def solve_puzzle_examples(puzzle, part_func, part_number):
    part_label = "a" if part_number == "1" else "b"

    for i, example in enumerate(puzzle.examples, start=1):
        if getattr(example, f"answer_{part_label}") is not None:
            (answer, execution_time) = timing_call(part_func, example.input_data)
            assert str(answer) == str(
                getattr(example, f"answer_{part_label}")
            ), f"part {part_number} - example {i} failed - {execution_time}"
            print(f"part {part_number} - example {i} successful - {execution_time}")


def solve_puzzle(puzzle, part_func, part_number):
    part_label = "a" if part_number == "1" else "b"

    if getattr(puzzle, f"answered_{part_label}"):
        (answer, execution_time) = timing_call(part_func, puzzle.input_data)
        assert str(answer) == str(
            getattr(puzzle, f"answer_{part_label}")
        ), f"part {part_number} failed - {execution_time}"
        print(f"part {part_number} - successful - {execution_time}")
    else:
        print("not solved yet")


def solve():
    puzzle = Puzzle(year, day)

    print(f"AoC - {year} Day {day:02d} - {puzzle.title}")

    solve_puzzle_examples(puzzle, part1, "1")
    solve_puzzle(puzzle, part1, "1")

    solve_puzzle_examples(puzzle, part2, "2")
    solve_puzzle(puzzle, part2, "2")

    print(f"AoC - {year} Day {day:02d} - {puzzle.title} - successful!")


if __name__ == "__main__":
    solve()
