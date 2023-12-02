import unittest

from problem1 import problem1
from problem2 import problem2

class Testing(unittest.TestCase):
    def test_problem1_sample(self):
        test_cases = (
            { 'input': '(())',  'expected': 0 },
            { 'input': '()()',  'expected': 0 },
            { 'input': '(((',  'expected': 3 },
            { 'input': '(()(()(',  'expected': 3 },
            { 'input': '))(((((',  'expected': 3 },
            { 'input': '())',  'expected': -1 },
            { 'input': '))(',  'expected': -1 },
            { 'input': ')))',  'expected': -3 },
            { 'input': ')())())',  'expected': -3 },
        )

        for test_case in test_cases:
            with self.subTest(test_case['input']):
                output = problem1(test_case['input'])
                self.assertEqual(output, test_case['expected'])

    def test_problem1(self):
        with open("input.txt") as f:
            line = f.read()
        
        output = problem1(line)
        self.assertEqual(output, 74)

    def test_problem2_sample(self):
        test_cases = (
            { 'input': ')',  'expected': 1 },
            { 'input': '()())',  'expected': 5 },
        )

        for test_case in test_cases:
            with self.subTest(test_case['input']):
                output = problem2(test_case['input'])
                self.assertEqual(output, test_case['expected'])

    def test_problem2(self):
        with open("input.txt") as f:
            line = f.read()
        
        output = problem2(line)
        self.assertEqual(output, 1795)

if __name__ == '__main__':
    unittest.main()