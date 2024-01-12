"""
Script to make updates in github
"""

import click
import pandas as pd 


class FilteringClass:
    """
    Class for filtering
    """

    def __init__(self, df):
        self.df = df

    def filter_price(self, price):
        """
        filter by price
        """
        return self.df[self.df["price"] > price]

@click.command(short_help="Parser to import dataset")
@click.option("-f", "--filename", require=True, help="File to import")

def main(filename):
    """
    Main function
    """

    df = pd.read_csv(filename)
    import pdb;pdb.set_trace()

    print(df.shape)

if __name__ == "__main__":
    main()