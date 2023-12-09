from inputs import read_input_file
from part2 import part2

actual_input = read_input_file("2015/day03/input.txt")


class TestPart2:
    def test_with_sample_data(self):
        assert part2("^v") == 3
        assert part2("^>v<") == 3
        assert part2("^v^v^v^v^v") == 11

    def test_with_actual_data(self):
        assert part2(actual_input[0]) == 2639
