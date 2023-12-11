from inputs import read_input_file_as_string
from part2 import meets_criteria, part2

actual_input = read_input_file_as_string("2019/day04/input.txt")


class TestPart1:
    def test_meets_criteria_1(self):
        assert meets_criteria(112233) is True

    def test_meets_criteria_2(self):
        assert meets_criteria(123444) is False

    def test_meets_criteria_3(self):
        assert meets_criteria(111122) is True

    def test_with_actual_data(self):
        assert part2(actual_input) == 1258
