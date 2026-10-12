# Beginner Python Learning Curriculum

This curriculum contains small, runnable examples that build from basic output
to object-oriented programming, then on to an introduction to data science and
machine learning. Units 1–15 use only the Python standard library; units 16–19
use numpy, matplotlib and scikit-learn.

## Python fundamentals (units 1–15)

1. [Basics and `print()`](01python_basics.py) — display text and simple results.
2. [Variables and types](02python_variables.py) — name values and inspect common types.
3. [Operators and input](03python_operators_input.py) — calculate, compare, and read a response with a safe default.
4. [Conditionals](04python_conditionals.py) — choose a path with `if`, `elif`, `else`, and `match`.
5. [Loops](05python_loops.py) — repeat actions with `for` and `while`.
6. [Functions](06python_functions.py) — reuse steps with parameters and return values.
7. [Strings](07python_strings.py) — clean, inspect, and format text.
8. [Lists](08python_lists.py) — keep and process an ordered sequence.
9. [Collections](09python_collections.py) — use dictionaries, tuples, and sets.
10. [Exceptions and files](10python_exceptions_files.py) — handle errors and read/write a temporary text file.
11. [Classes](11python_classes.py) — define a class and create an object, methods, special methods, properties.
12. [Inheritance](12python_inheritance.py) — child classes, `super()`, polymorphism, and composition.
13. [Modules and the standard library](13python_modules_stdlib.py) — `import`, `math`, `random`, `datetime`, `collections`, `statistics`, `json`, and `__name__ == "__main__"`.
14. [Iterators and generators](14python_iterators_generators.py) — `zip`, `any`/`all`, `sorted(key=...)`, `map`/`filter`, `yield`, and generator expressions.
15. [Mini project: grade book](15python_mini_project.py) — combine every unit into one small, tested program.

## Data science and machine learning (units 16–19)

16. [numpy basics](16numpy_basics.py) — arrays, vectorised maths, statistics, boolean masks, 2-D tables, and random numbers.
17. [Charts with matplotlib](17matplotlib_plots.py) — line, bar, scatter, and histogram charts, plus a multi-chart dashboard.
18. [Exploring a dataset](18data_exploration.py) — inspect the Iris flower data: class counts, summary statistics, group comparisons, correlation, and charts.
19. [Machine learning basics](19ml_basics.py) — train/test split, linear regression, k-nearest neighbours, decision trees, accuracy, confusion matrix, and overfitting.

Units 17–19 save their charts as PNG images in a `plots/` folder next to the
scripts. Open those files to see the charts.

## How to read the code

Every line of code has a comment starting with `##` directly above it that
explains what that line does:

```python
## Store the learner's name as text (a string).
learner_name = "Sam"
## print() shows the value on the screen.
print(learner_name)
```

Lines that start with a single `#` are section headings
(`# --- 1. Printing text ---`), notes, and the exercises at the end of each
file. Many units also include a **Common mistakes** note, and every unit ends
with **Try it yourself** exercises. A suggested way to study:

1. Read the `##` comments in a section and predict what the code will print.
2. Run the script and compare the output with your prediction.
3. Change a value, run it again, and see what happens.
4. Finish with the exercises at the bottom of the file.

## Setup

Install Python 3.10 or newer (Unit 4 uses `match`). Units 1–15 need nothing
else. For units 16–19, install the data science libraries once, preferably in a
virtual environment:

```sh
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python3 -m pip install -r requirements.txt
```

## Run a unit

Open a terminal in this directory and run any unit with:

```sh
python3 01python_basics.py
```

Replace the filename with another unit from the list to run that lesson. Unit 3
prompts for a favorite color and a birth year; pressing Enter (or running
without interactive input) uses the example values.

To run every unit in order and check that they all work:

```sh
for f in [0-9]*.py; do echo "== $f"; python3 "$f" < /dev/null || break; done
```
