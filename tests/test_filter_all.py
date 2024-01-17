"""
Test filtering conditions
"""

from scripts.repo_first_script import filter_all
import unittest
import pandas as pd 

class TestFilterAll(unittest.TestCase):
    """
    Test class for checking that month, year and price
    """

    def setUp(self):

        data = {
            'Publish Date (Month)': ['January', 'February', 'April', 'February'],
            'Publish Date (Year)': [2010, 2011, 2019, 2012],
            'Price Starting With ($)': [10.0, 12.0, 4.0, 5.0],
        }
        self.df = pd.DataFrame(data)

    def test_filter_by_month(self):
        result_df = filter_all(self.df, month='January')
        assert result_df.shape[0] == 1

    def test_filter_by_year(self):
        result_df = filter_all(self.df, year=2012)
        assert result_df.shape[0] == 1

    def test_filter_by_pricem(self):
        result_df = filter_all(self.df, pricem=10.0)
        assert result_df.shape[0] == 1

    def test_filter_by_pricel(self):
        result_df = filter_all(self.df, pricel=5.0)
        assert result_df.shape[0] == 1

    def test_no_filters(self):
        result_df = filter_all(self.df)
        assert result_df.shape[0] == 4


