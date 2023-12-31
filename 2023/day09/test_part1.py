from inputs import read_input_file
from part1 import part1, predict_next

sample_input = read_input_file("2023/day09/sample-input.txt")
actual_input = read_input_file("2023/day09/input.txt")


class TestPart1:
    def test_predict_next_1(self):
        assert predict_next([0, 3, 6, 9, 12, 15]) == 18

    def test_predict_next_2(self):
        assert predict_next([1, 3, 6, 10, 15, 21]) == 28

    def test_predict_next_3(self):
        assert predict_next([10, 13, 16, 21, 30, 45]) == 68

    def test_with_sample_data(self):
        assert part1(sample_input) == 114

    def test_with_actual_data(self):
        assert part1(actual_input) == 1904165718
