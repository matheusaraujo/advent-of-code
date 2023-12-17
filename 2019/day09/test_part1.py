from inputs import read_input_file_as_string
from part1 import part1

actual_input = read_input_file_as_string("2019/day09/input.txt")


class TestPart1:
    def test_should_copy_itself(self):
        quine = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
        assert part1(quine, None) == quine

    def test_with_actual_data(self):
        assert part1(actual_input, 1) == "2457252183"
