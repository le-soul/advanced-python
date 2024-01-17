"""
Script to make updates in github
"""
import sys

sys.path.append("scripts")
import click
import pandas as pd
import filtering as fg
import plots as p
import os
import matplotlib.pyplot as plt
import cleaning as cl


def load_dataset(filename):
    """
    Function to load dataset
    """
    extension = filename.rsplit(".", 1)[-1]
    if extension == "csv":
        return pd.read_csv(filename)
    else:
        raise TypeError(f"The extension is {extension} and not csv. Try again")


def filter_all(month=None, year=None, price=None):
    """ """

    print("I am filtering")

    if month:
        df = fg.FilteringClass(df).filter_by_publis_month(month)

    if year:
        df = fg.FilteringClass(df).filter_by_publis_year(year)

    if price:
        df = fg.FilteringClass(df).filter_price(price)
    print(df.head())
    print(df.shape)


@click.command(short_help="Parser to import dataset")
@click.option("-c", "--cleaning", is_flag=True, help="File to import")
@click.option(
    "-d", "--display", is_flag=True, help="Display the null and duplicate values"
)
@click.option("-cl", "--clean", is_flag=True, help="Delete null and duplicate values")
@click.option("-f", "--filename", required=True, help="File to import")
@click.option("-o", "--output", default="outputs", help="Folder to save all outputs")
@click.option("-fi", "--filtering", is_flag=True, help="Set a filtering or not")
@click.option("-p", "--price", type=float, help="Filter books by price")
@click.option("-m", "--month", type=str, help="Filter books by month")
@click.option("-y", "--year", type=int, help="Filter books by year")
@click.option("-a", "--analysis", is_flag=True, help="Analyse the data or not")
@click.option(
    "-g", "--graph", type=str, help="Type of book analysis (distribution or scatter)"
)
def main(
    filename,
    output,
    filtering,
    analysis,
    price,
    month,
    year,
    graph,
    cleaning,
    display,
    clean,
):
    """
    Main function
    """
    df = load_dataset(filename)
    if cleaning:
        print("I am cleaning")
        if display:
            cl.CleaningClass(df).display_null_and_duplicates_info()

        if clean:
            df = cl.CleaningClass(df).clean_data()

    if filtering:
        df = filter_all(month, year, price)

    try:
        df.to_csv(f"{output}/final_df.csv", index=None)
    except Exception as e:
        if not os.path.exists(output):
            os.makedirs(output)
        df.to_csv(f"{output}/final_df.csv", index=None)

    if analysis:
        print("I am analysing")

        if graph:
            p.BookAnalysis(df).perform_analysis(graph)
            if not os.path.exists(output):
                os.makedirs(output)

            if graph == "distribution":
                plt.savefig(f"{output}/DistributionPlot.png")
            elif graph == "scatter":
                plt.savefig(f"{output}/Scatter.png")


if __name__ == "__main__":
    main()
