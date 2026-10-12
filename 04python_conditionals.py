#!/usr/bin/env python3
# Unit 4: Choose what a program does with if, elif, and else.
#
# Big idea: a condition is any expression that is True or False. Python runs
# an indented block only when its condition is True. Indentation (4 spaces)
# is how Python knows which lines belong to the block.

# --- 1. if / elif / else ---------------------------------------------------------
## Change this score to explore the different branches.
score = 82

## Conditions are checked top to bottom; the first True one runs.
if score >= 90:
    ## Runs only for 90 and above.
    grade = "A"
## elif ("else if") is checked only when the conditions above were False.
elif score >= 80:
    ## Runs for 80-89, because 90+ was already caught above.
    grade = "B"
## Another elif for 70-79.
elif score >= 70:
    ## Runs for 70-79.
    grade = "C"
## else runs when no condition above was True.
else:
    ## Anything below 70.
    grade = "Keep practicing"

## Show the score.
print("Score:", score)
## Show which branch was chosen.
print("Result:", grade)

# --- 2. Combining conditions -------------------------------------------------------
## A True/False fact to combine with the score.
has_finished = True
## and: both conditions must be True for the block to run.
if score >= 60 and has_finished:
    ## Runs because 82 >= 60 and has_finished is True.
    print("The learner completed this practice check.")

## A day name to test.
day = "Saturday"
## or: only one side needs to be True.
if day == "Saturday" or day == "Sunday":
    ## Runs for either weekend day.
    print(day, "is a weekend day.")

## "in" checks membership: is day one of the items in this tuple?
if day in ("Saturday", "Sunday"):
    ## Same result, shorter code.
    print("Same answer using 'in'.")

# --- 3. Nested conditions -----------------------------------------------------------
## Values for a weather example.
temperature = 28
## Another value for the same example.
is_sunny = True
## The outer condition is checked first.
if temperature > 25:
    ## The inner if is only reached when it is hot.
    if is_sunny:
        ## Hot and sunny.
        print("Hot and sunny: wear a hat!")
    ## The inner else pairs with the inner if.
    else:
        ## Hot but not sunny.
        print("Hot but cloudy.")
## The outer else pairs with the outer if.
else:
    ## Not hot.
    print("Not too hot today.")

# --- 4. Truthy and falsy values -----------------------------------------------------
## An empty string counts as False in a condition.
username = ""
## "if username" means "if username is not empty".
if username:
    ## Skipped because username is empty.
    print("Welcome,", username)
## Runs because the condition was False.
else:
    ## Explain what happened.
    print("No username entered yet.")

## An empty list is also falsy; a list with items is truthy.
cart = ["tea"]
## The cart has one item, so this is True.
if cart:
    ## len() counts the items.
    print("Cart has", len(cart), "item(s).")

# --- 5. Conditional expression (one-line if) ------------------------------------------
## An age to classify.
age = 17
## Read as: "adult" if age >= 18, otherwise "minor".
status = "adult" if age >= 18 else "minor"
## Shows "minor".
print("Age", age, "is a", status)

# --- 6. A worked example: leap years ----------------------------------------------------
## Check several years with a loop (loops are explained in Unit 5).
for year in (1900, 2000, 2024, 2026):
    ## Divisible by 4, except centuries unless divisible by 400.
    is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    ## Print the answer for each year.
    print(year, "is a leap year" if is_leap else "is not a leap year")

# --- 7. match (Python 3.10+) -------------------------------------------------------------
## The value we want to compare against several patterns.
command = "stop"
## match tries each case from top to bottom.
match command:
    ## Matches exactly "start".
    case "start":
        ## Runs for "start".
        print("Starting the engine.")
    ## | means "or": matches "stop" or "halt".
    case "stop" | "halt":
        ## Runs for "stop" or "halt".
        print("Stopping the engine.")
    ## _ matches anything not matched above (like else).
    case _:
        ## Runs for anything else.
        print("Unknown command.")

# --- Common mistakes ------------------------------------------------------------------------
# * Using = instead of == inside a condition gives a SyntaxError.
# * Forgetting the colon (:) at the end of an if/elif/else line.
# * Mixing tabs and spaces for indentation. Always use 4 spaces.
# * Writing "if day == 'Saturday' or 'Sunday'": the right side is always
#   truthy! Write day == "Saturday" or day == "Sunday" (or use "in").

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Write a program that says whether a number is positive, negative or 0.
#   2. A cinema ticket is free under 5, half price under 12, else full price.
#   3. Ask for a password and print "Strong" if it has 8+ characters,
#      otherwise "Too short".
# ---------------------------------------------------------------------------
