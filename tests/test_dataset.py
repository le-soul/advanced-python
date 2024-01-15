"""
Test loading of the dataset
"""

import unittest
from scripts.repo_first_script import load_dataset


class TestDataset(unittest.TestCase):
    """
    Class to test the dataset input in different ways
    """

    def setUp(self):
        """
        Path to dataset
        """
        self.path = "datasets/BooksDatasetClean.aassacsv"
    
    def test_extension_fail(self):
        """
        Test for the extension of the dataset
        """
        with self.assertRaises(TypeError):
            load_dataset(self.path)

if __name__ == "__main__":
    unittest.main()