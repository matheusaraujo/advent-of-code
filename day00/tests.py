import unittest
import sys

sys.path.append('../helpers')

from problem1 import problem1
from problem2 import problem2
from helpers import read_input

class Testing(unittest.TestCase):
    def test_problem1_sample(self):
        input = read_input('sample-input.txt')
        output = problem1(input)
        self.assertEqual(output, ['42'])

    # def test_problem1(self):
    #     input = read_input()
    #     output = problem1(input)
    #     self.assertEqual(output, ["sample input"])

    # def test_problem2_sample(self):
    #     output = problem2(self.sample_input)
    #     self.assertEqual(output, "problem2")

    # def test_problem2(self):
    #     input = read_input()
    #     output = problem2(input)
    #     self.assertEqual(output, "problem2")

if __name__ == '__main__':
    unittest.main()