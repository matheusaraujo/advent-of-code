from inputs import read_input_file
from part2 import part2

sample_input = read_input_file("2023/day04/sample-input.txt")
actual_input = read_input_file("2023/day04/input.txt")


class TestPart2:
    def test_with_sample_data(self):
        assert part2(sample_input) == 30

    def test_with_actual_data(self):
        assert part2(actual_input) == 7258152
