#!/usr/bin/env python3
# Unit 19: Your first machine learning models with scikit-learn.
#
# Big idea: machine learning (ML) means letting a program LEARN a rule from
# examples instead of us writing the rule by hand.
#   * X (features)  — the information we know, e.g. hours studied.
#   * y (label)     — the answer we want to predict, e.g. exam score.
#   * Regression     predicts a NUMBER    (What score will they get?)
#   * Classification predicts a CATEGORY  (Which species is this flower?)
# Every scikit-learn model follows the same three steps:
#     model = SomeModel()      choose a model
#     model.fit(X, y)          learn from examples
#     model.predict(new_X)     make predictions

# --- 1. Setup --------------------------------------------------------------------------------
## Path builds the folder location for saved charts.
from pathlib import Path

## matplotlib draws the charts.
import matplotlib
## Draw to files so the unit runs without a screen.
matplotlib.use("Agg")
## The plotting interface.
import matplotlib.pyplot as plt
## numpy creates and handles the data.
import numpy as np
## The built-in Iris flower dataset (explored in Unit 18).
from sklearn.datasets import load_iris
## A straight-line model for regression.
from sklearn.linear_model import LinearRegression
## Scores that tell us how good the predictions are.
from sklearn.metrics import (ConfusionMatrixDisplay, accuracy_score,
                             confusion_matrix, mean_absolute_error, r2_score)
## Splits data into a part to learn from and a part to test on.
from sklearn.model_selection import train_test_split
## "k nearest neighbours": classify by looking at the most similar examples.
from sklearn.neighbors import KNeighborsClassifier
## A model that learns a flowchart of yes/no questions.
from sklearn.tree import DecisionTreeClassifier, export_text

## The folder for saved charts, next to this script.
PLOTS = Path(__file__).parent / "plots"
## Create it if needed.
PLOTS.mkdir(exist_ok=True)
## A seeded generator makes the data, and so the results, repeatable.
rng = np.random.default_rng(0)

# ===========================================================================
# PART A — Regression: predict a number
# ===========================================================================

# --- 2. Make some data -----------------------------------------------------------------------------
## 60 students who studied between 0 and 10 hours.
hours = rng.uniform(0, 10, size=60)
## The hidden "true" rule is score = 35 + 6 * hours, plus random noise.
scores = np.clip(35 + 6 * hours + rng.normal(0, 5, size=60), 0, 100)
## scikit-learn wants X as a 2-D table (rows x features); reshape(-1, 1)
## turns 60 numbers into 60 rows with 1 column.
X_hours = hours.reshape(-1, 1)
## Show the shapes: X is (60, 1), y is (60,).
print("Regression data:", X_hours.shape, scores.shape)

# --- 3. Split into training and test sets --------------------------------------------------------------
## Keep 25% of the rows hidden from the model so we can test it fairly.
## random_state fixes the shuffle so the split is the same every run.
X_train, X_test, y_train, y_test = train_test_split(
    X_hours, scores, test_size=0.25, random_state=0)
## 45 rows to learn from, 15 rows to test on.
print("Train rows:", len(X_train), "| Test rows:", len(X_test))

# --- 4. Train (fit) the model ----------------------------------------------------------------------------
## Choose the model: a straight line y = slope * x + intercept.
regressor = LinearRegression()
## fit() finds the slope and intercept that best match the training data.
regressor.fit(X_train, y_train)
## coef_ holds the learned slope; it should be close to the true 6.
print(f"Learned slope: {regressor.coef_[0]:.2f} points per hour")
## intercept_ is the predicted score for 0 hours; close to the true 35.
print(f"Learned intercept: {regressor.intercept_:.2f}")

# --- 5. Predict and evaluate --------------------------------------------------------------------------------
## Predict scores for the test students the model has never seen.
predictions = regressor.predict(X_test)
## Show three predictions next to the real answers.
for real, guess in list(zip(y_test, predictions))[:3]:
    ## :.1f shows one decimal place.
    print(f"  real {real:.1f}  predicted {guess:.1f}")
## Mean absolute error: on average, how many points the predictions are off.
print(f"Mean absolute error: {mean_absolute_error(y_test, predictions):.2f} points")
## R² (R squared): 1.0 is perfect, 0 is no better than always guessing the mean.
print(f"R² score: {r2_score(y_test, predictions):.3f}")
## Use the model on brand-new input: someone who studies 7.5 hours.
new_student = np.array([[7.5]])
## predict() returns an array; [0] takes its only value.
print(f"Prediction for 7.5 hours: {regressor.predict(new_student)[0]:.1f}")

# --- 6. Plot the data and the learned line -------------------------------------------------------------------
## A new figure and axes.
fig, ax = plt.subplots(figsize=(6, 4))
## Training points in one colour.
ax.scatter(X_train, y_train, alpha=0.6, label="training data")
## Test points in another colour.
ax.scatter(X_test, y_test, alpha=0.9, marker="s", label="test data")
## 100 evenly spaced x values to draw a smooth line.
line_x = np.linspace(0, 10, 100).reshape(-1, 1)
## The model's prediction for each of those x values IS the learned line.
ax.plot(line_x, regressor.predict(line_x), color="black", label="learned line")
## Title.
ax.set_title("Linear regression: hours vs score")
## x label.
ax.set_xlabel("Hours studied")
## y label.
ax.set_ylabel("Score")
## Legend.
ax.legend()
## Light grid.
ax.grid(alpha=0.3)
## Fit everything.
fig.tight_layout()
## Save.
fig.savefig(PLOTS / "regression.png", dpi=120)
## Free memory.
plt.close(fig)
## Report.
print("Saved plots/regression.png")

# ===========================================================================
# PART B — Classification: predict a category
# ===========================================================================

# --- 7. Load and split the Iris data ---------------------------------------------------------------------------
## load_iris() gives 150 flowers, 4 measurements each, and 3 species.
iris = load_iris()
## X: measurements, y: species numbers 0/1/2.
X, y = iris.data, iris.target
## stratify=y keeps the same mix of species in the train and test sets.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y)
## A blank line, then the sizes: 105 to train, 45 to test.
print("\nClassification data — train:", X_train.shape, "test:", X_test.shape)

# --- 8. k-nearest neighbours ------------------------------------------------------------------------------------
## To classify a flower, look at the 5 most similar training flowers and vote.
knn = KNeighborsClassifier(n_neighbors=5)
## "Fitting" k-NN simply stores the training examples.
knn.fit(X_train, y_train)
## Predict the species of every test flower.
knn_predictions = knn.predict(X_test)
## Accuracy = fraction of test flowers labelled correctly.
print(f"k-NN accuracy: {accuracy_score(y_test, knn_predictions):.1%}")

# --- 9. Decision tree ------------------------------------------------------------------------------------------
## A tree learns questions like "is petal width <= 0.7 cm?"; max_depth=3
## keeps it small and readable.
tree = DecisionTreeClassifier(max_depth=3, random_state=0)
## Learn the questions from the training data.
tree.fit(X_train, y_train)
## Predict the test flowers.
tree_predictions = tree.predict(X_test)
## Compare its accuracy with k-NN.
print(f"Decision tree accuracy: {accuracy_score(y_test, tree_predictions):.1%}")
## export_text() prints the learned questions as an indented flowchart
## (class 0 = setosa, 1 = versicolor, 2 = virginica).
print(export_text(tree, feature_names=list(iris.feature_names)))

# --- 10. Where does the model make mistakes? ---------------------------------------------------------------------
## Rows = true species, columns = predicted species; the diagonal is correct.
matrix = confusion_matrix(y_test, knn_predictions)
## Print the table of counts.
print("k-NN confusion matrix:\n", matrix)
## from_predictions() draws the same table as a coloured chart.
display = ConfusionMatrixDisplay.from_predictions(
    y_test, knn_predictions, display_labels=iris.target_names, cmap="Blues")
## Give the chart a title.
display.ax_.set_title("k-NN on Iris: true vs predicted")
## Fit everything.
display.figure_.tight_layout()
## Save.
display.figure_.savefig(PLOTS / "confusion_matrix.png", dpi=120)
## Free memory.
plt.close(display.figure_)
## Report.
print("Saved plots/confusion_matrix.png")

# --- 11. Predict a brand-new flower ------------------------------------------------------------------------------
## Measurements in the same order as the features: sepal length, sepal width,
## petal length, petal width (all cm). Double brackets = one row.
new_flower = np.array([[6.1, 2.8, 4.7, 1.2]])
## predict() returns the species number.
species_number = knn.predict(new_flower)[0]
## predict_proba() shows how confident the model is in each species.
probabilities = knn.predict_proba(new_flower)[0]
## Turn the number into a name.
print("New flower is probably:", iris.target_names[species_number])
## Show the vote share for each species.
for name, p in zip(iris.target_names, probabilities):
    ## :.0% shows a whole-number percentage.
    print(f"  {name:<11} {p:.0%}")

# --- 12. Why we test on unseen data -------------------------------------------------------------------------------
## A very deep tree can memorise the training data perfectly...
memoriser = DecisionTreeClassifier(random_state=0)
## ...learn from the training rows...
memoriser.fit(X_train, y_train)
## ...and score 100% on those same rows.
train_acc = accuracy_score(y_train, memoriser.predict(X_train))
## The honest score comes from rows it has never seen.
test_acc = accuracy_score(y_test, memoriser.predict(X_test))
## A big gap between the two numbers is a sign of overfitting. Iris is an
## easy dataset, so the gap is small here; on messy real data it is often large.
print(f"\nDeep tree — train accuracy {train_acc:.1%}, test accuracy {test_acc:.1%}")

# --- Common pitfalls ---------------------------------------------------------------------------------------------
# * Testing on the training data: the score looks great but means nothing.
# * Overfitting: a model that memorises noise does worse on new data.
# * Too little data, or features that do not relate to the label.
# * Forgetting that X must be 2-D: use reshape(-1, 1) for a single feature.

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Change n_neighbors to 1, 3 and 15. How does k-NN accuracy change?
#   2. Train the decision tree with max_depth=1. What single question does it ask?
#   3. Change the regression's hidden rule to 20 + 8 * hours. Does the model
#      learn the new slope and intercept?
#   4. Train k-NN using only the two sepal columns: X[:, :2]. Is it worse?
# ---------------------------------------------------------------------------
