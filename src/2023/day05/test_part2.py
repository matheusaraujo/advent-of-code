from inputs import read_input_file_as_string
from part2 import part2

actual_input = read_input_file_as_string("2023/day05/input.txt")
sample_input = read_input_file_as_string("2023/day05/sample-input.txt")


class TestPart2:
    def test_with_sample_data(self):
        assert part2(sample_input) == 46

    def test_with_actual_data(self):
        assert part2(actual_input) == 50716416
