import unittest

from problem1 import problem1
from problem2 import problem2, define_hand_value

class Testing(unittest.TestCase):
    def read_input(self, file_name = 'input.txt'):
        with open(file_name) as f:
            input = f.readlines()
        return input

    sample_input = "some input"

    def test_problem1_sample(self):
        input = self.read_input('sample-input.txt')
        output = problem1(input)
        self.assertEqual(output, 6440)

    def test_problem1(self):
        input = self.read_input()
        output = problem1(input)
        self.assertEqual(output, 250951660)

    def test_problem2_sample(self):
        input = self.read_input('sample-input.txt')
        output = problem2(input)
        self.assertEqual(output, 5905)

    def test_problem2(self):
        input = self.read_input()
        output = problem2(input)
        self.assertEqual(output, 251481660)

    def test_define_hand_value(self):
        test_cases = (
            { 'input': 'AAAAA',  'expected': 60 },
            { 'input': 'AAAA2',  'expected': 50 },
            { 'input': 'AAA22',  'expected': 40 },
            { 'input': 'AAA23',  'expected': 30 },
            { 'input': 'AA224',  'expected': 20 },
            { 'input': 'AA234',  'expected': 10 },
            { 'input': 'A2345',  'expected': 0 },
            { 'input': 'JJJJJ',  'expected': 60 },
            { 'input': 'JJJJ2',  'expected': 60 },
            { 'input': 'JJJ22',  'expected': 60 },
            { 'input': 'JJJ23',  'expected': 50 },
            { 'input': 'JJ223',  'expected': 50 },
            { 'input': 'JJ234',  'expected': 30 },
            { 'input': 'JAAAA',  'expected': 60 },
            { 'input': 'JAAA2',  'expected': 50 },
            { 'input': 'JAA23',  'expected': 30 },
            { 'input': 'JA234',  'expected': 10 },
            { 'input': 'JAA22',  'expected': 40 },
        )

        for test_case in test_cases:
            with self.subTest(test_case['input']):
                output = define_hand_value(test_case['input'])
                self.assertEqual(output, test_case['expected'])

if __name__ == '__main__':
    unittest.main()