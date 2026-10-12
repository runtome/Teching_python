#!/usr/bin/env python3
# Unit 3: Use arithmetic/comparison operators and read a value from the user.
#
# Big idea: operators combine values to make new values. input() lets the
# person running the program supply a value, which always arrives as text.

# --- 1. Arithmetic operators ---------------------------------------------------
# Arithmetic operators calculate with numbers.
first_number = 8
second_number = 3
print("Sum:", first_number + second_number)                 # 11
print("Difference:", first_number - second_number)          # 5
print("Product:", first_number * second_number)             # 24
print("Division:", first_number / second_number)            # 2.666...
print("Integer division:", first_number // second_number)   # 2 (rounds down)
print("Remainder:", first_number % second_number)           # 2
print("Power:", first_number ** 2)                          # 64

# % is handy for checking even/odd: an even number has remainder 0 when / 2.
print("Is 8 even?", first_number % 2 == 0)

# Order of operations follows maths rules: ** first, then * / // %, then + -.
# Use brackets to make your intention clear.
print("2 + 3 * 4 =", 2 + 3 * 4)        # 14
print("(2 + 3) * 4 =", (2 + 3) * 4)    # 20

# --- 2. Comparison operators ---------------------------------------------------
# Comparison operators produce True or False.
print("Is the first number larger?", first_number > second_number)
print("Equal?", first_number == second_number)        # == compares, = assigns
print("Not equal?", first_number != second_number)
print("At most 8?", first_number <= 8)

# Python allows chained comparisons, which read like maths.
age = 15
print("Is age a teenager?", 13 <= age <= 19)

# --- 3. Logical operators --------------------------------------------------------
# and: both must be True | or: at least one True | not: flips True/False
is_weekend = True
is_raining = False
print("Go to the park?", is_weekend and not is_raining)
print("Stay home?", not is_weekend or is_raining)

# --- 4. Reading input ------------------------------------------------------------
# input() clearly prompts the learner; EOFError gives a safe default in
# non-interactive runs where no keyboard input is available.
try:
    favorite_color = input("Type a favorite color (press Enter for none): ").strip()
except EOFError:
    favorite_color = ""

# The default also makes an empty response useful and predictable.
if not favorite_color:
    favorite_color = "blue"
print("Your example color is", favorite_color + ".")

# input() always returns a string. To do maths, convert it with int() or
# float(). A small helper function (see Unit 6) keeps this runnable without
# a keyboard.
def ask_number(prompt, default):
    """Ask for a whole number; fall back to default for empty or bad input."""
    try:
        reply = input(prompt).strip()
    except EOFError:
        reply = ""
    return int(reply) if reply.isdigit() else default


birth_year = ask_number("What year were you born? (Enter for 2010): ", 2010)
current_year = 2026
print("This year you turn", current_year - birth_year)

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Ask for two numbers and print their sum, product and average.
#   2. Use % to print whether a number typed by the user is even or odd.
#   3. Convert a temperature in Celsius to Fahrenheit: F = C * 9 / 5 + 32.
#   4. What is 17 // 5 and 17 % 5? How do they relate to 17 / 5?
# ---------------------------------------------------------------------------
