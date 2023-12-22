from inputs import read_input_file
from part1 import part1

sample_input_1 = read_input_file("2023/day21/sample-input-1.txt")
actual_input = read_input_file("2023/day21/input.txt")


class TestPart1:
    def test_with_sample_data(self):
        assert part1(sample_input_1, 6) == 16

    def test_with_actual_data(self):
        assert part1(actual_input, 64) == 3809
