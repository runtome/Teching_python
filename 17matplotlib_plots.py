#!/usr/bin/env python3
# Unit 17: Visualise data with matplotlib.
#
# Big idea: a chart shows patterns that are hard to see in a table of
# numbers. matplotlib draws charts; every chart has a Figure (the whole
# picture) containing one or more Axes (the plotting areas).
#
# This unit SAVES each chart as a PNG in the plots/ folder. Open the files
# to look at them. To pop up a window instead, replace plt.savefig(...) with
# plt.show() and remove the matplotlib.use("Agg") line.

# --- 1. Setup ------------------------------------------------------------------------------
## Path builds the folder location for the saved charts.
from pathlib import Path

## matplotlib is the plotting library.
import matplotlib
## "Agg" draws straight to image files, so this runs without a screen.
matplotlib.use("Agg")
## pyplot is the part we use to draw; everyone calls it plt.
import matplotlib.pyplot as plt
## numpy creates the data (Unit 16).
import numpy as np

## The plots folder sits next to this script.
PLOTS = Path(__file__).parent / "plots"
## Create it if it does not exist yet; no error if it already does.
PLOTS.mkdir(exist_ok=True)
## A seeded random generator so the charts look the same every run.
rng = np.random.default_rng(7)

# --- 2. Line plot: change over time ---------------------------------------------------------
## Labels for the x axis.
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
## One temperature per day for Bangkok.
bangkok = [33, 34, 32, 35, 36, 34, 33]
## And for Chiang Mai.
chiang_mai = [29, 30, 28, 31, 32, 30, 27]
## Start a new figure; figsize is (width, height) in inches.
plt.figure(figsize=(7, 4))
## plot() draws a line; marker="o" adds a dot at each point; label is for the legend.
plt.plot(days, bangkok, marker="o", label="Bangkok")
## A second line on the same axes, with a dashed style.
plt.plot(days, chiang_mai, marker="s", linestyle="--", label="Chiang Mai")
## A title at the top.
plt.title("Daily maximum temperature")
## Always label your axes, including units.
plt.xlabel("Day")
## The y axis label.
plt.ylabel("Temperature (°C)")
## legend() shows which line is which, using the labels above.
plt.legend()
## A light grid makes values easier to read.
plt.grid(alpha=0.3)
## tight_layout() stops labels from being cut off.
plt.tight_layout()
## Save the figure as a PNG file.
plt.savefig(PLOTS / "line.png", dpi=120)
## close() frees memory before starting the next chart.
plt.close()
## Tell the learner where the file went.
print("Saved plots/line.png")

# --- 3. Bar chart: comparing categories --------------------------------------------------------
## Category names.
fruits = ["Mango", "Durian", "Banana", "Rambutan"]
## One value per category.
sales = [120, 45, 160, 80]
## plt.subplots() returns the figure and its axes; using "ax" is the
## object-oriented style that scales well to bigger charts.
fig, ax = plt.subplots(figsize=(6, 4))
## bar() draws one bar per category.
bars = ax.bar(fruits, sales, color="tab:orange")
## Write each value on top of its bar.
ax.bar_label(bars)
## With the ax style, title/label methods start with set_.
ax.set_title("Fruit sold this week")
## The y axis label.
ax.set_ylabel("Kilograms")
## Fit everything inside the figure.
fig.tight_layout()
## Save the figure.
fig.savefig(PLOTS / "bar.png", dpi=120)
## Free the memory.
plt.close(fig)
## Report the file.
print("Saved plots/bar.png")

# --- 4. Scatter plot: the relationship between two numbers ----------------------------------------
## 40 random study times between 0 and 10 hours.
hours = rng.uniform(0, 10, size=40)
## Score rises about 6 points per hour, plus random noise.
exam_score = 40 + 6 * hours + rng.normal(0, 6, size=40)
## np.clip() keeps every score inside the real range 0-100.
exam_score = np.clip(exam_score, 0, 100)
## A new figure and axes.
fig, ax = plt.subplots(figsize=(6, 4))
## scatter() draws one dot per (x, y) pair; alpha makes dots see-through.
ax.scatter(hours, exam_score, alpha=0.7)
## Title.
ax.set_title("Study time vs exam score")
## x label.
ax.set_xlabel("Hours studied")
## y label.
ax.set_ylabel("Score")
## Light grid.
ax.grid(alpha=0.3)
## Fit everything.
fig.tight_layout()
## Save.
fig.savefig(PLOTS / "scatter.png", dpi=120)
## Free memory.
plt.close(fig)
## np.corrcoef gives the correlation: near +1 means "rises together".
print("Saved plots/scatter.png", "| correlation:",
      round(np.corrcoef(hours, exam_score)[0, 1], 2))

# --- 5. Histogram: how values are distributed ---------------------------------------------------------
## 500 simulated heights with mean 165 cm and spread 7 cm.
heights = rng.normal(165, 7, size=500)
## A new figure and axes.
fig, ax = plt.subplots(figsize=(6, 4))
## hist() counts how many values fall into each of 20 "bins".
ax.hist(heights, bins=20, color="tab:green", edgecolor="white")
## axvline() draws a vertical line, here at the mean.
ax.axvline(heights.mean(), color="black", linestyle="--", label="mean")
## Title.
ax.set_title("Distribution of 500 heights")
## x label.
ax.set_xlabel("Height (cm)")
## y label: how many people are in each bin.
ax.set_ylabel("Count")
## Show the legend for the mean line.
ax.legend()
## Fit everything.
fig.tight_layout()
## Save.
fig.savefig(PLOTS / "histogram.png", dpi=120)
## Free memory.
plt.close(fig)
## Report.
print("Saved plots/histogram.png")

# --- 6. Several charts in one figure (subplots) -----------------------------------------------------------
## subplots(2, 2) makes a 2 x 2 grid; axes is a 2-D array of Axes objects.
fig, axes = plt.subplots(2, 2, figsize=(9, 7))
## Top-left: the line chart again.
axes[0, 0].plot(days, bangkok, marker="o")
## Its title.
axes[0, 0].set_title("Line: temperature")
## Top-right: the bar chart.
axes[0, 1].bar(fruits, sales, color="tab:orange")
## Its title.
axes[0, 1].set_title("Bar: fruit sales")
## Bottom-left: the scatter plot.
axes[1, 0].scatter(hours, exam_score, alpha=0.7)
## Its title.
axes[1, 0].set_title("Scatter: hours vs score")
## Bottom-right: the histogram.
axes[1, 1].hist(heights, bins=20, color="tab:green", edgecolor="white")
## Its title.
axes[1, 1].set_title("Histogram: heights")
## suptitle() is one title for the whole figure.
fig.suptitle("Four common chart types")
## Fit everything.
fig.tight_layout()
## Save.
fig.savefig(PLOTS / "dashboard.png", dpi=120)
## Free memory.
plt.close(fig)
## Report.
print("Saved plots/dashboard.png")

# --- Choosing a chart ------------------------------------------------------------------------------------
# * Line      -> how something changes over time.
# * Bar       -> comparing amounts between categories.
# * Scatter   -> whether two numeric variables are related.
# * Histogram -> how one numeric variable is spread out.
# Always add a title, axis labels with units, and a legend when there are
# several series.

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Add a third city to the line chart.
#   2. Make the bar chart horizontal with ax.barh().
#   3. Change the histogram to 40 bins. What changes?
#   4. Plot y = x ** 2 for x = np.linspace(-5, 5, 100).
# ---------------------------------------------------------------------------
