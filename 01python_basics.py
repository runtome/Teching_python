#!/usr/bin/env python3
# Unit 1: Start with Python and display information with print().
#
# Big idea: a Python program is a list of instructions that run from the top
# of the file to the bottom, one line at a time. print() is the simplest way
# to see what a program is doing.

# --- 1. Printing text ---------------------------------------------------------
# print() sends readable text to the screen.
# Text inside quotes is called a "string". Single or double quotes both work.
print("Hello, Python learner!")
print('Single quotes work too.')

# --- 2. Printing several values -----------------------------------------------
# You can print several values together by separating them with commas.
# print() automatically puts one space between each value.
print("A small step today", "makes a strong habit tomorrow.")

# sep= changes the text placed between values; end= changes what comes last.
# By default sep=" " and end="\n" (a new line).
print("2026", "10", "12", sep="-")
print("This line ends with ... ", end="")
print("and this text continues on the same line.")

# --- 3. Printing the result of a calculation ---------------------------------
# Python evaluates simple expressions inside print() before displaying them.
print("2 + 3 =", 2 + 3)
print("10 / 4 =", 10 / 4)      # / always gives a decimal (float) result.
print("2 ** 5 =", 2 ** 5)      # ** means "to the power of".

# Notice the difference: inside quotes is text, outside quotes is calculated.
print("7 * 6")   # prints the characters 7 * 6
print(7 * 6)     # prints 42

# --- 4. Special characters ----------------------------------------------------
# A backslash starts an "escape sequence": \n is a new line, \t is a tab.
print("Line one\nLine two")
print("Name:\tAda")
print("She said \"Python is fun!\"")   # \" puts a quote inside a string.

# Triple quotes let one string span several lines.
print("""Roses are red,
Python is neat,
print() shows output,
and that's pretty sweet.""")

# --- 5. Comments --------------------------------------------------------------
# Any text after a # is a comment. Python ignores it, but people read it.
# Use comments to explain *why* code exists, not to repeat what it does.

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Print your name and your favourite food on one line using a comma.
#   2. Print today's date as DD/MM/YYYY using three numbers and sep="/".
#   3. Print a small box shape made of "*" characters using \n.
#   4. What does print() with nothing inside the brackets do? Try it!
# ---------------------------------------------------------------------------
