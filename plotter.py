import matplotlib.pyplot as plt
import numpy as np


class Plotter:
    def __init__(self, df):
        self.df = df

    def draw_plots(self, columns, save_path="plots"):
        """Draws plots for comparing different columns.

        Args:
            columns: A list of column names to compare.
            save_path: The path to save the plots.

        Returns:
            A list of paths to all plots.
        """
        plot_paths = []
        for column in columns:
            fig = plt.figure()
            plt.plot(self.df[column])
            plt.xlabel("Index")
            plt.ylabel(column)
            plt.title(f"Comparison of {column}")
            plt.grid(True)

            plot_path = f"{save_path}/{column}.png"
            plt.savefig(plot_path)
            plot_paths.append(plot_path)

        return plot_paths
