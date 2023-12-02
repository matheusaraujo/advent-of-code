import unittest

from fixtures import extract_line, extract_game
from problem1 import problem1
from problem2 import problem2

class Testing1(unittest.TestCase):
    def test_extract_line(self):
        test_cases = (
            {
                'case': 'RGB', 
                'input': '3 red, 4 green, 5 blue', 
                'expected': [3, 4, 5]
            },
            {
                'case': 'R', 
                'input': '3 red', 
                'expected': [3, 0, 0]
            },
            {
                'case': 'G', 
                'input': '0 green', 
                'expected': [0, 0, 0]
            },
            {
                'case': 'B', 
                'input': '10 blue', 
                'expected': [0, 0, 10]
            },
            {
                'case': 'RG', 
                'input': '3 red, 4 green', 
                'expected': [3, 4, 0]
            },
        )

        for test_case in test_cases:
            with self.subTest(test_case['case']):
                output = extract_line(test_case['input'])
                self.assertEqual(output, test_case['expected'])

    def test_extract_game(self):
        test_cases = (
            {
                'case': 'Game 1', 
                'input': 'Game 1: 3 blue, 4 red, 2 green', 
                'expected': 1
            },
            {
                'case': 'Game 99', 
                'input': 'Game 99: 3 blue, 4 red, 2 green', 
                'expected': 99
            },
        )

        for test_case in test_cases:
            with self.subTest(test_case['case']):
                output = extract_game(test_case['input'])
                self.assertEqual(output, test_case['expected'])

    def test_problem_1_sample(self):
        lines = [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        ]

        limits = "12 red, 13 green, 14 blue"

        output = problem1(lines, limits)

        self.assertEqual(output, 8)

    def test_problem_1(self):
        with open("input.txt") as f:
            lines = f.readlines()

        limits = "12 red, 13 green, 14 blue"

        output = problem1(lines, limits)

        self.assertEqual(output, 2237)

    def test_problem_2_sample(self):
        lines = [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        ]

        output = problem2(lines)

        self.assertEqual(output, 2286)

    def test_problem_2(self):
        with open("input.txt") as f:
            lines = f.readlines()

        output = problem2(lines)

        self.assertEqual(output, 66681)


if __name__ == '__main__':
    unittest.main()