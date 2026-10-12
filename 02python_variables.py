#!/usr/bin/env python3
# Unit 2: Give values names and explore common built-in data types.
#
# Big idea: a variable is a name that points to a value. The value has a
# "type" which decides what you can do with it (add it, make it uppercase...).

# --- 1. Creating variables ----------------------------------------------------
# Variables let us reuse values by referring to a descriptive name.
# The = sign means "store the value on the right under the name on the left".
learner_name = "Sam"      # str   (string / text)
lesson_number = 2         # int   (whole number)
is_ready = True           # bool  (True or False)
temperature = 21.5        # float (decimal number)
nothing_yet = None        # NoneType (means "no value")

# type() shows the kind of value stored in each variable.
print("Name:", learner_name, "—", type(learner_name).__name__)
print("Lesson:", lesson_number, "—", type(lesson_number).__name__)
print("Ready:", is_ready, "—", type(is_ready).__name__)
print("Temperature:", temperature, "—", type(temperature).__name__)
print("Nothing yet:", nothing_yet, "—", type(nothing_yet).__name__)

# --- 2. Variables can change --------------------------------------------------
# Assigning again replaces the old value. The name now points to the new one.
lesson_number = lesson_number + 1
print("Next lesson:", lesson_number)

# Shortcut operators update a variable in place.
lesson_number += 1     # same as lesson_number = lesson_number + 1
print("Lesson after that:", lesson_number)

# Several variables can be assigned on one line.
x, y, z = 1, 2, 3
print("x, y, z =", x, y, z)

# Swapping two values needs no temporary variable in Python.
x, y = y, x
print("After swapping, x =", x, "and y =", y)

# --- 3. Converting between types ---------------------------------------------
# Converting a number to text makes it easy to build a sentence.
message = learner_name + " is studying lesson " + str(lesson_number) + "."
print(message)

# int(), float(), str() and bool() convert values to another type.
print("int('42') + 1 =", int("42") + 1)
print("float('3.5') * 2 =", float("3.5") * 2)
print("int(9.99) =", int(9.99), "(int() cuts off the decimal part)")
print("round(9.99) =", round(9.99), "(round() rounds to the nearest whole)")

# bool() treats "empty" values as False and everything else as True.
print("bool(0) =", bool(0), "| bool('') =", bool(""), "| bool('hi') =", bool("hi"))

# --- 4. Common mistake ---------------------------------------------------------
# "5" + 5 fails because Python will not guess whether you want text or maths.
# We catch the error here so the program keeps running (see Unit 10).
try:
    print("5" + 5)
except TypeError as error:
    print("Error:", error)
print("Fixed with int():", int("5") + 5, "| fixed with str():", "5" + str(5))

# --- 5. Naming rules -----------------------------------------------------------
# Names may contain letters, digits and underscores, but cannot start with a
# digit. They are case-sensitive: age and Age are different variables.
# Python style (PEP 8) uses lower_case_with_underscores for variable names.
# Constants (values that should not change) are written in UPPER_CASE.
SECONDS_PER_MINUTE = 60
print("Seconds in 5 minutes:", 5 * SECONDS_PER_MINUTE)

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Create variables for your age and your city, then print a sentence.
#   2. What is type(3 / 1)? Predict first, then check.
#   3. Convert the string "100" to a number and divide it by 8.
#   4. Swap the values of two variables called first and second.
# ---------------------------------------------------------------------------
