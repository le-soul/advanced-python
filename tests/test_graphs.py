"""
Test for graphs
"""

import unittest
import pandas as pd
from scripts.plots import BookAnalysis


class TestBookAnalysis(unittest.TestCase):
    """
    Class to test the graphs for analysis
    """

    def setUp(self):
        data = {
            "Category": ["Fiction", "Non-Fiction", "Fiction", "Mystery"],
            "Publish Date (Year)": [2010, 2004, 2002, 2009],
            "Price Starting With ($)": [10.0, 12.0, 4.0, 3.0],
        }
        self.df = pd.DataFrame(data)
        self.book_analysis = BookAnalysis(self.df)

    def test_plot_category_distribution(self):
        """
        Test to see if the distribution graph shows an error or not
        """
        self.book_analysis.plot_category_distribution()

    def test_scatter_plot_price_vs_year(self):
        """
        Test to see if the scatter graph shows an error or not
        """
        self.book_analysis.scatter_plot_price_vs_year()


if __name__ == "__main__":
    unittest.main()
