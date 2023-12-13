from inputs import read_input_file
from part1 import part1

sample_input_1 = read_input_file("2019/day06/sample-input-1.txt")
actual_input = read_input_file("2019/day06/input.txt")


class TestPart1:
    def test_with_sample_data_1(self):
        assert part1(sample_input_1) == 42

    def test_with_actual_data(self):
        assert part1(actual_input) == 247089
