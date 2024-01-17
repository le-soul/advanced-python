"""
Filtering Class
"""


class FilteringClass:
    """
    Class for filtering
    """

    def __init__(self, df):
        self.df = df

    def filter_by_publis_year(self, year):
        """
        Filter books by a given year
        """
        return self.df[self.df["Publish Date (Year)"] == year]

    def filter_by_publis_month(self, month):
        """
        Filter books by a given month
        """
        return self.df[self.df["Publish Date (Month)"] == month]

    def filter_pricem(self, pricem):
        """
        Filter books by given price, more than
        """
        return self.df[self.df["Price Starting With ($)"] > pricem]
    
    def filter_pricel(self, pricel):
        """
        Filter books by given price, less than
        """
        return self.df[self.df["Price Starting With ($)"] < pricel]
