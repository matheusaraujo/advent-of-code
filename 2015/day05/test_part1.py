from inputs import read_input_file
from part1 import is_nice_string, part1

actual_input = read_input_file("2015/day05/input.txt")


class TestPart1:
    def test_is_nice_string_1(self):
        assert is_nice_string("ugknbfddgicrmopn") is True

    def test_is_nice_string_2(self):
        assert is_nice_string("aaa") is True

    def test_is_nice_string_3(self):
        assert is_nice_string("jchzalrnumimnmhp") is False

    def test_is_nice_string_4(self):
        assert is_nice_string("haegwjzuvuyypxyu") is False

    def test_is_nice_string_5(self):
        assert is_nice_string("dvszwmarrgswjxmb") is False

    def test_with_actual_data(self):
        assert part1(actual_input) == 255
