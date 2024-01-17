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
            'Publish Date (Year)': [2010, 2008, 2002, 2005],
            'Price Starting With ($)': [4.0, 7.0, 2.0, 10.0],
        }
        self.df = pd.DataFrame(data)

    def test_filter_by_publis_year(self):
        """
        Test to see if the function filter by year
        """
        self.df = FilteringClass(self.df).filter_by_publis_year(2005)
        self.assertTrue(all(self.df["Publish Date (Year)"] == 2005))

    def test_filter_by_publis_month(self):
        """
        Test to see if the function filter by month
        """
        self.df = FilteringClass(self.df).filter_by_publis_month("January")
        self.assertTrue(all(self.df["Publish Date (Month)"] == "January"))

    def test_filter_pricem(self):
        """
        Test to see if the function filter by price, more than
        """
        self.df = FilteringClass(self.df).filter_pricem(4.0)
        self.assertTrue(all(self.df["Price Starting With ($)"] > 4.0))

    def test_filter_pricem(self):
        """
        Test to see if the function filters by price, less than
        """
        self.df = FilteringClass(self.df).filter_pricel(7.0)
        self.assertTrue(all(self.df["Price Starting With ($)"] < 7.0))


if __name__ == "__main__":
    unittest.main()
