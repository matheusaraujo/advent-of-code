import unittest

from problem1 import problem1
from problem2 import problem2

class Testing(unittest.TestCase):
    def read_input(self):
        with open("input.txt") as f:
            input = f.readlines()
        return input

    def test_problem1_sample_1(self):
        test_cases = [
            {
                'input': [
                    "turn on 1,0 through 1,2"
                ],
                'expected': 3
            },
        ]
        for test_case in test_cases:
            with self.subTest(test_case['input']):
                output = problem1(test_case['input'], 4)
                self.assertEqual(output, test_case['expected'])

    # def test_problem1(self):
    #     input = self.read_input()
    #     output = problem1(input)
    #     self.assertEqual(output, ["sample input"])

    # def test_problem2_sample(self):
    #     input = problem2(self.sample_input)
    #     self.assertEqual(input, "problem2")

    # def test_problem2(self):
    #     input = self.read_input()
    #     output = problem2(input)
    #     self.assertEqual(output, "problem2")

if __name__ == '__main__':
    unittest.main()