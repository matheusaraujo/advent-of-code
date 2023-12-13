from inputs import read_input_file
from part2 import part2

sample_input_2 = read_input_file("2019/day06/sample-input-2.txt")
actual_input = read_input_file("2019/day06/input.txt")


class TestPart2:
    def test_with_sample_data(self):
        assert part2(sample_input_2) == 4

    def test_with_actual_data(self):
        assert part2(actual_input) == 442
