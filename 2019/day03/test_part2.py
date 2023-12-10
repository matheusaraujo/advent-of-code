from inputs import read_input_file
from part2 import part2

sample_input_a = read_input_file("2019/day03/sample-input-a.txt")
sample_input_b = read_input_file("2019/day03/sample-input-b.txt")
sample_input_c = read_input_file("2019/day03/sample-input-c.txt")
actual_input = read_input_file("2019/day03/input.txt")


class TestPart2:
    def test_with_sample_data(self):
        assert part2(sample_input_a) == 30
        assert part2(sample_input_b) == 610
        assert part2(sample_input_c) == 410

    def test_with_actual_data(self):
        assert part2(actual_input) == 9006
