from inputs import read_input_file
from part1 import part1

sample_input = read_input_file("2023/day14/sample-input.txt")
actual_input = read_input_file("2023/day14/input.txt")


class TestPart1:
    def test_with_sample_data(self):
        assert part1(sample_input) == 136

    def test_with_actual_data(self):
        assert part1(actual_input) == 110274
