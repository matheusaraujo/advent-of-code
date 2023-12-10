from inputs import read_input_file
from part1 import part1

sample_input_a = read_input_file("2019/day03/sample-input-a.txt")
sample_input_b = read_input_file("2019/day03/sample-input-b.txt")
sample_input_c = read_input_file("2019/day03/sample-input-c.txt")
actual_input = read_input_file("2019/day03/input.txt")


class TestPart1:
    def test_with_sample_data_a(self):
        assert part1(sample_input_a) == 6

    def test_with_sample_data_b(self):
        assert part1(sample_input_b) == 159

    def test_with_sample_data_c(self):
        assert part1(sample_input_c) == 135

    def test_with_actual_data(self):
        assert part1(actual_input) == 446
