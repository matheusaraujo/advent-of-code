from inputs import read_input_file_as_string
from part1 import part1

sample_input_1a = read_input_file_as_string("2019/day07/sample-input-1a.txt")
sample_input_1b = read_input_file_as_string("2019/day07/sample-input-1b.txt")
sample_input_1c = read_input_file_as_string("2019/day07/sample-input-1c.txt")
actual_input = read_input_file_as_string("2019/day07/input.txt")


class TestPart1:
    def test_with_sample_data_1a(self):
        assert part1(sample_input_1a) == 43210

    def test_with_sample_data_1b(self):
        assert part1(sample_input_1b) == 54321

    def test_with_sample_data_1c(self):
        assert part1(sample_input_1c) == 65210

    def test_with_actual_data(self):
        assert part1(actual_input) == 17440
