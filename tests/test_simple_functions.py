"""
Script to write the test for the sum and subtract functions
"""

import unittest
from scripts.simple_functions import sum_two_nums, sub_two_nums


class TestSimpleFunction(unittest.TestCase):
    """
    Test simple functions sum & subtract
    """

    def test_sum(self):
        """
        Test the sum function
        """
        result = sum_two_nums(4, 5)
        self.assertEqual(result, 9)

    def test_sub(self):
        """
        Test the sub function
        """
        result = sub_two_nums(1, 3)
        self.assertEqual(result, -2)


if __name__ == "__main__":
    unittest.main()
