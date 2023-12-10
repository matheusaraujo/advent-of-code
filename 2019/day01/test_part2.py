from inputs import read_input_file
from part2 import calculate_module_fuel, part2

actual_input = read_input_file("2019/day01/input.txt")


class TestPart2:
    def test_calculate_module_fuel_1(self):
        assert calculate_module_fuel(12) == 2

    def test_calculate_module_fuel_2(self):
        assert calculate_module_fuel(14) == 2

    def test_calculate_module_fuel_3(self):
        assert calculate_module_fuel(1969) == 966

    def test_calculate_module_fuel_4(self):
        assert calculate_module_fuel(100756) == 50346

    def test_with_actual_data(self):
        assert part2(actual_input) == 5218616
