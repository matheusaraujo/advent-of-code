import unittest

from problem1 import problem1
from problem2 import problem2

class Testing(unittest.TestCase):
    def read_input(self, file = 'input.txt'):
        with open(file) as f:
            input = f.readlines()
        return input

    def test_problem1_sample(self):
        input = self.read_input('input-sample.txt')
        output = problem1(input)
        self.assertEqual(output, 288)

    def test_problem1(self):
        input = self.read_input()
        output = problem1(input)
        self.assertEqual(output, 1624896)

    def test_problem2_sample(self):
        input = self.read_input('input-sample.txt')
        output = problem2(input)
        self.assertEqual(output, 71503)

    def test_problem2(self):
        input = self.read_input()
        output = problem2(input)
        self.assertEqual(output, 32583852)

if __name__ == '__main__':
    unittest.main()