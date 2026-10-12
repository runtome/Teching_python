#!/usr/bin/env python3
# Unit 5: Repeat work with for loops and while loops.

# range(1, 4) produces 1, 2, and 3; the stop value is not included.
for number in range(1, 4):
    print("Counting with for:", number)

# A while loop repeats as long as its condition stays true.
countdown = 3
while countdown > 0:
    print("Countdown:", countdown)
    countdown -= 1  # Update the value so the loop eventually ends.
print("Go!")

# continue skips just the current iteration.
for number in range(1, 6):
    if number == 3:
        continue
    print("Not skipped:", number)
