#!/usr/bin/env python3
# Unit 13: Reuse code with import and explore the standard library.
#
# Big idea: a module is a Python file full of useful code. "import" loads it
# so you can use its functions. Python ships with a large "standard library"
# — no installation needed.

# --- 1. Ways to import -----------------------------------------------------------------------
import math                          # use as math.sqrt(...)
import random as rnd                 # give the module a shorter nickname
from datetime import date, timedelta  # import specific names directly
from collections import Counter, defaultdict
import json

# --- 2. math -------------------------------------------------------------------------------------
print("sqrt(81) =", math.sqrt(81))
print("pi =", round(math.pi, 5))
print("ceil(4.1) =", math.ceil(4.1), "| floor(4.9) =", math.floor(4.9))
print("gcd(12, 18) =", math.gcd(12, 18))

# --- 3. random -----------------------------------------------------------------------------------
# seed() makes the "random" results repeatable, which is useful for lessons
# and tests. Remove it to get different results each run.
rnd.seed(42)
print("Dice roll:", rnd.randint(1, 6))
print("Random choice:", rnd.choice(["rock", "paper", "scissors"]))
cards = ["A", "K", "Q", "J"]
rnd.shuffle(cards)
print("Shuffled cards:", cards)

# --- 4. datetime -----------------------------------------------------------------------------------
new_year = date(2027, 1, 1)
start = date(2026, 10, 12)
print("Days from", start, "to New Year:", (new_year - start).days)
print("One week after start:", start + timedelta(weeks=1))
print("Start was a", start.strftime("%A"))   # %A = weekday name

# --- 5. collections -----------------------------------------------------------------------------------
# Counter counts things for you (compare with the manual loop in Unit 9).
letters = Counter("mississippi")
print("Letter counts:", dict(letters))
print("Two most common:", letters.most_common(2))

# defaultdict creates a starting value for missing keys automatically.
groups = defaultdict(list)
for word in ["apple", "avocado", "banana", "blueberry", "cherry"]:
    groups[word[0]].append(word)
print("Grouped by first letter:", dict(groups))

# --- 6. json: save and load structured data as text -----------------------------------------------------
# JSON is a common text format for sending data between programs.
profile = {"name": "Ploy", "skills": ["python", "maths"], "level": 3}
as_text = json.dumps(profile, indent=2)
print("As JSON text:\n" + as_text)
loaded = json.loads(as_text)
print("Loaded back, skills:", loaded["skills"])

# --- 7. Exploring a module -----------------------------------------------------------------------------
# dir() lists names inside a module; help() shows documentation.
print("Some names in math:", [name for name in dir(math) if not name.startswith("_")][:8])
# help(math.sqrt)   # uncomment to read the docs in the terminal

# --- 8. Your own modules and the __name__ check --------------------------------------------------------
# Any .py file can be imported. If you save a file called helpers.py with a
# function shout(), another file in the same folder can do:
#     from helpers import shout
#
# When a file is run directly, Python sets __name__ to "__main__". When it is
# imported, __name__ is the module's name. This check lets a file be both a
# runnable script and an importable module:
def main():
    print("This unit was run directly, so main() ran.")


if __name__ == "__main__":
    main()

# --- 9. Third-party packages ----------------------------------------------------------------------------
# Thousands more packages live on PyPI (https://pypi.org). Install one with:
#     python3 -m pip install requests
# Tip: create a virtual environment first so each project has its own packages:
#     python3 -m venv .venv
#     source .venv/bin/activate        (Windows: .venv\Scripts\activate)

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Use random to simulate 1000 coin flips and count heads with Counter.
#   2. Calculate how many days old you are using date.today().
#   3. Write your own module mytools.py with a function, then import it here.
#   4. Save a dict to a .json file with json.dump() and load it again.
# ---------------------------------------------------------------------------
