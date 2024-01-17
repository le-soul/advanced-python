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


