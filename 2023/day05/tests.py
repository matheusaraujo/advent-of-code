import unittest

from problem1 import problem1
from problem2 import problem2

class Testing(unittest.TestCase):
    def read_input(self, file = 'input.txt'):
        with open(file) as f:
            input = f.read()
        return input

    def test_problem1_sample(self):
        input = self.read_input('input-example.txt')
        output = problem1(input)
        self.assertEqual(output, 35)

    def test_problem1(self):
        input = self.read_input()
        output = problem1(input)
        self.assertEqual(output, 309796150)

    # def test_problem2_sample(self):
    #     input = self.read_input('input-example.txt')
    #     output = problem2(input)
    #     self.assertEqual(output, 46)

    # def test_problem2(self):
    #     input = self.read_input()
    #     output = problem2(input)
    #     self.assertEqual(output, 0)

if __name__ == '__main__':
    unittest.main()