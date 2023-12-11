from inputs import read_input_file
from part2 import part2

sample_input_2a = read_input_file("2023/day10/sample-input-2a.txt")
sample_input_2b = read_input_file("2023/day10/sample-input-2b.txt")
sample_input_2c = read_input_file("2023/day10/sample-input-2c.txt")
sample_input_2d = read_input_file("2023/day10/sample-input-2d.txt")
actual_input = read_input_file("2023/day10/input.txt")


class TestPart2:
    def test_with_sample_data_2a(self):
        assert part2(sample_input_2a) == 4

    def test_with_sample_data_2b(self):
        assert part2(sample_input_2b) == 4

    def test_with_sample_data_2c(self):
        assert part2(sample_input_2c) == 8

    def test_with_sample_data_2d(self):
        assert part2(sample_input_2d) == 10

    def test_with_actual_data(self):
        # 242 too low
        assert part2(actual_input) == 435
