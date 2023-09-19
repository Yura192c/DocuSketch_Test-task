import matplotlib.pyplot as plt

from plotter import Plotter
import pandas as pd


def draw_plots(json_file, save_path="plots"):
    """Reads a JSON file as a Pandas DataFrame and draws plots for comparing different columns.

    Args:
        json_file: The path to the JSON file.
        save_path: The path to save the plots.

    Returns:
        A list of paths to all plots.
    """
    df = pd.read_json(json_file)
    plotter = Plotter(df)

    plot_paths = plotter.draw_plots(columns=["gt_corners", "rb_corners", "mean", "max", "min"], save_path=save_path)

    return plot_paths
