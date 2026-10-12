#!/usr/bin/env python3
# Unit 3: Use arithmetic/comparison operators and read a value from the user.
#
# Big idea: operators combine values to make new values. input() lets the
# person running the program supply a value, which always arrives as text.

# --- 1. Arithmetic operators ---------------------------------------------------
## Store two numbers to calculate with.
first_number = 8
## The second number.
second_number = 3
## + adds: 8 + 3 = 11.
print("Sum:", first_number + second_number)
## - subtracts: 8 - 3 = 5.
print("Difference:", first_number - second_number)
## * multiplies: 8 * 3 = 24.
print("Product:", first_number * second_number)
## / divides and always gives a float: 2.666...
print("Division:", first_number / second_number)
## // divides and rounds DOWN to a whole number: 2.
print("Integer division:", first_number // second_number)
## % gives the remainder after dividing: 8 = 3 * 2 + 2, so 2.
print("Remainder:", first_number % second_number)
## ** raises to a power: 8 squared is 64.
print("Power:", first_number ** 2)
## abs() removes a minus sign: the distance from zero.
print("abs(-7) =", abs(-7))

## An even number has remainder 0 when divided by 2, so this is True.
print("Is 8 even?", first_number % 2 == 0)
## Order of operations: * happens before +, so this is 2 + 12 = 14.
print("2 + 3 * 4 =", 2 + 3 * 4)
## Brackets happen first, so this is 5 * 4 = 20.
print("(2 + 3) * 4 =", (2 + 3) * 4)

## Practical example: split a bill. 1250 baht shared by 4 people.
bill, people = 1250, 4
## // gives the whole baht each person pays, % gives the leftover baht.
print("Each pays", bill // people, "baht, leftover", bill % people, "baht")

# --- 2. Comparison operators ---------------------------------------------------
## > asks "is the left bigger?" and gives True or False.
print("Is the first number larger?", first_number > second_number)
## == compares for equality (one = assigns, two == compares).
print("Equal?", first_number == second_number)
## != means "not equal".
print("Not equal?", first_number != second_number)
## <= means "less than or equal to".
print("At most 8?", first_number <= 8)
## Store an age to test.
age = 15
## Chained comparisons read like maths: is 13 <= age AND age <= 19?
print("Is age a teenager?", 13 <= age <= 19)
## Strings compare alphabetically: "apple" comes before "banana".
print("'apple' < 'banana'?", "apple" < "banana")

# --- 3. Logical operators --------------------------------------------------------
## A True/False fact.
is_weekend = True
## Another True/False fact.
is_raining = False
## and: both sides must be True. not flips False into True.
print("Go to the park?", is_weekend and not is_raining)
## or: at least one side must be True.
print("Stay home?", not is_weekend or is_raining)

# --- 4. Reading input ------------------------------------------------------------
## try lets us handle the case where there is no keyboard (EOFError).
try:
    ## input() shows the prompt and waits; .strip() removes extra spaces.
    favorite_color = input("Type a favorite color (press Enter for none): ").strip()
## EOFError happens when the program runs without a keyboard attached.
except EOFError:
    ## Use an empty string so the next step can choose a default.
    favorite_color = ""

## An empty string counts as False, so "not favorite_color" is True when empty.
if not favorite_color:
    ## Pick a predictable default value.
    favorite_color = "blue"
## Show the result.
print("Your example color is", favorite_color + ".")


## input() always returns a string. This helper function (see Unit 6) turns
## the reply into a whole number, or uses a default for empty or bad input.
def ask_number(prompt, default):
    """Ask for a whole number; fall back to default for empty or bad input."""
    ## Try to read a reply from the keyboard.
    try:
        ## Read and clean the reply.
        reply = input(prompt).strip()
    ## No keyboard available.
    except EOFError:
        ## Treat it like an empty reply.
        reply = ""
    ## isdigit() is True only for text made of digits like "2010".
    return int(reply) if reply.isdigit() else default


## Ask for a birth year, defaulting to 2010.
birth_year = ask_number("What year were you born? (Enter for 2010): ", 2010)
## A fixed current year keeps the lesson's output predictable.
current_year = 2026
## Subtraction gives the age reached this year.
print("This year you turn", current_year - birth_year)

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Ask for two numbers and print their sum, product and average.
#   2. Use % to print whether a number typed by the user is even or odd.
#   3. Convert a temperature in Celsius to Fahrenheit: F = C * 9 / 5 + 32.
#   4. What is 17 // 5 and 17 % 5? How do they relate to 17 / 5?
# ---------------------------------------------------------------------------
