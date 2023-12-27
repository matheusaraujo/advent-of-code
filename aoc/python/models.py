from dataclasses import dataclass
from typing import List


@dataclass
class Example:
    example: str
    input_file: str
    output_file: str


@dataclass
class Part:
    solved: bool
    output_file: str
    examples: List[Example]


@dataclass
class Puzzle:
    title: str
    year: str
    day: str
    part1: Part
    part2: Part
    input_file: str

    def __str__(self):
        return f"AoC {self.year} Day {self.day} - {self.title}"
