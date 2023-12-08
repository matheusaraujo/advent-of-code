import unittest, sys

sys.path.append('../..')

from helpers.test import AoCTesting
from problem1 import problem1
from problem2 import problem2

class Testing_0000_Day00(AoCTesting):
    def test_problem1_sample(self):
        super()._test(problem1, 'sample-input.txt', 1)

    def test_problem1(self):
        super()._test(problem1, 'input.txt', 42)

    def test_problem2_sample(self):
        super()._test(problem2, 'sample-input.txt', 2)
    
    def test_problem2(self):
        super()._test(problem2, 'input.txt', 84)

if __name__ == '__main__':
    unittest.main()