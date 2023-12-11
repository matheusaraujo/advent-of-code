from inputs import read_input_file_as_string
from part1 import meets_criteria, part1

actual_input = read_input_file_as_string("2019/day04/input.txt")


class TestPart1:
    def test_meets_criteria_1(self):
        assert meets_criteria(111111) == True

    def test_meets_criteria_2(self):
        assert meets_criteria(223450) == False

    def test_meets_criteria_3(self):
        assert meets_criteria(123789) == False

    def test_with_actual_data(self):
        assert part1(actual_input) == 1864
