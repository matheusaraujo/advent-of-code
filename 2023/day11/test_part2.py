from inputs import read_input_file
from part2 import part2

sample_input = read_input_file("2023/day11/sample-input.txt")
actual_input = read_input_file("2023/day11/input.txt")


class TestPart2:
    def test_with_sample_data_a(self):
        assert part2(sample_input, 10) == 1030

    def test_with_sample_data_b(self):
        assert part2(sample_input, 100) == 8410

    def test_with_actual_data(self):
        assert part2(actual_input, 1000000) == 678728808158
