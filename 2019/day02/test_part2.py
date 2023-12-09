from inputs import read_input_file_as_string
from part2 import part2

actual_input = read_input_file_as_string("2019/day02/input.txt")


class TestPart2:
    def test_with_sample_data(self):
        assert part2(actual_input, 5305097) == 1202

    def test_with_actual_data(self):
        assert part2(actual_input, 19690720) == 4925
