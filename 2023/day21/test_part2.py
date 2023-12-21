from inputs import read_input_file
from part2 import part2

actual_input = read_input_file("2023/day21/input.txt")


# pylint: disable=too-few-public-methods
class TestPart2:
    def test_with_actual_data(self):
        assert part2(actual_input, 26501365) == 629720570456311
