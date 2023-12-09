from inputs import read_input_file
from part1 import is_nice_string, part1

actual_input = read_input_file("2015/day05/input.txt")


class TestPart1:
    def test_with_sample_data(self):
        assert is_nice_string("ugknbfddgicrmopn") is True
        assert is_nice_string("aaa") is True
        assert is_nice_string("jchzalrnumimnmhp") is False
        assert is_nice_string("haegwjzuvuyypxyu") is False
        assert is_nice_string("dvszwmarrgswjxmb") is False

    def test_with_actual_data(self):
        assert part1(actual_input) == 255
