from inputs import read_input_file
from part1 import part1

actual_input = read_input_file("2015/day03/input.txt")


class TestPart1:
    def test_with_sample_data(self):
        assert part1(">") == 2
        assert part1("v^v^v^v^v") == 2
        assert part1(">>") == 3
        assert part1(">><") == 3

    def test_with_actual_data(self):
        assert part1(actual_input[0]) == 2565