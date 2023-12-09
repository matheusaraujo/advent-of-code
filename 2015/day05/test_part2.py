from inputs import read_input_file
from part2 import is_nice_string, part2

actual_input = read_input_file("2015/day05/input.txt")


class TestPart2:
    def test_with_sample_data(self):
        assert is_nice_string("qjhvhtzxzqqjkmpb") is True
        assert is_nice_string("xxyxx") is True
        assert is_nice_string("uurcxstgmygtbstg") is False
        assert is_nice_string("ieodomkazucvgmuy") is False

    def test_with_actual_data(self):
        assert part2(actual_input) == 55
