import unittest

from problem1 import problem1
from problem2 import problem2

class Testing(unittest.TestCase):
    def test_problem1_sample(self):
        output = problem1("problem1")
        self.assertEqual(output, "problem1")

    def test_problem1(self):
        with open("input.txt") as f:
            line = f.readlines()
        
        output = problem1(line)
        self.assertEqual(output, ["sample input"])

    def test_problem2_sample(self):
        output = problem2("some input")
        self.assertEqual(output, "problem2")

    def test_problem2(self):
        with open("input.txt") as f:
            line = f.readlines()
        
        output = problem2(line)
        self.assertEqual(output, "problem2")

if __name__ == '__main__':
    unittest.main()