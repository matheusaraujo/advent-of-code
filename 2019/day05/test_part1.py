from inputs import read_input_file_as_string
from part1 import part1

actual_input = read_input_file_as_string("2019/day05/input.txt")


class TestPart1:
    def test_with_sample_data(self):
        assert part1("2,1,2,7,4,7,99,0", 0) == 2

    def test_with_sample_data_2(self):
        assert part1("1102,10,10,7,4,7,99,0", 0) == 100

    def test_with_actual_data(self):
        assert part1(actual_input, 1) == 15426686
