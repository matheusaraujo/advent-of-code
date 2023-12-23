from inputs import read_input_file
from part2 import part2

sample_input = read_input_file("2023/day23/sample-input.txt")
actual_input = read_input_file("2023/day23/input.txt")


class TestPart2:
    def test_with_sample_data(self):
        assert part2(sample_input) == 154

    def test_with_actual_data(self):
        assert part2(actual_input) == 6418
