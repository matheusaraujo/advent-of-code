from inputs import read_input_file_as_string
from part2 import part2

actual_input = read_input_file_as_string("2019/day08/input.txt")
expected_output = read_input_file_as_string("2019/day08/output.txt")


class TestPart2:
    def test_with_sample_data(self):
        assert part2("0222112222120000", 2, 2) == "-##-"

    def test_with_actual_data(self):
        assert part2(actual_input, 6, 25) == expected_output.replace("\n", "")
