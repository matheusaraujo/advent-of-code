import unittest

from problem1 import problem1
from problem2 import problem2

class Testing(unittest.TestCase):
    def test_problem1(self):
        input = [
            "1abc2", \
            "pqr3stu8vwx", \
            "a1b2c3d4e5f", \
            "treb7uchet"
        ]

        output = problem1(input)
        self.assertEqual(output, 142)

    def test_problem2(self):
        input = [
            "two1nine", \
            "eightwothree", \
            "abcone2threexyz", \
            "xtwone3four", \
            "4nineeightseven2", \
            "zoneight234", \
            "7pqrstsixteen"
        ]

        output = problem2(input)
        self.assertEqual(output, 281)

if __name__ == '__main__':
    unittest.main()