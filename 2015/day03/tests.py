import unittest

from problem1 import problem1
from problem2 import problem2

class Testing(unittest.TestCase):
    def test_problem1_sample(self):
        self.assertEqual(problem1(">"), 2)
        self.assertEqual(problem1("^v^v^v^v^v"), 2)
        self.assertEqual(problem1(">>"), 3)
        self.assertEqual(problem1(">><"), 3)

    def test_problem1(self):
        with open("input.txt") as f:
            line = f.read()
        
        output = problem1(line)
        self.assertEqual(output, 2565)

    def test_problem2_sample(self):
        self.assertEqual(problem2("^v"), 3)
        self.assertEqual(problem2("^>v<"), 3)
        self.assertEqual(problem2("^v^v^v^v^v"), 11)
        
    def test_problem2(self):
        with open("input.txt") as f:
            line = f.read()
        
        output = problem2(line)
        self.assertEqual(output, 2639)

if __name__ == '__main__':
    unittest.main()