from inputs import read_input_file
from part1 import part1

actual_input = read_input_file("2015/day04/input.txt")


class TestPart1:
    def test_with_sample_data(self):
        assert part1("abcdef") == 609043
        assert part1("pqrstuv") == 1048970

    def test_with_actual_data(self):
        assert part1(actual_input[0]) == 254575
