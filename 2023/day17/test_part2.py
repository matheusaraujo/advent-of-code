from inputs import read_input_file
from part2 import part2

sample_input_2a = read_input_file("2023/day17/sample-input-2a.txt")
sample_input_2b = read_input_file("2023/day17/sample-input-2b.txt")
actual_input = read_input_file("2023/day17/input.txt")


class TestPart2:
    def test_with_sample_data_2a(self):
        assert part2(sample_input_2a) == 94

    def test_with_sample_data_2b(self):
        assert part2(sample_input_2b) == 71

    def test_with_actual_data(self):
        assert part2(actual_input) == 1294
