#!/usr/bin/env python3
# Unit 6: Package reusable steps in functions.
#
# Big idea: a function is a named, reusable block of code. Define it once with
# def, then call it as many times as you like. Good functions do one job.


# --- 1. Parameters and return values ------------------------------------------------
## def creates a function named greet with one parameter called name.
def greet(name):
    """Return a friendly greeting for one learner."""
    ## return sends the finished text back to whoever called the function.
    return f"Hello, {name}! Welcome to Python."


## height=1 is a default: it is used when the caller leaves height out.
def rectangle_area(width, height=1):
    """Calculate the area of a rectangle."""
    ## Multiply the two sides and hand the answer back.
    return width * height


## Call greet with "Riley"; the returned text is printed.
print(greet("Riley"))
## Both arguments given: 4 * 3 = 12.
print("Area:", rectangle_area(4, 3))
## height left out, so the default 1 is used: 4 * 1 = 4.
print("Area of a 4 by 1 rectangle:", rectangle_area(4))
## Keyword arguments name each parameter, so the order no longer matters.
print("Area with keywords:", rectangle_area(height=5, width=2))


# --- 2. return vs print ---------------------------------------------------------------
## This function only prints; it does not return anything.
def square_and_print(number):
    ## Show the square on screen. The function then returns None by itself.
    print("Square is", number * number)


## This function returns the square so other code can use it.
def square(number):
    ## Hand the value back.
    return number * number


## The call prints "Square is 9", but result_a receives None.
result_a = square_and_print(3)
## result_b receives the number 9.
result_b = square(3)
## None: there was nothing returned.
print("Value from square_and_print:", result_a)
## Because square returned 9, we can keep calculating: 9 + 1 = 10.
print("Value from square, plus one:", result_b + 1)


# --- 3. Returning several values ------------------------------------------------------------
## A function can return several values separated by commas (a tuple, Unit 9).
def min_max_average(numbers):
    """Return the smallest, largest and average of a list of numbers."""
    ## min(), max(), sum() and len() are built-in helper functions.
    return min(numbers), max(numbers), sum(numbers) / len(numbers)


## Unpack the three returned values into three variables.
low, high, average = min_max_average([4, 9, 1, 7])
## :.2f shows the average with two decimal places.
print(f"low={low}, high={high}, average={average:.2f}")


# --- 4. Scope: where variables live ---------------------------------------------------------
## A "global" variable defined at the top level of the file.
bonus = 10


## Variables created inside a function are "local" and vanish when it ends.
def add_bonus(points):
    ## Functions can READ global variables such as bonus.
    total = points + bonus
    ## total is local; return gives its value to the caller.
    return total


## Shows 15. Writing print(total) out here would fail with a NameError.
print("Points with bonus:", add_bonus(5))


# --- 5. Flexible arguments: *args and **kwargs ----------------------------------------------
## *numbers collects ANY number of positional arguments into a tuple.
def add_all(*numbers):
    ## Start a running total.
    total = 0
    ## Visit every number that was passed in.
    for number in numbers:
        ## Add it to the total.
        total += number
    ## Give back the result.
    return total


## Four arguments are collected into (1, 2, 3, 4) and added up.
print("add_all(1, 2, 3, 4) =", add_all(1, 2, 3, 4))


## **details collects named arguments into a dictionary.
def describe_pet(**details):
    ## .items() gives each key and value pair.
    for key, value in details.items():
        ## Print one detail per line.
        print(f"  {key}: {value}")


## A heading for the output below.
print("Pet details:")
## Each name=value pair becomes a dictionary entry.
describe_pet(name="Mochi", species="cat", age=3)


# --- 6. Functions calling functions --------------------------------------------------------
## A small function that does one conversion.
def celsius_to_fahrenheit(celsius):
    ## The standard conversion formula.
    return celsius * 9 / 5 + 32


## A bigger function built from the smaller one.
def weather_report(city, celsius):
    ## Reuse the converter instead of repeating the formula.
    fahrenheit = celsius_to_fahrenheit(celsius)
    ## :.1f shows one decimal place.
    return f"{city}: {celsius}°C ({fahrenheit:.1f}°F)"


## Shows "Bangkok: 33°C (91.4°F)".
print(weather_report("Bangkok", 33))


# --- 7. Validating input inside a function -----------------------------------------------
## Functions are a good place to check that inputs make sense.
def bmi(weight_kg, height_m):
    """Return body mass index, or None if the height is not sensible."""
    ## Guard clause: leave early when the input is unusable.
    if height_m <= 0:
        ## None tells the caller "no answer".
        return None
    ## BMI = weight divided by height squared, rounded to 1 decimal place.
    return round(weight_kg / height_m ** 2, 1)


## A normal call.
print("BMI for 60 kg, 1.70 m:", bmi(60, 1.70))
## A bad height returns None instead of crashing with ZeroDivisionError.
print("BMI with height 0:", bmi(60, 0))


# --- 8. Recursion: a function that calls itself ------------------------------------------------
## Every recursive function needs a "base case" that stops the recursion.
def factorial(n):
    """Return n! = n * (n-1) * ... * 1."""
    ## Base case: 1! and 0! are 1, so stop here.
    if n <= 1:
        ## No further calls.
        return 1
    ## Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)


## 5 * 4 * 3 * 2 * 1 = 120.
print("5! =", factorial(5))


# --- 9. lambda: tiny unnamed functions ---------------------------------------------------------
## Some words to sort.
words = ["banana", "kiwi", "apple"]
## key= tells sorted() what to compare; the lambda returns each word's length.
print("Sorted by length:", sorted(words, key=lambda word: len(word)))
## A lambda can be stored in a variable, although def is usually clearer.
double = lambda n: n * 2
## Shows 14.
print("double(7) =", double(7))

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Write is_even(n) that returns True or False.
#   2. Write circle_area(radius) using 3.14159 * radius ** 2.
#   3. Write count_vowels(text) that returns how many vowels are in text.
#   4. Write a recursive function that returns the sum of 1..n.
# ---------------------------------------------------------------------------
