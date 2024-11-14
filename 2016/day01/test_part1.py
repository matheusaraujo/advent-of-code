from inputs import read_input_file
from part1 import part1

sample_input_1a = read_input_file("2016/day01/sample-input-1a.txt")
sample_input_1b = read_input_file("2016/day01/sample-input-1b.txt")
sample_input_1c = read_input_file("2016/day01/sample-input-1c.txt")
actual_input = read_input_file("2016/day01/input.txt")


class TestPart1:
    def test_with_sample_data_a(self):
        assert part1(sample_input_1a) == 5

    def test_with_sample_data_b(self):
        assert part1(sample_input_1b) == 2

    def test_with_sample_data_c(self):
        assert part1(sample_input_1c) == 12

    def test_with_actual_data(self):
        assert part1(actual_input) == 161
