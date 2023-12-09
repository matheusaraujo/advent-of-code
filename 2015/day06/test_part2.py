from inputs import read_input_file
from part2 import part2

actual_input = read_input_file("2015/day06/input.txt")


class TestPart2:
    def test_with_sample_data(self):
        assert part2(["turn on 0,0 through 0,0"]) == 1

    def test_with_actual_data(self):
        assert part2(actual_input) == 14687245
