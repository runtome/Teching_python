#!/usr/bin/env python3
# Unit 13: Reuse code with import and explore the standard library.
#
# Big idea: a module is a Python file full of useful code. "import" loads it
# so you can use its functions. Python ships with a large "standard library"
# — no installation needed.

# --- 1. Ways to import -----------------------------------------------------------------------
## Import a whole module; use its contents as math.sqrt(...).
import math
## Import a module under a shorter nickname.
import random as rnd
## Import only specific names, so we can write date(...) instead of datetime.date(...).
from datetime import date, timedelta
## Two handy containers from the collections module.
from collections import Counter, defaultdict
## json reads and writes data as JSON text.
import json
## statistics has mean, median and more.
import statistics

# --- 2. math -------------------------------------------------------------------------------------
## Square root: 9.0.
print("sqrt(81) =", math.sqrt(81))
## math.pi is a constant; round() keeps 5 decimals.
print("pi =", round(math.pi, 5))
## ceil() rounds up, floor() rounds down.
print("ceil(4.1) =", math.ceil(4.1), "| floor(4.9) =", math.floor(4.9))
## gcd() is the greatest common divisor: 6.
print("gcd(12, 18) =", math.gcd(12, 18))
## hypot() gives the long side of a right-angled triangle: 5.0.
print("hypot(3, 4) =", math.hypot(3, 4))

# --- 3. random -----------------------------------------------------------------------------------
## seed() makes "random" results repeatable — great for lessons and tests.
rnd.seed(42)
## randint(1, 6) picks a whole number from 1 to 6 inclusive.
print("Dice roll:", rnd.randint(1, 6))
## choice() picks one item from a list.
print("Random choice:", rnd.choice(["rock", "paper", "scissors"]))
## A list to shuffle.
cards = ["A", "K", "Q", "J"]
## shuffle() mixes the list in place.
rnd.shuffle(cards)
## Show the new order.
print("Shuffled cards:", cards)
## sample() picks several different items without repeats.
print("Lottery numbers:", sorted(rnd.sample(range(1, 50), 6)))

# --- 4. datetime -----------------------------------------------------------------------------------
## date(year, month, day) builds a date.
new_year = date(2027, 1, 1)
## Another date.
start = date(2026, 10, 12)
## Subtracting dates gives a timedelta; .days is the number of days.
print("Days from", start, "to New Year:", (new_year - start).days)
## Adding a timedelta moves a date forward.
print("One week after start:", start + timedelta(weeks=1))
## strftime() formats a date; %A is the weekday name.
print("Start was a", start.strftime("%A"))
## %d/%m/%Y gives day/month/year.
print("As DD/MM/YYYY:", start.strftime("%d/%m/%Y"))

# --- 5. collections -----------------------------------------------------------------------------------
## Counter counts things for you (compare with the manual loop in Unit 9).
letters = Counter("mississippi")
## dict() shows the counts as a normal dictionary.
print("Letter counts:", dict(letters))
## most_common(2) gives the two most frequent items.
print("Two most common:", letters.most_common(2))
## defaultdict(list) creates an empty list for any missing key automatically.
groups = defaultdict(list)
## Visit each word.
for word in ["apple", "avocado", "banana", "blueberry", "cherry"]:
    ## word[0] is the first letter; no need to check if the key exists.
    groups[word[0]].append(word)
## Show the groups.
print("Grouped by first letter:", dict(groups))

# --- 6. statistics -----------------------------------------------------------------------------------
## Some daily temperatures.
temps = [31, 33, 29, 35, 33, 30, 32]
## mean() is the average.
print("Mean:", round(statistics.mean(temps), 2))
## median() is the middle value after sorting.
print("Median:", statistics.median(temps))
## mode() is the most common value.
print("Mode:", statistics.mode(temps))

# --- 7. json: save and load structured data as text -----------------------------------------------------
## A Python dictionary with a list inside.
profile = {"name": "Ploy", "skills": ["python", "maths"], "level": 3}
## dumps() ("dump string") turns it into JSON text; indent=2 makes it readable.
as_text = json.dumps(profile, indent=2)
## Show the JSON text.
print("As JSON text:\n" + as_text)
## loads() ("load string") turns JSON text back into Python objects.
loaded = json.loads(as_text)
## It is a normal dictionary again.
print("Loaded back, skills:", loaded["skills"])

# --- 8. Exploring a module -----------------------------------------------------------------------------
## dir() lists the names in a module; skip the internal ones starting with _.
public_names = [name for name in dir(math) if not name.startswith("_")]
## Show the first eight.
print("Some names in math:", public_names[:8])
## help(math.sqrt) would print documentation — try it in the Python shell.


# --- 9. Your own modules and the __name__ check --------------------------------------------------------
## Any .py file can be imported. If helpers.py defines shout(), another file in
## the same folder can write: from helpers import shout
##
## When a file is run directly, Python sets __name__ to "__main__". When it is
## imported, __name__ is the module's name. This lets one file be both.
def main():
    ## Only runs when this file is the program being run.
    print("This unit was run directly, so main() ran.")


## True only when this file was run directly (not imported).
if __name__ == "__main__":
    ## Start the program.
    main()

# --- 10. Third-party packages ----------------------------------------------------------------------------
# Thousands more packages live on PyPI (https://pypi.org). Install one with:
#     python3 -m pip install requests
# Tip: create a virtual environment first so each project has its own packages:
#     python3 -m venv .venv
#     source .venv/bin/activate        (Windows: .venv\Scripts\activate)
# Units 16-19 use numpy, matplotlib and scikit-learn installed this way.

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Use random to simulate 1000 coin flips and count heads with Counter.
#   2. Calculate how many days old you are using date.today().
#   3. Write your own module mytools.py with a function, then import it here.
#   4. Save a dict to a .json file with json.dump() and load it again.
# ---------------------------------------------------------------------------
