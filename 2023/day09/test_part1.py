from inputs import read_input_file
from part1 import part1, predict_next

actual_input = read_input_file("2023/day09/input.txt")
sample_input = read_input_file("2023/day09/sample-input.txt")


class TestPart1:
    def test_predict_next(self):
        assert predict_next([0, 3, 6, 9, 12, 15]) == 18
        assert predict_next([1, 3, 6, 10, 15, 21]) == 28
        assert predict_next([10, 13, 16, 21, 30, 45]) == 68

    def test_with_sample_data(self):
        assert part1(sample_input) == 114

    def test_with_actual_data(self):
        assert part1(actual_input) == 1904165718
