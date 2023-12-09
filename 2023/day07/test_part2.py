from inputs import read_input_file
from part2 import define_hand_value, part2

sample_input = read_input_file("2023/day07/sample-input.txt")
actual_input = read_input_file("2023/day07/input.txt")


class TestPart2:
    def test_define_hand_value(self):
        assert define_hand_value("AAAAA") == 60
        assert define_hand_value("AAAA2") == 50
        assert define_hand_value("AAA22") == 40
        assert define_hand_value("AAA23") == 30
        assert define_hand_value("AA224") == 20
        assert define_hand_value("AA234") == 10
        assert define_hand_value("A2345") == 0
        assert define_hand_value("JJJJJ") == 60
        assert define_hand_value("JJJJ2") == 60
        assert define_hand_value("JJJ22") == 60
        assert define_hand_value("JJJ23") == 50
        assert define_hand_value("JJ223") == 50
        assert define_hand_value("JJ234") == 30
        assert define_hand_value("JAAAA") == 60
        assert define_hand_value("JAAA2") == 50
        assert define_hand_value("JAA23") == 30
        assert define_hand_value("JA234") == 10
        assert define_hand_value("JAA22") == 40

    def test_with_sample_data(self):
        assert part2(sample_input) == 5905

    def test_with_actual_data(self):
        assert part2(actual_input) == 251481660
