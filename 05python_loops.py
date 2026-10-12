#!/usr/bin/env python3
# Unit 5: Repeat work with for loops and while loops.
#
# Big idea: use a for loop when you know what to go through (a range, a list,
# a string). Use a while loop when you repeat *until* something changes.

# --- 1. for loops with range() ------------------------------------------------------
## range(1, 4) produces 1, 2, 3; the stop value 4 is NOT included.
for number in range(1, 4):
    ## The indented line runs once for each number.
    print("Counting with for:", number)

## Print a label; end=" " keeps the next output on the same line.
print("Even numbers:", end=" ")
## range(start, stop, step): start at 0, stop before 11, jump by 2.
for number in range(0, 11, 2):
    ## Print each number followed by a space instead of a new line.
    print(number, end=" ")
## An empty print() finishes the line.
print()

## Another label on the same line pattern.
print("Backwards:", end=" ")
## A negative step counts down: 5, 4, 3, 2, 1.
for number in range(5, 0, -1):
    ## Print each number on the same line.
    print(number, end=" ")
## Finish the line.
print()

# --- 2. Looping over other things ---------------------------------------------------
## A for loop over a string visits each character in turn.
for letter in "Hi!":
    ## Runs three times: H, i, !
    print("Letter:", letter)

## A for loop over a list visits each item (lists are Unit 8).
for fruit in ["mango", "durian", "rambutan"]:
    ## Runs once per fruit.
    print("Fruit:", fruit)

## enumerate() gives a counter AND the item; start=1 counts from 1.
for position, fruit in enumerate(["mango", "durian"], start=1):
    ## Shows "1 -> mango", then "2 -> durian".
    print(position, "->", fruit)

# --- 3. Accumulating a result ------------------------------------------------------------
## Start the running total at zero before the loop.
total = 0
## Visit every number from 1 to 100.
for number in range(1, 101):
    ## Add the current number to the running total.
    total += number
## After the loop finishes, total holds 5050.
print("Sum of 1..100:", total)

## Counting is accumulating 1 each time a condition is True.
multiples_of_7 = 0
## Check every number from 1 to 100.
for number in range(1, 101):
    ## Is the number divisible by 7?
    if number % 7 == 0:
        ## Count it.
        multiples_of_7 += 1
## There are 14 multiples of 7 up to 100.
print("Multiples of 7 up to 100:", multiples_of_7)

# --- 4. while loops ---------------------------------------------------------------------------
## Start value for a countdown.
countdown = 3
## Repeat as long as the condition stays True.
while countdown > 0:
    ## Show the current value.
    print("Countdown:", countdown)
    ## Update the value so the loop eventually ends.
    countdown -= 1
## Runs once, after the loop ends.
print("Go!")

## while suits problems where you do not know the number of repeats.
value = 1000
## Count how many halvings it takes.
halvings = 0
## Keep going while the value is at least 1.
while value >= 1:
    ## Halve the value.
    value /= 2
    ## Count this halving.
    halvings += 1
## Report the answer: 10.
print("1000 can be halved", halvings, "times before dropping below 1.")

# --- 5. break and continue --------------------------------------------------------------------
## Visit 1 to 5.
for number in range(1, 6):
    ## When number is 3...
    if number == 3:
        ## ...continue skips the rest of this round and moves to 4.
        continue
    ## Runs for 1, 2, 4, 5.
    print("Not skipped:", number)

## Search upward through the numbers.
for number in range(1, 100):
    ## Stop at the first number whose square is bigger than 50.
    if number * number > 50:
        ## Show what was found.
        print("First number whose square is over 50:", number)
        ## break leaves the loop immediately.
        break

## A for loop can have an else block.
for number in [3, 5, 7]:
    ## Look for an even number.
    if number % 2 == 0:
        ## Found one.
        print("Found an even number.")
        ## Stop searching (this also skips the else block).
        break
## else runs only if the loop finished WITHOUT break.
else:
    ## No break happened, so there were no even numbers.
    print("No even numbers in the list.")

# --- 6. Nested loops ---------------------------------------------------------------------------
## The outer loop picks a row: 1, 2, 3.
for row in range(1, 4):
    ## Start an empty line of text for this row.
    line = ""
    ## The inner loop runs completely for every row.
    for column in range(1, 4):
        ## :4 pads each number to 4 characters so columns line up.
        line += f"{row * column:4}"
    ## Print the finished row.
    print(line)

## Nested loops can also draw shapes: row 1 has 1 star, row 2 has 2...
for row in range(1, 5):
    ## "*" * row repeats the star row times.
    print("*" * row)

# --- Common mistakes ---------------------------------------------------------------------------
# * Forgetting to update the variable in a while loop -> an infinite loop.
#   (Press Ctrl+C in the terminal to stop a program that never ends.)
# * Expecting range(1, 5) to include 5. It stops *before* the stop value.

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Print the 7 times table from 7 x 1 to 7 x 12.
#   2. Print an upside-down triangle of stars with 5 rows.
#   3. FizzBuzz: for 1..30 print "Fizz" for multiples of 3, "Buzz" for
#      multiples of 5, "FizzBuzz" for both, otherwise the number.
#   4. Use a while loop to find the smallest power of 2 that is over 1000.
# ---------------------------------------------------------------------------
