from inputs import read_input_file
from part1 import part1

actual_input = read_input_file("2015/day01/input.txt")


class Test2015Day01Part1:
    def test_with_sample_data(self):
        assert part1("(())") == 0
        assert part1("()()") == 0
        assert part1("(((") == 3
        assert part1("(()(()(") == 3
        assert part1("))(((((") == 3
        assert part1("())") == -1
        assert part1("))(") == -1
        assert part1(")))") == -3
        assert part1(")())())") == -3

    def test_with_actual_data(self):
        assert part1(actual_input[0]) == 74
