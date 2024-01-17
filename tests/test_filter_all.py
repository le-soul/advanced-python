"""
Test filtering conditions
"""

from scripts.repo_first_script import filter_all
import unittest
import pandas as pd 

class TestFilterAll(unittest.TestCase):

    def setUp(self):

        data = {
            'Publish Date (Month)': ['January', 'February', 'April', 'February'],
            'Publish Date (Year)': [2020, 2021, 2019, 2022],
            'Price Starting With ($)': [10, 15, 20, 25],
        }
        self.df = pd.DataFrame(data)

    def test_filter_by_month(self):
        result_df = filter_all(self.df, month='January')
        assert result_df.shape[0] == 1 

    def test_filter_by_year(self):
        result_df = filter_all(self.df, year=2022)
        assert result_df.shape[0] == 1 

    def test_filter_by_price(self):
        result_df = filter_all(self.df, price=15.0)
        assert result_df.shape[0] == 2 

    def test_no_filters(self):
        result_df = filter_all(self.df)
        assert result_df.shape[0] == 4


