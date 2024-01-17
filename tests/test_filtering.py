"""
Test filtering
"""
import unittest
import pandas as pd
from scripts.filtering import FilteringClass


class TestFilterData(unittest.TestCase):
    def setUp(self):
        dataset_path = "datasets/BooksDatasetClean.csv"
        self.df = pd.read_csv(dataset_path)

    def test_filter_by_publis_year(self):
        """
        Test to see if the function filter by year
        """
        filtered_df = FilteringClass(self.df).filter_by_publis_year(2022)
        self.assertTrue(all(filtered_df["Publish Date (Year)"] == 2022))

    def test_filter_by_publis_month(self):
        """
        Test to see if the function filter by month
        """
        filtered_df = FilteringClass(self.df).filter_by_publis_month("January")
        self.assertTrue(all(filtered_df["Publish Date (Month)"] == "January"))

    def test_filter_price(self):
        """
        Test to see if the function filter by price
        """
        filtered_df = FilteringClass(self.df).filter_price(25)
        self.assertTrue(all(filtered_df["Price Starting With ($)"] > 25))


if __name__ == "__main__":
    unittest.main()
