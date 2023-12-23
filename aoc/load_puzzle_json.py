import json
import sys

from aocd.models import Puzzle

if len(sys.argv) < 3:
    print("year and day must be specified")
    print("  usage: python load_puzzle_json.py [year] [day]")
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


if __name__ == "__main__":
    puzzle = JsonPuzzle(year, day)
    puzzle.write_file()
    puzzle.write_example_files()
    puzzle.write_input()
