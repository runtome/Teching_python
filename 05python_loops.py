#!/usr/bin/env python3
# Unit 5: Repeat work with for loops and while loops.
#
# Big idea: use a for loop when you know what to go through (a range, a list,
# a string). Use a while loop when you repeat *until* something changes.

# --- 1. for loops with range() ------------------------------------------------------
# range(1, 4) produces 1, 2, and 3; the stop value is not included.
for number in range(1, 4):
    print("Counting with for:", number)

# range(start, stop, step) can skip values or count backwards.
print("Even numbers:", end=" ")
for number in range(0, 11, 2):
    print(number, end=" ")
print()  # finish the line

print("Backwards:", end=" ")
for number in range(5, 0, -1):
    print(number, end=" ")
print()

# --- 2. Looping over other things ---------------------------------------------------
# A for loop can visit each character of a string...
for letter in "Hi!":
    print("Letter:", letter)

# ...or each item of a list (more in Unit 8).
for fruit in ["mango", "durian", "rambutan"]:
    print("Fruit:", fruit)

# enumerate() gives both the position and the item.
for position, fruit in enumerate(["mango", "durian"], start=1):
    print(position, "->", fruit)

# --- 3. Accumulating a result ------------------------------------------------------------
# A common pattern: start with an empty "total" and add to it each time round.
total = 0
for number in range(1, 101):
    total += number
print("Sum of 1..100:", total)

# --- 4. while loops ---------------------------------------------------------------------------
# A while loop repeats as long as its condition stays true.
countdown = 3
while countdown > 0:
    print("Countdown:", countdown)
    countdown -= 1  # Update the value so the loop eventually ends.
print("Go!")

# while is ideal when you don't know how many repeats you need.
# How many times can 1000 be halved before it is below 1?
value = 1000
halvings = 0
while value >= 1:
    value /= 2
    halvings += 1
print("1000 can be halved", halvings, "times before dropping below 1.")

# --- 5. break and continue --------------------------------------------------------------------
# continue skips just the current iteration.
for number in range(1, 6):
    if number == 3:
        continue
    print("Not skipped:", number)

# break leaves the loop immediately.
for number in range(1, 100):
    if number * number > 50:
        print("First number whose square is over 50:", number)
        break

# A for loop's else block runs only if the loop was NOT stopped by break.
for number in [3, 5, 7]:
    if number % 2 == 0:
        print("Found an even number.")
        break
else:
    print("No even numbers in the list.")

# --- 6. Nested loops ---------------------------------------------------------------------------
# A loop inside a loop: the inner loop runs completely for each outer step.
for row in range(1, 4):
    line = ""
    for column in range(1, 4):
        line += f"{row * column:4}"   # :4 pads each number to 4 characters
    print(line)

# --- Common mistakes ---------------------------------------------------------------------------
# * Forgetting to update the variable in a while loop -> an infinite loop.
#   (Press Ctrl+C in the terminal to stop a program that never ends.)
# * Expecting range(1, 5) to include 5. It stops *before* the stop value.

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Print the 7 times table from 7 x 1 to 7 x 12.
#   2. Print a triangle of stars: *, **, ***, ... up to 5 rows.
#   3. FizzBuzz: for 1..30 print "Fizz" for multiples of 3, "Buzz" for
#      multiples of 5, "FizzBuzz" for both, otherwise the number.
#   4. Use a while loop to find the smallest power of 2 that is over 1000.
# ---------------------------------------------------------------------------
