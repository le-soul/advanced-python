"""
Cleaning Class
"""


class CleaningClass:
    """
    
    """
    def __init__(self, df):
        self.df = df

    def display_null_and_duplicates_info(self):
        """
        
        """
        null_info = self.df.isnull().sum()
        print("Null Values Information:")
        print(null_info)
        duplicate_info = self.df.duplicated().sum()
        print("Duplicate Values Information:")
        print(duplicate_info)

    def clean_data(self):
        """
        
        """
        self.df = self.df.drop_duplicates()
        self.df = self.df.dropna()

        return self.df
