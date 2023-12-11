import pytest
from inputs import read_input_file
from part1 import part1

actual_input = read_input_file("2015/day04/input.txt")


class TestPart1:
    @pytest.mark.skip(reason="skipping this test just to save time")
    def test_with_sample_data_1(self):
        assert part1("abcdef") == 609043

    @pytest.mark.skip(reason="skipping this test just to save time")
    def test_with_sample_data_2(self):
        assert part1("pqrstuv") == 1048970

    def test_with_actual_data(self):
        assert part1(actual_input[0]) == 254575
