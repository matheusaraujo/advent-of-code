from inputs import read_input_file
from part2 import is_nice_string, part2

actual_input = read_input_file("2015/day05/input.txt")


class TestPart2:
    def test_is_nice_string_1(self):
        assert is_nice_string("qjhvhtzxzqqjkmpb") is True

    def test_is_nice_string_2(self):
        assert is_nice_string("xxyxx") is True

    def test_is_nice_string_3(self):
        assert is_nice_string("uurcxstgmygtbstg") is False

    def test_is_nice_string_4(self):
        assert is_nice_string("ieodomkazucvgmuy") is False

    def test_with_actual_data(self):
        assert part2(actual_input) == 55
