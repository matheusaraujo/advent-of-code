from inputs import read_input_file
from part2 import part2

actual_input = read_input_file("2015/day04/input.txt")


class TestPart2:
    def test_with_sample_data_1(self):
        assert part2("abcdef") == 6742839

    def test_with_sample_data_2(self):
        assert part2("pqrstuv") == 5714438

    def test_with_actual_data(self):
        assert part2(actual_input[0]) == 1038736
