from inputs import read_input_file
from part2 import part2

actual_input = read_input_file("2023/day03/input.txt")
sample_input = read_input_file("2023/day03/sample-input.txt")


class TestPart2:
    def test_with_sample_data(self):
        assert part2(sample_input) == 467835

    def test_with_actual_data(self):
        assert part2(actual_input) == 67779080
