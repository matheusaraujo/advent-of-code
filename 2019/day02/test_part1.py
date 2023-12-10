from inputs import read_input_file_as_string
from part1 import part1

actual_input = read_input_file_as_string("2019/day02/input.txt")


class TestPart1:
    def test_with_sample_data_1(self):
        assert part1("1,9,10,3,2,3,11,0,99,30,40,50") == 3500

    def test_with_sample_data_2(self):
        assert part1("1,0,0,0,99") == 2

    def test_with_sample_data_3(self):
        assert part1("2,3,0,3,99") == 2

    def test_with_sample_data_4(self):
        assert part1("2,4,4,5,99,0") == 2

    def test_with_sample_data_5(self):
        assert part1("1,1,1,4,99,5,6,0,99") == 30

    def test_with_actual_data(self):
        assert part1(actual_input, 12, 2) == 5305097
