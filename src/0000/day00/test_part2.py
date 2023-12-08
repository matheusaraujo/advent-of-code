from part2 import part2
from inputs import read_input_file

actual_input = read_input_file('0000/day00/input.txt')
sample_input = read_input_file('0000/day00/sample-input.txt')

class Test0000Day00part2:
    def test_with_sample_data(self):
        assert part2(sample_input) == 2

    def test_with_actual_data(self):
        assert part2(actual_input) == 84
