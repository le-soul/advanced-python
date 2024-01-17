"""
Cleaning Class
"""


class CleaningClass:
    """
    Class for viewing null values and duplicates, and deciding on deleting them
    """
    def __init__(self, df):
        self.df = df

    def display_null_and_duplicates_info(self):
        """
        Displays null and duplicate values
        """
        null_info = self.df.isnull().sum()
        print("Null Values Information:")
        print(null_info)
        duplicate_info = self.df.duplicated().sum()
        print("Duplicate Values Information:")
        print(duplicate_info)

    def clean_data(self):
        """
        Deletes the duplicates and null values
        """
        self.df = self.df.drop_duplicates()
        self.df = self.df.dropna()

        return self.df
