#!/usr/bin/env python3
# Unit 18: Explore a real dataset before doing any machine learning.
#
# Big idea: data science starts by LOOKING at the data: how big is it, what
# do the columns mean, what are typical values, and how do the groups differ?
# We use the famous Iris dataset: 150 flowers from 3 species, with 4
# measurements each. It comes built in with scikit-learn, so no download.

# --- 1. Setup --------------------------------------------------------------------------------
## Path builds the folder location for saved charts.
from pathlib import Path

## matplotlib draws the charts (Unit 17).
import matplotlib
## Draw to files so the unit runs without a screen.
matplotlib.use("Agg")
## The plotting interface.
import matplotlib.pyplot as plt
## numpy does the number crunching (Unit 16).
import numpy as np
## load_iris() returns the Iris dataset that ships with scikit-learn.
from sklearn.datasets import load_iris

## The folder for saved charts, next to this script.
PLOTS = Path(__file__).parent / "plots"
## Create it if needed.
PLOTS.mkdir(exist_ok=True)

# --- 2. Load the data ----------------------------------------------------------------------------
## The dataset object holds the numbers plus descriptions.
iris = load_iris()
## X is a 2-D array: one ROW per flower, one COLUMN per measurement ("feature").
X = iris.data
## y is a 1-D array of species numbers: 0, 1 or 2 (the "target" or "label").
y = iris.target
## The names of the four measurement columns.
feature_names = iris.feature_names
## The names that go with species numbers 0, 1 and 2.
species_names = iris.target_names

# --- 3. First look ---------------------------------------------------------------------------------
## (150, 4) means 150 flowers and 4 measurements each.
print("X shape:", X.shape, "| y shape:", y.shape)
## What each column means.
print("Features:", feature_names)
## What each species number means; .tolist() turns the array into a plain list.
print("Species:", species_names.tolist())
## Always look at a few raw rows; they reveal units and typical values.
print("First 3 rows:\n", X[:3])
## Labels of the first 3 rows (all species 0, setosa).
print("First 3 labels:", y[:3])

# --- 4. How many of each class? ------------------------------------------------------------------------
## np.unique with return_counts=True gives each value and how often it appears.
labels, counts = np.unique(y, return_counts=True)
## zip pairs each label with its count.
for label, count in zip(labels, counts):
    ## A balanced dataset has similar counts for each class.
    print(f"  {species_names[label]:<11} {count} flowers")

# --- 5. Summary statistics for each feature --------------------------------------------------------------
## Header row for a small table.
print(f"\n{'feature':<20}{'mean':>7}{'std':>7}{'min':>7}{'max':>7}")
## enumerate gives the column number and its name.
for column, name in enumerate(feature_names):
    ## X[:, column] is every row of this one column.
    values = X[:, column]
    ## One aligned line of statistics per feature.
    print(f"{name:<20}{values.mean():>7.2f}{values.std():>7.2f}"
          f"{values.min():>7.1f}{values.max():>7.1f}")

# --- 6. Compare the groups ---------------------------------------------------------------------------------
## A blank line, then a heading.
print("\nAverage petal length by species:")
## Visit species 0, 1, 2.
for label, name in enumerate(species_names):
    ## The mask y == label keeps only rows of this species (Unit 16).
    petal_lengths = X[y == label, 2]
    ## A big difference between groups is a hint that ML can tell them apart.
    print(f"  {name:<11} {petal_lengths.mean():.2f} cm")

# --- 7. Correlation between features -----------------------------------------------------------------------
## corrcoef with rowvar=False treats each COLUMN as a variable: gives a 4x4 table.
correlation = np.corrcoef(X, rowvar=False)
## Values near +1: rise together; near -1: one rises as the other falls; 0: unrelated.
print("\nCorrelation matrix (rounded):\n", np.round(correlation, 2))
## Petal length (column 2) vs petal width (column 3) is very strongly related.
print("Petal length vs petal width:", round(correlation[2, 3], 2))

# --- 8. Visualise: scatter plot coloured by species ----------------------------------------------------------
## A new figure and axes.
fig, ax = plt.subplots(figsize=(6, 4.5))
## Draw each species separately so each gets its own colour and legend entry.
for label, name in enumerate(species_names):
    ## Mask for this species.
    rows = y == label
    ## Column 2 (petal length) on x, column 3 (petal width) on y.
    ax.scatter(X[rows, 2], X[rows, 3], label=name, alpha=0.7)
## Use the real feature names as axis labels.
ax.set_xlabel(feature_names[2])
## The y label.
ax.set_ylabel(feature_names[3])
## Title.
ax.set_title("Iris petals: the species form clear groups")
## The legend shows which colour is which species.
ax.legend()
## Light grid.
ax.grid(alpha=0.3)
## Fit everything.
fig.tight_layout()
## Save the chart.
fig.savefig(PLOTS / "iris_scatter.png", dpi=120)
## Free memory.
plt.close(fig)
## Report.
print("\nSaved plots/iris_scatter.png")

# --- 9. Visualise: one histogram per feature --------------------------------------------------------------------
## A 2 x 2 grid of plots, one for each of the 4 features.
fig, axes = plt.subplots(2, 2, figsize=(9, 6))
## axes.flat walks the 2-D grid as a flat list; zip pairs it with column numbers.
for column, ax in zip(range(4), axes.flat):
    ## Overlay one histogram per species in this feature.
    for label, name in enumerate(species_names):
        ## alpha=0.5 lets overlapping bars show through.
        ax.hist(X[y == label, column], bins=15, alpha=0.5, label=name)
    ## The feature name as this subplot's title.
    ax.set_title(feature_names[column])
## One shared legend in the first subplot is enough.
axes[0, 0].legend()
## A title for the whole figure.
fig.suptitle("How each measurement differs between species")
## Fit everything.
fig.tight_layout()
## Save.
fig.savefig(PLOTS / "iris_histograms.png", dpi=120)
## Free memory.
plt.close(fig)
## Report.
print("Saved plots/iris_histograms.png")

# --- What we learned --------------------------------------------------------------------------------------------
# * The data is clean (no missing values) and balanced (50 of each species).
# * Petal measurements separate the species far better than sepal ones.
# * Setosa is completely separate; versicolor and virginica overlap a little.
# These clues tell us a simple ML model should work well (Unit 19).

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Print the average SEPAL width for each species. Which is widest?
#   2. Draw the scatter plot using the two sepal columns. Are groups clearer?
#   3. Find the single flower with the longest petal and print its species.
#   4. Load sklearn.datasets.load_wine() and repeat this exploration.
# ---------------------------------------------------------------------------
