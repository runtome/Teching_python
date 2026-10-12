#!/usr/bin/env python3
# Unit 1: Start with Python and display information with print().
#
# Big idea: a Python program is a list of instructions that run from the top
# of the file to the bottom, one line at a time. print() is the simplest way
# to see what a program is doing.
#
# How to read these lessons: every line of code has a "##" comment directly
# above it that explains what that line does.

# --- 1. Printing text ---------------------------------------------------------
## print() sends readable text to the screen. Text in quotes is a "string".
print("Hello, Python learner!")
## Single quotes make a string too; choose one style and stay consistent.
print('Single quotes work too.')

# --- 2. Printing several values -----------------------------------------------
## Commas separate values; print() puts one space between each value.
print("A small step today", "makes a strong habit tomorrow.")
## sep= sets the text placed between values (here a dash instead of a space).
print("2026", "10", "12", sep="-")
## end= sets what is printed last; "" means "do not start a new line".
print("This line ends with ... ", end="")
## Because the previous print had end="", this text continues the same line.
print("and this text continues on the same line.")

# --- 3. Printing the result of a calculation ---------------------------------
## Python calculates 2 + 3 first, then prints the label and the answer 5.
print("2 + 3 =", 2 + 3)
## / always gives a decimal number (a "float"), so 10 / 4 is 2.5.
print("10 / 4 =", 10 / 4)
## ** means "to the power of": 2 ** 5 is 2 * 2 * 2 * 2 * 2 = 32.
print("2 ** 5 =", 2 ** 5)
## Inside quotes is just text, so this prints the characters 7 * 6.
print("7 * 6")
## Outside quotes Python calculates, so this prints 42.
print(7 * 6)
## Numbers and text can be mixed with commas; Python converts them for you.
print("There are", 60 * 24, "minutes in one day.")

# --- 4. Special characters ----------------------------------------------------
## \n is an "escape sequence" meaning new line, so this prints two lines.
print("Line one\nLine two")
## \t inserts a tab, which is handy for lining text up in columns.
print("Name:\tAda")
## \" puts a double-quote character inside a double-quoted string.
print("She said \"Python is fun!\"")
## Another way: use single quotes outside so double quotes inside are fine.
print('He replied "Me too!"')
## Triple quotes let one string span several lines exactly as typed.
print("""Roses are red,
Python is neat,
print() shows output,
and that's pretty sweet.""")

# --- 5. Repeating and joining text ---------------------------------------------
## * repeats a string: "=" * 30 makes a line of 30 equals signs.
print("=" * 30)
## + joins (concatenates) strings with no space added automatically.
print("Py" + "thon")
## print() with nothing inside prints an empty line, useful for spacing.
print()

# --- 6. Comments --------------------------------------------------------------
## Any text after # is a comment: Python ignores it, but people read it.
## Good comments explain *why* code exists, not only what it does.
print("Comments never appear in the output.")  # this note is ignored too

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Print your name and your favourite food on one line using a comma.
#   2. Print today's date as DD/MM/YYYY using three numbers and sep="/".
#   3. Print a small box shape made of "*" characters using \n.
#   4. Print a line of 40 dashes using string repetition.
# ---------------------------------------------------------------------------
