from inputs import read_input_file
from part1 import count_arrangement, part1

sample_input = read_input_file("2023/day12/sample-input.txt")
actual_input = read_input_file("2023/day12/input.txt")


class TestPart1:
    def test_count_arrangement_1(self):
        assert count_arrangement("???.### 1,1,3") == 1

    def test_count_arrangement_2(self):
        assert count_arrangement(".??..??...?##. 1,1,3") == 4

    def test_count_arrangement_3(self):
        assert count_arrangement("?#?#?#?#?#?#?#? 1,3,1,6") == 1

    def test_count_arrangement_4(self):
        assert count_arrangement("????.#...#... 4,1,1") == 1

    def test_count_arrangement_5(self):
        assert count_arrangement("????.######..#####. 1,6,5") == 4

    def test_count_arrangement_6(self):
        assert count_arrangement("?###???????? 3,2,1") == 10

    def test_with_sample_data(self):
        assert part1(sample_input) == 21

    def test_with_actual_data(self):
        assert part1(actual_input) == 6949
