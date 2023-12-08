import unittest

from problem1 import problem1
from problem2 import problem2

class Testing(unittest.TestCase):
    def read_input(self):
        with open("input.txt") as f:
            input = f.readlines()
        return input

    def test_problem1(self):
        input = self.read_input()
        output = problem1(input)
        self.assertEqual(output, 543903)

    def test_problem2(self):
        input = self.read_input()
        output = problem2(input)
        self.assertEqual(output, 14687245)

if __name__ == '__main__':
    unittest.main()