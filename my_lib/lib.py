import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn.objects as so
import seaborn as sns
from matplotlib import style

sns.set_style("whitegrid")


def get_data(dataset):
    data = pd.read_csv(dataset)
    return data


def get_mean(df, col):
    return df[col].mean()


def get_median(df, col):
    return df[col].median()


def summary(df):
    return df.describe()


def vizualisation(data, first_column="EngineSize", second_column="MPG_Highway"):
    sns.set_style("whitegrid")
    my_chart = (
        so.Plot(data, first_column, second_column)
        .add(so.Line(color="r"), so.PolyFit(order=2))
        .add(so.Dot())
        .label(title=f"Visualization of {first_column} and {second_column}")
    )
    try:
        my_chart.save(f"Visualization_of_{first_column}_&_{second_column}.png")
    except Exception as e:
        print(f"Error saving plot: {e}")
    return my_chart


def create_histogram(df, column="Horsepower"):
    plt.figure(figsize=(10, 6))
    plt.hist(df[column], bins=20, color="blue", edgecolor="black")
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.savefig(f"{column}_histogram.png")
    plt.show()


def correlation_matrix(df):
    df = df.select_dtypes(float)
    plt.figure(figsize=(14, 10))
    plt.matshow(
        df.corr(),
        cmap="coolwarm",
    )
    plt.title("Correlation Matrix", pad=20)
    plt.colorbar()
    plt.savefig("correlation_matrix.png")
    plt.show()
