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

    def filter_price(self, price):
        """
        Filter books by given price
        """
        return self.df[self.df["Price Starting With ($)"] > price]
