from inputs import read_input_file
from part2 import part2

actual_input = read_input_file("2023/day08/input.txt")
sample_input_b = read_input_file("2023/day08/sample-input-b.txt")
sample_input_c = read_input_file("2023/day08/sample-input-c.txt")


class TestPart2:
    def test_with_sample_data_b(self):
        assert part2(sample_input_b) == 6

    def test_with_sample_data_c(self):
        assert part2(sample_input_c) == 6

    def test_with_actual_data(self):
        assert part2(actual_input) == 10668805667831
