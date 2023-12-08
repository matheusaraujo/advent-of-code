from inputs import read_input_file
from part1 import part1

actual_input = read_input_file("2015/day02/input.txt")


class TestPart1:
    def test_with_sample_data(self):
        assert part1(['2x3x4']) == 58
        assert part1(['1x1x10']) == 43

    def test_with_actual_data(self):
        assert part1(actual_input) == 1598415
