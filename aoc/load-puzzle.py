import json
import sys

from aocd.models import Puzzle

year, day = int(sys.argv[1]), int(sys.argv[2])


class JsonPuzzle(Puzzle):
    def to_json(self):
        return {
            "year": str(self.year),
            "day": str(self.day).zfill(2),
            "title": self.title,
            "part_1": {
                "done": self.answered_a,
                "answer": self.answer_a,
            },
            "part_2": {
                "done": self.answered_b,
                "answer": self.answer_b,
            },
        }

    def write_file(self):
        file_path = f"{self.year}-{self.day:02d}.puzzle.json"

        with open(file_path, "w") as json_file:
            json.dump(self.to_json(), json_file, indent=4)

    def write_input(self):
        file_path = f"{self.year}-{self.day:02d}.puzzle.in"

        with open(file_path, "w") as input_file:
            input_file.write(self.input_data)

    def write_example_files(self):
        idx = 1
        for example in self.examples:
            if example.answer_a is not None:
                self.write_example_file("1", idx, example.input_data)
                idx += 1

        idx = 1
        for example in self.examples:
            if example.answer_b is not None:
                self.write_example_file("2", idx, example.input_data)
                idx += 1

    def write_example_file(self, part, idx_example, input_data):
        file_path = f"{self.year}-{self.day:02d}-part{part}-{idx_example}.puzzle.in"

        with open(file_path, "w") as input_file:
            input_file.write(input_data)


def write_plain_txt_file(file_name, content):
    with open(f"data/{file_name}", "w", encoding="utf-8") as file:
        file.write(content)


def write_json_file(file_name, content):
    with open(f"data/{file_name}", "w", encoding="utf-8") as json_file:
        json.dump(content, json_file, indent=4)


def number_to_string(n):
    n += 1
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = ""
    while n > 0:
        remainder = (n - 1) % 26
        result = alphabet[remainder] + result
        n = (n - 1) // 26

    return result


if __name__ == "__main__":
    puzzle = Puzzle(year, day)

    file_prefix = f"{puzzle.year:04d}-{puzzle.day:02d}"

    puzzle_json = {
        "title": puzzle.title,
        "year": f"{puzzle.year:04d}",
        "day": f"{puzzle.day:02d}",
        "part1": {"solved": puzzle.answered_a},
        "part2": {"solved": puzzle.answered_b},
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

    write_plain_txt_file(f"{file_prefix}.in", puzzle.input_data)

    if puzzle.answered_a:
        write_plain_txt_file(f"{file_prefix}-part1.out", puzzle.answer_a)

    if puzzle.answered_b:
        write_plain_txt_file(f"{file_prefix}-part2.out", puzzle.answer_b)

    write_json_file(f"{file_prefix}.json", puzzle_json)
