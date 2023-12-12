from inputs import read_input_file
from part2 import count_arrangement_part2, part2

sample_input = read_input_file("2023/day12/sample-input.txt")
actual_input = read_input_file("2023/day12/input.txt")


class TestPart2:
    def test_count_arrangement_1(self):
        assert count_arrangement_part2("???.### 1,1,3") == 1

    def test_count_arrangement_2(self):
        assert count_arrangement_part2(".??..??...?##. 1,1,3") == 16384

    def test_count_arrangement_3(self):
        assert count_arrangement_part2("?#?#?#?#?#?#?#? 1,3,1,6") == 1

    def test_count_arrangement_4(self):
        assert count_arrangement_part2("????.#...#... 4,1,1") == 16

    def test_count_arrangement_5(self):
        assert count_arrangement_part2("????.######..#####. 1,6,5") == 2500

    def test_count_arrangement_6(self):
        assert count_arrangement_part2("?###???????? 3,2,1") == 506250

    def test_with_sample_data(self):
        assert part2(sample_input) == 525152

    def test_with_actual_data(self):
        assert part2(actual_input) == 51456609952403
