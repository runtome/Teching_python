#!/usr/bin/env python3
# Unit 14: Process sequences elegantly with built-ins, iterators and generators.
#
# Big idea: Python has many tools that loop for you. Using them makes code
# shorter and easier to read. Generators produce values one at a time, so
# they can handle huge (even endless) sequences without using much memory.

names = ["Ana", "Ben", "Cy"]
scores = [88, 72, 95]

# --- 1. zip(): walk through several lists together ------------------------------------------
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# zip + dict turns two lists into a dictionary.
score_book = dict(zip(names, scores))
print("Score book:", score_book)

# --- 2. any() and all() --------------------------------------------------------------------------
print("Did anyone score over 90?", any(score > 90 for score in scores))
print("Did everyone pass (>= 50)?", all(score >= 50 for score in scores))

# --- 3. sorted() with a key -----------------------------------------------------------------------
# key= tells sorted() what to compare. Here: sort (name, score) pairs by score.
pairs = list(zip(names, scores))
ranking = sorted(pairs, key=lambda pair: pair[1], reverse=True)
print("Ranking:", ranking)

# --- 4. map() and filter() --------------------------------------------------------------------------
# map applies a function to every item; filter keeps items that pass a test.
# Comprehensions often do the same job and are usually considered clearer.
upper_names = list(map(str.upper, names))
high_scores = list(filter(lambda score: score >= 80, scores))
print("map ->", upper_names, "| filter ->", high_scores)
print("comprehension ->", [n.upper() for n in names], [s for s in scores if s >= 80])

# --- 5. Iterators: what a for loop really does ---------------------------------------------------------
# iter() makes an iterator; next() asks it for the next value.
letters = iter("abc")
print(next(letters), next(letters), next(letters))
# One more next(letters) would raise StopIteration — that is how a for loop
# knows when to stop.


# --- 6. Generator functions: yield ----------------------------------------------------------------------
# A function with yield returns a generator. It pauses at each yield and
# continues from there the next time a value is requested.
def countdown(start):
    print("  (generator started)")
    while start > 0:
        yield start
        start -= 1


for value in countdown(3):
    print("  got", value)


# Generators can even be infinite, because values are made only when needed.
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


first_ten = []
for number in fibonacci():
    if len(first_ten) == 10:
        break
    first_ten.append(number)
print("First ten Fibonacci numbers:", first_ten)

# --- 7. Generator expressions ----------------------------------------------------------------------------
# Like a list comprehension but with ( ). Values are produced lazily, so this
# sums a million squares without building a million-item list in memory.
total = sum(n * n for n in range(1_000_000))
print("Sum of the first million squares:", total)

# --- 8. Unpacking with * -----------------------------------------------------------------------------------
first, *middle, last = [1, 2, 3, 4, 5]
print("first:", first, "| middle:", middle, "| last:", last)
print("Unpack a list into print:", *names)

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Use zip to print a table of three lists: names, ages and cities.
#   2. Write a generator even_numbers(limit) that yields 0, 2, 4, ... < limit.
#   3. Use any() to check whether a sentence contains a digit.
#   4. Sort a list of words by their last letter.
# ---------------------------------------------------------------------------
