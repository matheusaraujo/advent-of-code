import unittest

from problem1 import problem1
from problem2 import problem2

class Testing(unittest.TestCase):
    def read_input(self):
        with open("input.txt") as f:
            input = f.readlines()
        return input

    sample_input = "some input"

    def test_problem1_sample(self):
        output = problem1(self.sample_input)
        self.assertEqual(output, "some input")

    def test_problem1(self):
        input = self.read_input()
        output = problem1(input)
        self.assertEqual(output, ["sample input"])

    def test_problem2_sample(self):
        input = problem2(self.sample_input)
        self.assertEqual(input, "problem2")

    def test_problem2(self):
        input = self.read_input()
        output = problem2(input)
        self.assertEqual(output, "problem2")

if __name__ == '__main__':
    unittest.main()