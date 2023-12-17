from inputs import read_input_file_as_string
from part2 import part2

actual_input = read_input_file_as_string("2019/day09/input.txt")


class TestPart2:
    def test_should_output_16digit_number(self):
        assert part2("1102,34915192,34915192,7,4,7,99,0", None) == 1219070632396864

    def test_should_output_value_in_the_middle(self):
        assert part2("104,1125899906842624,99", None) == 1125899906842624

    def test_with_actual_data(self):
        assert part2(actual_input, 2) == 70634
