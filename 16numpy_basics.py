#!/usr/bin/env python3
# Unit 16: Data science starts with numpy arrays.
#
# Big idea: numpy stores many numbers in one "array" and does maths on all of
# them at once (this is called vectorisation). It is much faster than Python
# loops and is the foundation of matplotlib, pandas and scikit-learn.
#
# Setup (once):  python3 -m pip install -r requirements.txt

# --- 1. Importing numpy ----------------------------------------------------------------
## Everyone imports numpy with the short nickname np.
import numpy as np

# --- 2. Creating arrays ----------------------------------------------------------------
## np.array() turns a Python list into a numpy array.
heights_cm = np.array([152, 160, 171, 165, 180, 158])
## Shows the array (no commas, which is how numpy prints).
print("Heights:", heights_cm)
## arange() is like range() but returns an array: 0, 2, 4, 6, 8.
print("arange(0, 10, 2):", np.arange(0, 10, 2))
## linspace(0, 1, 5) gives 5 evenly spaced values from 0 to 1 INCLUDING 1.
print("linspace(0, 1, 5):", np.linspace(0, 1, 5))
## zeros() makes an array filled with 0.0; useful as a starting point.
print("zeros(4):", np.zeros(4))
## ones() makes an array of 1.0.
print("ones(3):", np.ones(3))

# --- 3. Shape, size and type ------------------------------------------------------------
## .shape gives the size of each dimension; (6,) means 6 items in 1 dimension.
print("shape:", heights_cm.shape)
## .size is the total number of items.
print("size:", heights_cm.size)
## .dtype is the type of every item (all items in an array share one type).
print("dtype:", heights_cm.dtype)

# --- 4. Vectorised maths: no loop needed ------------------------------------------------
## Dividing the array divides EVERY item: centimetres to metres.
heights_m = heights_cm / 100
## Shows six values in metres.
print("Heights in metres:", heights_m)
## Matching weights for the same six people.
weights_kg = np.array([48, 55, 70, 62, 85, 50])
## Item-by-item maths between two arrays of the same length: BMI for everyone.
bmi = weights_kg / heights_m ** 2
## np.round(..., 1) rounds every item to one decimal place.
print("BMI:", np.round(bmi, 1))

## For comparison, the same calculation with a plain Python loop.
bmi_loop = []
## zip pairs each weight with its height (Unit 14).
for w, h in zip(weights_kg, heights_m):
    ## Calculate one BMI at a time.
    bmi_loop.append(round(float(w / h ** 2), 1))
## Same numbers, more code.
print("BMI with a loop:", bmi_loop)

# --- 5. Summary statistics ----------------------------------------------------------------
## mean() is the average; round() keeps two decimal places.
print("Mean height:", round(heights_cm.mean(), 2))
## np.median() is the middle value after sorting.
print("Median height:", np.median(heights_cm))
## std() is the standard deviation: how spread out the values are.
print("Std deviation:", round(heights_cm.std(), 2))
## min() and max() give the smallest and largest values.
print("Min / max:", heights_cm.min(), "/", heights_cm.max())
## argmax() gives the POSITION (index) of the largest value.
print("Tallest person is at index:", heights_cm.argmax())

# --- 6. Indexing, slicing and boolean masks ------------------------------------------------
## Indexing and slicing work just like lists.
print("First three:", heights_cm[:3])
## A comparison on an array gives an array of True/False (a "mask").
is_tall = heights_cm > 165
## Shows which people are taller than 165 cm.
print("Mask (taller than 165):", is_tall)
## Using the mask as an index keeps only the True positions.
print("Tall heights:", heights_cm[is_tall])
## True counts as 1, so sum() counts how many are True.
print("How many are tall:", is_tall.sum())
## Combine masks with & (and) or | (or); brackets are required.
print("Between 155 and 170:", heights_cm[(heights_cm > 155) & (heights_cm < 170)])

# --- 7. 2-D arrays: tables of numbers -------------------------------------------------------
## Each row is a student; each column is a test.
scores = np.array([
    [80, 92, 77],
    [65, 70, 88],
    [90, 85, 95],
])
## shape (3, 3) means 3 rows and 3 columns.
print("Scores shape:", scores.shape)
## [row, column]: row 1, column 2 is 88.
print("Student 1, test 2:", scores[1, 2])
## [:, 0] means "every row, column 0": all results for the first test.
print("All results for test 0:", scores[:, 0])
## axis=1 works ACROSS each row: one average per student.
print("Average per student:", np.round(scores.mean(axis=1), 1))
## axis=0 works DOWN each column: one average per test.
print("Average per test:", np.round(scores.mean(axis=0), 1))
## reshape() changes the shape without changing the data: 6 items -> 2 x 3.
print("arange(6) reshaped to 2x3:\n", np.arange(6).reshape(2, 3))

# --- 8. Random numbers for experiments ------------------------------------------------------
## A random generator with a fixed seed gives the same "random" numbers each run.
rng = np.random.default_rng(42)
## 1000 values from a normal (bell-shaped) distribution: mean 170, spread 8.
simulated_heights = rng.normal(loc=170, scale=8, size=1000)
## The sample mean should be close to 170.
print("Simulated mean height:", round(simulated_heights.mean(), 1))
## integers(1, 7, size=10) rolls a six-sided die ten times (7 is excluded).
print("Ten dice rolls:", rng.integers(1, 7, size=10))

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Convert an array of Celsius temperatures to Fahrenheit in one line.
#   2. From 1000 dice rolls, find the fraction that were a 6.
#   3. In the scores table, find which student has the highest average.
#   4. Use a mask to replace every negative number in an array with 0.
# ---------------------------------------------------------------------------
