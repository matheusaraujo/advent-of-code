from inputs import read_input_file
from part2 import part2

actual_input = read_input_file("2015/day02/input.txt")


class TestPart2:
    def test_with_sample_data_1(self):
        assert part2(["2x3x4"]) == 34

    def test_with_sample_data_2(self):
        assert part2(["1x1x10"]) == 14

    def test_with_actual_data(self):
        assert part2(actual_input) == 3812909
