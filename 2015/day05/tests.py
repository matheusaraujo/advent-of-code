import unittest

from problem1 import problem1, problem1_solve
from problem2 import problem2, problem2_solve

class Testing(unittest.TestCase):
    def test_problem1_sample(self):
        self.assertTrue(problem1_solve("ugknbfddgicrmopn"))
        self.assertTrue(problem1_solve("aaa"))
        self.assertFalse(problem1_solve("jchzalrnumimnmhp"))
        self.assertFalse(problem1_solve("haegwjzuvuyypxyu"))
        self.assertFalse(problem1_solve("dvszwmarrgswjxmb"))

    def test_problem1(self):
        with open("input.txt") as f:
            input = f.readlines()
        
        output = problem1(input)
        self.assertEqual(output, 255)

    def test_problem2_sample(self):
        self.assertTrue(problem2_solve("qjhvhtzxzqqjkmpb"))
        self.assertTrue(problem2_solve("xxyxx"))
        self.assertFalse(problem2_solve("uurcxstgmygtbstg"))
        self.assertFalse(problem2_solve("ieodomkazucvgmuy"))
        
    def test_problem2(self):
        with open("input.txt") as f:
            input = f.readlines()
        
        output = problem2(input)
        self.assertEqual(output, 55)

if __name__ == '__main__':
    unittest.main()