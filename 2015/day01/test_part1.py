from inputs import read_input_file
from part1 import part1

actual_input = read_input_file("2015/day01/input.txt")


class TestPart1:
    def test_with_sample_data_1(self):
        assert part1("(())") == 0

    def test_with_sample_data_2(self):
        assert part1("()()") == 0

    def test_with_sample_data_3(self):
        assert part1("(((") == 3

    def test_with_sample_data_4(self):
        assert part1("(()(()(") == 3

    def test_with_sample_data_5(self):
        assert part1("))(((((") == 3

    def test_with_sample_data_6(self):
        assert part1("())") == -1

    def test_with_sample_data_7(self):
        assert part1("))(") == -1

    def test_with_sample_data_8(self):
        assert part1(")))") == -3

    def test_with_sample_data_9(self):
        assert part1(")())())") == -3

    def test_with_actual_data(self):
        assert part1(actual_input[0]) == 74
