#!/usr/bin/env python3
# Unit 4: Choose what a program does with if, elif, and else.

# Change this score to explore the different branches.
score = 82

# Python checks conditions from top to bottom and runs the first match.
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "Keep practicing"

print("Score:", score)
print("Result:", grade)

# Combine conditions with and; both sides must be true.
has_finished = True
if score >= 60 and has_finished:
    print("The learner completed this practice check.")
