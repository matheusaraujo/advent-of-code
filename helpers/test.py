import unittest

class AoCTesting(unittest.TestCase):
    def read_input_file(self, file_name):
        with open(file_name) as f:
            input = f.readlines()
        return input

    def _test(self, function, input_file, expected_result):
        input = self.read_input_file(input_file)
        output = function(input)
        self.assertEqual(output, expected_result)