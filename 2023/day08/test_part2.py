from inputs import read_input_file
from part2 import part2

actual_input = read_input_file("2023/day08/input.txt")
sample_input_1b = read_input_file("2023/day08/sample-input-1b.txt")


class TestPart2:
    def test_with_sample_data(self):
        assert part2(sample_input_1b) == 6

    def test_with_actual_data(self):
        assert part2(actual_input) == 10668805667831
