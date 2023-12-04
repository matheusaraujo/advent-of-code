import unittest

from problem1 import problem1
from problem2 import problem2

class Testing(unittest.TestCase):
    def read_input(self):
        with open("input.txt") as f:
            input = f.readlines()
        return input

    sample_input = {
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    }

    def test_problem1_sample(self):
        output = problem1(self.sample_input)
        self.assertEqual(output, 13)

    def test_problem1(self):
        input = self.read_input()
        output = problem1(input)
        self.assertEqual(output, 24848)

    # def test_problem2_sample(self):
    #     input = problem2(self.sample_input)
    #     self.assertEqual(input, "problem2")

    # def test_problem2(self):
    #     input = self.read_input()
    #     output = problem2(input)
    #     self.assertEqual(output, "problem2")

if __name__ == '__main__':
    unittest.main()