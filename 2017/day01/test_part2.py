from inputs import read_input_file
from part2 import part2


actual_input = read_input_file("2017/day01/input.txt")


class TestPart2:
    def test_with_sample_data_1(self):
        assert part2(["1212"]) == 6

    def test_with_sample_data_2(self):
        assert part2(["1221"]) == 0

    def test_with_sample_data_3(self):
        assert part2(["123425"]) == 4

    def test_with_sample_data_4(self):
        assert part2(["123123"]) == 12

    def test_with_sample_data_5(self):
        assert part2(["12131415"]) == 4

    def test_with_actual_data(self):
        assert part2(actual_input) == 0
