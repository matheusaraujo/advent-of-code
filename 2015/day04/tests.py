import unittest

from problem1 import problem1
from problem2 import problem2

class Testing(unittest.TestCase):
    def test_problem1_sample(self):
        self.assertEqual(problem1("abcdef"), 609043)
        self.assertEqual(problem1("pqrstuv"), 1048970)

    def test_problem1(self):
        with open("input.txt") as f:
            input = f.read()
        
        output = problem1(input)
        self.assertEqual(output, 254575)

    def test_problem2(self):
        with open("input.txt") as f:
            input = f.read()
        
        output = problem2(input)
        self.assertEqual(output, 1038736)

if __name__ == '__main__':
    unittest.main()