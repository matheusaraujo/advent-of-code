from inputs import read_input_file
from part1 import part1

actual_input = read_input_file("2017/day01/input.txt")


class TestPart1:
    def test_with_sample_data_1(self):
        assert part1(["1122"]) == 3

    def test_with_sample_data_2(self):
        assert part1(["1111"]) == 4

    def test_with_sample_data_3(self):
        assert part1(["1234"]) == 0

    def test_with_sample_data_4(self):
        assert part1(["91212129"]) == 9

    def test_with_actual_data(self):
        assert part1(actual_input) == 1182
