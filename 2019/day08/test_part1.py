from inputs import read_input_file_as_string
from part1 import part1

actual_input = read_input_file_as_string("2019/day08/input.txt")


class TestPart1:
    def test_with_sample_data(self):
        assert part1("000000112156789422", 3, 3) == 2

    def test_with_actual_data(self):
        assert part1(actual_input, 25, 6) == 1485
