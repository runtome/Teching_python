#!/usr/bin/env python3
# Unit 2: Give values names and explore common built-in data types.
#
# Big idea: a variable is a name that points to a value. The value has a
# "type" which decides what you can do with it (add it, make it uppercase...).

# --- 1. Creating variables ----------------------------------------------------
## = stores the value on the right under the name on the left. This is a str.
learner_name = "Sam"
## A whole number is an int (integer).
lesson_number = 2
## True and False are bool (Boolean) values, used for yes/no facts.
is_ready = True
## A number with a decimal point is a float.
temperature = 21.5
## None means "no value yet"; its type is NoneType.
nothing_yet = None

## type() tells us the kind of value; .__name__ gives just the type's name.
print("Name:", learner_name, "—", type(learner_name).__name__)
## The same check for the int variable.
print("Lesson:", lesson_number, "—", type(lesson_number).__name__)
## The same check for the bool variable.
print("Ready:", is_ready, "—", type(is_ready).__name__)
## The same check for the float variable.
print("Temperature:", temperature, "—", type(temperature).__name__)
## The same check for None.
print("Nothing yet:", nothing_yet, "—", type(nothing_yet).__name__)

# --- 2. Variables can change --------------------------------------------------
## The right side is worked out first (2 + 1), then stored back in the name.
lesson_number = lesson_number + 1
## Shows the new value, 3.
print("Next lesson:", lesson_number)
## += is a shortcut for lesson_number = lesson_number + 1.
lesson_number += 1
## Shows 4.
print("Lesson after that:", lesson_number)
## Other shortcuts exist too: -=, *=, /=. Here we double a score.
score = 5
## score becomes 5 * 2 = 10.
score *= 2
## Shows 10.
print("Doubled score:", score)

## Several variables can be assigned on one line, matched left to right.
x, y, z = 1, 2, 3
## Shows 1 2 3.
print("x, y, z =", x, y, z)
## Swapping two values needs no temporary variable in Python.
x, y = y, x
## Now x is 2 and y is 1.
print("After swapping, x =", x, "and y =", y)

# --- 3. Converting between types ---------------------------------------------
## str() turns the number into text so it can be joined with + to other text.
message = learner_name + " is studying lesson " + str(lesson_number) + "."
## Shows the finished sentence.
print(message)
## int() turns the text "42" into the number 42, so we can add 1.
print("int('42') + 1 =", int("42") + 1)
## float() turns text into a decimal number.
print("float('3.5') * 2 =", float("3.5") * 2)
## int() on a float simply cuts off everything after the decimal point.
print("int(9.99) =", int(9.99), "(int() cuts off the decimal part)")
## round() rounds to the nearest whole number instead.
print("round(9.99) =", round(9.99), "(round() rounds to the nearest whole)")
## round(value, 2) keeps two digits after the decimal point.
print("round(3.14159, 2) =", round(3.14159, 2))
## bool() treats "empty" values (0, "") as False and everything else as True.
print("bool(0) =", bool(0), "| bool('') =", bool(""), "| bool('hi') =", bool("hi"))

# --- 4. Common mistake ---------------------------------------------------------
## try lets us run code that might fail without stopping the program (Unit 10).
try:
    ## "5" + 5 fails: Python will not guess whether you want text or maths.
    print("5" + 5)
## except catches the TypeError and stores it in the name "error".
except TypeError as error:
    ## Show the error message Python produced.
    print("Error:", error)
## Fix it by converting one side so both have the same type.
print("Fixed with int():", int("5") + 5, "| fixed with str():", "5" + str(5))

# --- 5. Naming rules -----------------------------------------------------------
## Names use letters, digits and _, cannot start with a digit, and are
## case-sensitive (age and Age differ). UPPER_CASE marks a constant.
SECONDS_PER_MINUTE = 60
## Using a named constant is clearer than a "magic number" like 60.
print("Seconds in 5 minutes:", 5 * SECONDS_PER_MINUTE)
## id() shows the identity of the object a name points to.
same_value = learner_name
## Both names point to the same string object, so the ids are equal.
print("Same object?", id(same_value) == id(learner_name))

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Create variables for your age and your city, then print a sentence.
#   2. What is type(3 / 1)? Predict first, then check.
#   3. Convert the string "100" to a number and divide it by 8.
#   4. Swap the values of two variables called first and second.
# ---------------------------------------------------------------------------
