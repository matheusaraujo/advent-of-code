from inputs import read_input_file
from part2 import part2, predict_previous

sample_input = read_input_file("2023/day09/sample-input.txt")
actual_input = read_input_file("2023/day09/input.txt")


class TestPart2:
    def test_predict_previous_1(self):
        assert predict_previous([0, 3, 6, 9, 12, 15]) == -3

    def test_predict_previous_2(self):
        assert predict_previous([1, 3, 6, 10, 15, 21]) == 0

    def test_predict_previous_3(self):
        assert predict_previous([10, 13, 16, 21, 30, 45]) == 5

    def test_with_sample_data(self):
        assert part2(sample_input) == 2

    def test_with_actual_data(self):
        assert part2(actual_input) == 964
