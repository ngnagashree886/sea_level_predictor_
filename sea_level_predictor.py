import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read the data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Line of best fit using all data
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Years from the first year to 2050
    years = pd.Series(range(df["Year"].min(), 2051))

    # Predicted sea levels
    sea_levels = slope * years + intercept

    # Plot the first line of best fit
    ax.plot(years, sea_levels)

    # Line of best fit using data from 2000 onwards
    df_recent = df[df["Year"] >= 2000]

    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    # Years from 2000 to 2050
    years_recent = pd.Series(range(2000, 2051))

    # Predicted sea levels
    sea_levels_recent = slope_recent * years_recent + intercept_recent

    # Plot the second line of best fit
    ax.plot(years_recent, sea_levels_recent)

    # Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save figure
    fig.savefig("sea_level_plot.png")

    return fig