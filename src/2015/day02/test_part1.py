from inputs import read_input_file
from part1 import part1

actual_input = read_input_file("2015/day02/input.txt")
sample_input = read_input_file("2015/day02/sample-input.txt")


class Test2015Day02Part1:
    def test_with_sample_data(self):
        assert part1(sample_input) == 1

    def test_with_actual_data(self):
        assert part1(actual_input) == 42
