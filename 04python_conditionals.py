#!/usr/bin/env python3
# Unit 4: Choose what a program does with if, elif, and else.
#
# Big idea: a condition is any expression that is True or False. Python runs
# an indented block only when its condition is True. Indentation (4 spaces)
# is how Python knows which lines belong to the block.

# --- 1. if / elif / else ---------------------------------------------------------
# Change this score to explore the different branches.
score = 82

# Python checks conditions from top to bottom and runs the first match.
# Once a branch runs, the rest are skipped — so order matters!
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "Keep practicing"

print("Score:", score)
print("Result:", grade)

# --- 2. Combining conditions -------------------------------------------------------
# Combine conditions with and; both sides must be true.
has_finished = True
if score >= 60 and has_finished:
    print("The learner completed this practice check.")

# or needs only one side to be true.
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print(day, "is a weekend day.")

# "in" is a neat shortcut for checking against several options.
if day in ("Saturday", "Sunday"):
    print("Same answer using 'in'.")

# --- 3. Nested conditions -----------------------------------------------------------
# An if can sit inside another if. Keep nesting shallow so code stays readable.
temperature = 28
is_sunny = True
if temperature > 25:
    if is_sunny:
        print("Hot and sunny: wear a hat!")
    else:
        print("Hot but cloudy.")
else:
    print("Not too hot today.")

# --- 4. Truthy and falsy values -----------------------------------------------------
# Empty values (0, "", [], None) count as False; everything else counts as True.
username = ""
if username:
    print("Welcome,", username)
else:
    print("No username entered yet.")

# --- 5. Conditional expression (one-line if) ------------------------------------------
# value_if_true if condition else value_if_false
age = 17
status = "adult" if age >= 18 else "minor"
print("Age", age, "is a", status)

# --- 6. match (Python 3.10+) -------------------------------------------------------------
# match compares one value against several patterns. _ matches anything else.
command = "stop"
match command:
    case "start":
        print("Starting the engine.")
    case "stop" | "halt":
        print("Stopping the engine.")
    case _:
        print("Unknown command.")

# --- Common mistakes ------------------------------------------------------------------------
# * Using = instead of == inside a condition gives a SyntaxError.
# * Forgetting the colon (:) at the end of an if/elif/else line.
# * Mixing tabs and spaces for indentation. Always use 4 spaces.

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Write a program that says whether a number is positive, negative or 0.
#   2. A cinema ticket is free under 5, half price under 12, else full price.
#   3. Leap year: divisible by 4, except centuries unless divisible by 400.
#      (2000 -> leap, 1900 -> not leap, 2024 -> leap)
# ---------------------------------------------------------------------------
