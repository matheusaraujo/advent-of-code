from inputs import read_input_file
from part1 import part1

LIMITS = "12 red, 13 green, 14 blue"
sample_input = read_input_file("2023/day02/sample-input.txt")
actual_input = read_input_file("2023/day02/input.txt")


class TestPart1:
    def test_with_sample_data(self):
        assert part1(sample_input, LIMITS) == 8

    def test_with_actual_data(self):
        assert part1(actual_input, LIMITS) == 2237
