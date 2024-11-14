from inputs import read_input_file
from part2 import part2

sample_input_2a = read_input_file("2016/day01/sample-input-2a.txt")
actual_input = read_input_file("2016/day01/input.txt")


class TestPart2:
    def test_with_sample_data(self):
        assert part2(sample_input_2a) == 4

    def test_with_actual_data(self):
        assert part2(actual_input) == 110
