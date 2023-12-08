import unittest

from problem1 import problem1
from problem2 import problem2

class Testing(unittest.TestCase):
    def read_input(self, file_name = 'input.txt'):
        with open(file_name) as f:
            input = f.readlines()
        return input

    def test_problem1_sample_a(self):
        input = self.read_input('sample-input-1a.txt')
        output = problem1(input)
        self.assertEqual(output, 2)

    def test_problem1_sample_b(self):
        input = self.read_input('sample-input-1b.txt')
        output = problem1(input)
        self.assertEqual(output, 6)

    def test_problem1(self):
        input = self.read_input()
        output = problem1(input)
        self.assertEqual(output, 16697)

    def test_problem1_sample_b(self):
        input = self.read_input('sample-input-2a.txt')
        output = problem2(input)
        self.assertEqual(output, 6)

    def test_problem2(self):
        input = self.read_input()
        output = problem2(input)
        self.assertEqual(output, 10668805667831)

if __name__ == '__main__':
    unittest.main()