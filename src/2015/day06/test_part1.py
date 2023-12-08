from inputs import read_input_file
from part1 import part1

actual_input = read_input_file("2015/day06/input.txt")


class TestPart1:
    def test_with_sample_data(self):
        assert part1(["turn on 0,0 through 999,999"]) == 1_000_000

    def test_with_actual_data(self):
        assert part1(actual_input) == 543903
