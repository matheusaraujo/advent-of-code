import unittest

from problem1 import problem1
from problem2 import problem2

class Testing(unittest.TestCase):
    def test_problem1_sample(self):
        input = [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            ".#.$.*....",
            ".664.598..",
        ]
        output = problem1(input)
        self.assertEqual(output, 4361)

    def test_problem1(self):
        with open("input.txt") as f:
            input = f.readlines()
        
        output = problem1(input)
        self.assertEqual(output, 512794)

    # def test_problem2_sample(self):
    #     input = problem2("some input")
    #     self.assertEqual(input, "problem2")

    # def test_problem2(self):
    #     with open("input.txt") as f:
    #         input = f.readlines()
        
    #     output = problem2(input)
    #     self.assertEqual(output, "problem2")

if __name__ == '__main__':
    unittest.main()