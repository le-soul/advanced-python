"""
Test filtering
"""
import sys 
sys.path.append('scripts')
import unittest
import pandas as pd
from scripts.filtering import FilteringClass


class TestFilterData(unittest.TestCase):
    def setUp(self):
        data = {
            'Publish Date (Month)': ['January', 'February', 'April', 'February'],
            'Publish Date (Year)': [2020, 2021, 2019, 2022],
            'Price Starting With ($)': [10, 15, 20, 25],
        }
        self.df = pd.DataFrame(data)

    def test_filter_by_publis_year(self):
        """
        Test to see if the function filter by year
        """
        self.df = FilteringClass(self.df).filter_by_publis_year(2022)
        self.assertTrue(all(self.df["Publish Date (Year)"] == 2022))

    def test_filter_by_publis_month(self):
        """
        Test to see if the function filter by month
        """
        self.df = FilteringClass(self.df).filter_by_publis_month("January")
        self.assertTrue(all(self.df["Publish Date (Month)"] == "January"))

    def test_filter_price(self):
        """
        Test to see if the function filter by price
        """
        self.df = FilteringClass(self.df).filter_price(25)
        self.assertTrue(all(self.df["Price Starting With ($)"] > 25))


if __name__ == "__main__":
    unittest.main()
