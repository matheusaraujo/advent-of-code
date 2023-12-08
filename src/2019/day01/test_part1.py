from inputs import read_input_file
from part1 import part1, calculate_module_fuel

actual_input = read_input_file("2019/day01/input.txt")

class TestPart1:
    def test_with_sample_data(self):
        assert calculate_module_fuel(12) == 2
        assert calculate_module_fuel(14) == 2
        assert calculate_module_fuel(1969) == 654
        assert calculate_module_fuel(100756) == 33583

    def test_with_actual_data(self):
        assert part1(actual_input) == 3481005
