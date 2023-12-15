from inputs import read_input_file_as_string
from part1 import hashing, part1

sample_input = read_input_file_as_string("2023/day15/sample-input.txt")
actual_input = read_input_file_as_string("2023/day15/input.txt")


class TestPart1:
    def test_hashing(self):
        assert hashing("HASH") == 52

    def test_with_sample_data(self):
        assert part1(sample_input) == 1320

    def test_with_actual_data(self):
        assert part1(actual_input) == 506869
