from inputs import read_input_file
from part2 import part2

sample_input = read_input_file("2023/day01/sample-input-2.txt")
actual_input = read_input_file("2023/day01/input.txt")


class TestPart2:
    def test_with_sample_data(self):
        assert part2(sample_input) == 281

    def test_with_actual_data(self):
        assert part2(actual_input) == 53515
