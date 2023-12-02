import unittest

from problem1 import problem1
from problem2 import problem2

class Testing(unittest.TestCase):
    def test_problem1_sample(self):
        output = problem1(['2x3x4'])
        self.assertEqual(output, 58)

        output = problem1(['1x1x10'])
        self.assertEqual(output, 43)

    def test_problem1(self):
        with open("input.txt") as f:
            line = f.readlines()
        
        output = problem1(line)
        self.assertEqual(output, 1598415)

    def test_problem2_sample(self):
        output = problem2(['2x3x4'])
        self.assertEqual(output, 34)

        output = problem2(['1x1x10'])
        self.assertEqual(output, 14)

    def test_problem2(self):
        with open("input.txt") as f:
            line = f.readlines()
        
        output = problem2(line)
        self.assertEqual(output, 3812909)

if __name__ == '__main__':
    unittest.main()