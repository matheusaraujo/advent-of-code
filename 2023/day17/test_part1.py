from inputs import read_input_file
from part1 import part1

sample_input_1a = read_input_file("2023/day17/sample-input-1a.txt")
actual_input = read_input_file("2023/day17/input.txt")


class TestPart1:
    def test_with_sample_data_1a(self):
        assert part1(sample_input_1a) == 102

    def test_with_actual_data(self):
        assert part1(actual_input) == 1110
