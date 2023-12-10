from inputs import read_input_file
from part1 import part1

actual_input = read_input_file("2023/day08/input.txt")
sample_input_a = read_input_file("2023/day08/sample-input-a.txt")
sample_input_b = read_input_file("2023/day08/sample-input-b.txt")


class TestPart1:
    def test_with_sample_data_a(self):
        assert part1(sample_input_a) == 2

    def test_with_sample_data_b(self):
        assert part1(sample_input_b) == 6

    def test_with_actual_data(self):
        assert part1(actual_input) == 16697
