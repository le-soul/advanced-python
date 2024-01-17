"""
Analysis Class
"""

import matplotlib.pyplot as plt


class BookAnalysis:
    """
    Class to analyse database with graphs
    """

    def __init__(self, df):
        self.df = df

    def plot_category_distribution(self):
        """
        Plot the distribution of books in each category
        """
        categories_list = self.df["Category"].str.split(", ").explode()
        category_counts = categories_list.value_counts()
        plt.figure(figsize=(10, 6))
        category_counts.plot(kind="bar", color="skyblue")
        plt.title("Distribution of Books in Each Category")
        plt.xlabel("Category")
        plt.ylabel("Number of Books")

    def scatter_plot_price_vs_year(self):
        """
        Create a scatter plot of book prices vs. publish year
        """
        plt.figure(figsize=(12, 8))
        plt.scatter(
            self.df["Publish Date (Year)"],
            self.df["Price Starting With ($)"],
            alpha=0.5,
        )
        plt.title("Scatter Plot of Book Prices vs. Publish Year")
        plt.xlabel("Publish Year")
        plt.ylabel("Price Starting With ($)")
        plt.grid(True)

    def perform_analysis(self, analysis_type):
        """
        Perform the specified analysis based on the provided analysis type.
        """
        if analysis_type == "distribution":
            self.plot_category_distribution()
        elif analysis_type == "scatter":
            self.scatter_plot_price_vs_year()
        else:
            raise ValueError(f"Unknown analysis type: {analysis_type}")
