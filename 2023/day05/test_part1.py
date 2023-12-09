from inputs import read_input_file_as_string
from part1 import part1

actual_input = read_input_file_as_string("2023/day05/input.txt")
sample_input = read_input_file_as_string("2023/day05/sample-input.txt")


class TestPart1:
    def test_with_sample_data(self):
        assert part1(sample_input) == 35

    def test_with_actual_data(self):
        assert part1(actual_input) == 309796150
