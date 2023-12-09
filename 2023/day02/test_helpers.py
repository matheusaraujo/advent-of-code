from helpers import extract_game, extract_line


class TestHelpers:
    def test_extract_line(self):
        assert extract_line("3 red, 4 green, 5 blue") == [3, 4, 5]
        assert extract_line("3 red") == [3, 0, 0]
        assert extract_line("0 green") == [0, 0, 0]
        assert extract_line("10 blue") == [0, 0, 10]
        assert extract_line("3 red, 4 green") == [3, 4, 0]

    def test_extract_game(self):
        assert extract_game("Game 1: 3 blue, 4 red, 2 green") == 1
        assert extract_game("Game 99: 3 blue, 4 red, 2 green") == 99
