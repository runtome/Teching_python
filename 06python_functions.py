#!/usr/bin/env python3
# Unit 6: Package reusable steps in functions.
#
# Big idea: a function is a named, reusable block of code. Define it once with
# def, then call it as many times as you like. Good functions do one job.


# --- 1. Parameters and return values ------------------------------------------------
# Parameters receive information, and return sends a result back to the caller.
def greet(name):
    """Return a friendly greeting for one learner."""
    return f"Hello, {name}! Welcome to Python."


# A default parameter is used when the caller leaves that argument out.
def rectangle_area(width, height=1):
    """Calculate the area of a rectangle."""
    return width * height


print(greet("Riley"))
print("Area:", rectangle_area(4, 3))
print("Area of a 4 by 1 rectangle:", rectangle_area(4))

# Keyword arguments name the parameter, so order no longer matters.
print("Area with keywords:", rectangle_area(height=5, width=2))


# --- 2. return vs print ---------------------------------------------------------------
# print() only shows a value. return hands the value back so code can use it.
def square_and_print(number):
    print("Square is", number * number)   # returns None automatically


def square(number):
    return number * number


result_a = square_and_print(3)
result_b = square(3)
print("Value from square_and_print:", result_a)   # None
print("Value from square, plus one:", result_b + 1)


# --- 3. Returning several values ------------------------------------------------------------
# Separate values with commas; Python packs them into a tuple (see Unit 9).
def min_max_average(numbers):
    """Return the smallest, largest and average of a list of numbers."""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)


low, high, average = min_max_average([4, 9, 1, 7])
print(f"low={low}, high={high}, average={average:.2f}")


# --- 4. Scope: where variables live ---------------------------------------------------------
# Variables created inside a function are "local": they vanish when it ends.
bonus = 10   # a "global" variable defined at the top level


def add_bonus(points):
    total = points + bonus   # functions can READ global variables
    return total


print("Points with bonus:", add_bonus(5))
# print(total)  # would fail: NameError, total only exists inside add_bonus


# --- 5. Flexible arguments: *args and **kwargs ----------------------------------------------
# *args collects any number of positional arguments into a tuple.
def add_all(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print("add_all(1, 2, 3, 4) =", add_all(1, 2, 3, 4))


# **kwargs collects named arguments into a dictionary.
def describe_pet(**details):
    for key, value in details.items():
        print(f"  {key}: {value}")


print("Pet details:")
describe_pet(name="Mochi", species="cat", age=3)


# --- 6. Functions calling functions --------------------------------------------------------
# Small functions can be combined to build bigger behaviour.
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def weather_report(city, celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)
    return f"{city}: {celsius}°C ({fahrenheit:.1f}°F)"


print(weather_report("Bangkok", 33))


# --- 7. Recursion: a function that calls itself ------------------------------------------------
# Every recursive function needs a "base case" that stops the recursion.
def factorial(n):
    """Return n! = n * (n-1) * ... * 1."""
    if n <= 1:          # base case
        return 1
    return n * factorial(n - 1)


print("5! =", factorial(5))


# --- 8. lambda: tiny unnamed functions ---------------------------------------------------------
# Useful for short one-off functions, e.g. as a sort key.
words = ["banana", "kiwi", "apple"]
print("Sorted by length:", sorted(words, key=lambda word: len(word)))

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Write is_even(n) that returns True or False.
#   2. Write circle_area(radius) using 3.14159 * radius ** 2.
#   3. Write count_vowels(text) that returns how many vowels are in text.
#   4. Write a recursive function that returns the sum of 1..n.
# ---------------------------------------------------------------------------
