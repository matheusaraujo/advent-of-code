from inputs import read_input_file
from part2 import part2, calculate_module_fuel

actual_input = read_input_file("2019/day01/input.txt")

class TestPart2:
    def test_with_sample_data(self):
        assert calculate_module_fuel(12) == 2
        assert calculate_module_fuel(14) == 2
        assert calculate_module_fuel(1969) == 966
        assert calculate_module_fuel(100756) == 50346

    def test_with_actual_data(self):
        assert part2(actual_input) == 0
