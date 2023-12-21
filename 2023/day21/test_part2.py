from inputs import read_input_file
from part2 import part2

sample_input_2 = read_input_file("2023/day21/sample-input-2.txt")
actual_input = read_input_file("2023/day21/input.txt")


class TestPart2:
    def test_with_sample_data_2a(self):
        assert part2(sample_input_2, 6) == 16

    def test_with_sample_data_2b(self):
        assert part2(sample_input_2, 10) == 50

    # def test_with_sample_data_2c(self):
    #     assert part2(sample_input_2, 50) == 1594

    # def test_with_sample_data_2d(self):
    #     assert part2(sample_input_2, 100) == 6536

    # def test_with_sample_data_2e(self):
    #     assert part2(sample_input_2, 500) == 167004

    # def test_with_sample_data_2f(self):
    #     assert part2(sample_input_2, 1000) == 668697

    # def test_with_sample_data_2g(self):
    #     assert part2(sample_input_2, 5000) == 16733044

    # def test_with_actual_data(self):
    #     assert part2(actual_input) == 84
