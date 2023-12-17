from inputs import read_input_file_as_string
from part2 import part2

actual_input = read_input_file_as_string("2019/day05/input.txt")


class TestPart2:
    def test_with_sample_data_equals_to_8(self):
        assert part2("3,9,8,9,10,9,4,9,99,-1,8", 8) == 1

    def test_with_sample_data_not_equals_to_8(self):
        assert part2("3,9,8,9,10,9,4,9,99,-1,8", 7) == 0

    def test_with_sample_data_less_than_8(self):
        assert part2("3,9,7,9,10,9,4,9,99,-1,8", 7) == 1

    def test_with_sample_data_not_less_than_8(self):
        assert part2("3,9,7,9,10,9,4,9,99,-1,8", 9) == 0

    def test_with_sample_data_equals_to_8_immediate_mode(self):
        assert part2("3,3,1108,-1,8,3,4,3,99", 8) == 1

    def test_with_sample_data_not_equals_to_8_immediate_mode(self):
        assert part2("3,3,1108,-1,8,3,4,3,99", 7) == 0

    def test_with_sample_data_less_than_8_immediate_mode(self):
        assert part2("3,3,1107,-1,8,3,4,3,99", 7) == 1

    def test_with_sample_data_not_less_than_8_immediate_mode(self):
        assert part2("3,3,1107,-1,8,3,4,3,99", 9) == 0

    def test_with_actual_data(self):
        assert part2(actual_input, 5) == 11430197
