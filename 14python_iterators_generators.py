#!/usr/bin/env python3
# Unit 14: Process sequences elegantly with built-ins, iterators and generators.
#
# Big idea: Python has many tools that loop for you. Using them makes code
# shorter and easier to read. Generators produce values one at a time, so
# they can handle huge (even endless) sequences without using much memory.

## Two lists that belong together: the first name matches the first score.
names = ["Ana", "Ben", "Cy"]
## Scores in the same order as names.
scores = [88, 72, 95]

# --- 1. zip(): walk through several lists together ------------------------------------------
## zip() pairs item 0 with item 0, item 1 with item 1, and so on.
for name, score in zip(names, scores):
    ## Each round gets one name and its score.
    print(f"{name} scored {score}")
## dict(zip(...)) turns the pairs into a dictionary.
score_book = dict(zip(names, scores))
## Shows {'Ana': 88, ...}.
print("Score book:", score_book)

# --- 2. any() and all() --------------------------------------------------------------------------
## any() is True if at least one item is True.
print("Did anyone score over 90?", any(score > 90 for score in scores))
## all() is True only if every item is True.
print("Did everyone pass (>= 50)?", all(score >= 50 for score in scores))

# --- 3. sorted() with a key -----------------------------------------------------------------------
## list(zip(...)) makes a list of (name, score) tuples.
pairs = list(zip(names, scores))
## key= picks the score (index 1) to compare; reverse=True puts highest first.
ranking = sorted(pairs, key=lambda pair: pair[1], reverse=True)
## Shows the ranking.
print("Ranking:", ranking)

# --- 4. map() and filter() --------------------------------------------------------------------------
## map() applies str.upper to every name.
upper_names = list(map(str.upper, names))
## filter() keeps only scores where the function returns True.
high_scores = list(filter(lambda score: score >= 80, scores))
## Show both results.
print("map ->", upper_names, "| filter ->", high_scores)
## Comprehensions do the same jobs and are often clearer.
print("comprehension ->", [n.upper() for n in names], [s for s in scores if s >= 80])

# --- 5. Iterators: what a for loop really does ---------------------------------------------------------
## iter() makes an iterator: an object that hands out one value at a time.
letters = iter("abc")
## next() asks for the next value: a, then b, then c.
print(next(letters), next(letters), next(letters))
## One more next(letters) would raise StopIteration — that is how a for loop
## knows when to stop.
print("Next with a default:", next(letters, "no more letters"))


# --- 6. Generator functions: yield ----------------------------------------------------------------------
## A function containing yield returns a generator instead of running at once.
def countdown(start):
    ## This line runs only when the first value is requested.
    print("  (generator started)")
    ## Keep producing values while start is above zero.
    while start > 0:
        ## yield hands out a value and PAUSES here until the next request.
        yield start
        ## Execution continues from here on the next request.
        start -= 1


## The for loop keeps asking the generator for values until it finishes.
for value in countdown(3):
    ## Receives 3, 2, 1.
    print("  got", value)


## Generators can be infinite, because values are only made when needed.
def fibonacci():
    ## The first two Fibonacci numbers.
    a, b = 0, 1
    ## Loop forever — safe, because the caller decides when to stop.
    while True:
        ## Hand out the current number.
        yield a
        ## Move along: the next number is the sum of the previous two.
        a, b = b, a + b


## Collect values here.
first_ten = []
## Ask the infinite generator for values.
for number in fibonacci():
    ## Stop once we have ten.
    if len(first_ten) == 10:
        ## Leave the loop (the generator is simply abandoned).
        break
    ## Keep this number.
    first_ten.append(number)
## Shows [0, 1, 1, 2, 3, 5, 8, 13, 21, 34].
print("First ten Fibonacci numbers:", first_ten)

# --- 7. Generator expressions ----------------------------------------------------------------------------
## ( ) instead of [ ] makes values lazily: no million-item list is built.
total = sum(n * n for n in range(1_000_000))
## Underscores in 1_000_000 just make big numbers easier to read.
print("Sum of the first million squares:", total)

# --- 8. Unpacking with * -----------------------------------------------------------------------------------
## *middle collects everything between the first and last items.
first, *middle, last = [1, 2, 3, 4, 5]
## Shows first: 1 | middle: [2, 3, 4] | last: 5.
print("first:", first, "| middle:", middle, "| last:", last)
## *names spreads the list out as separate arguments to print().
print("Unpack a list into print:", *names)

# --- 9. A worked example: reading data in chunks -------------------------------------------------------------
## A generator that groups any sequence into chunks of a given size.
def chunks(items, size):
    ## Step through the positions 0, size, 2*size, ...
    for start in range(0, len(items), size):
        ## Yield one slice at a time.
        yield items[start:start + size]


## Group ten numbers into chunks of four.
for group in chunks(list(range(1, 11)), 4):
    ## Shows [1, 2, 3, 4], [5, 6, 7, 8], [9, 10].
    print("Chunk:", group)

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Use zip to print a table of three lists: names, ages and cities.
#   2. Write a generator even_numbers(limit) that yields 0, 2, 4, ... < limit.
#   3. Use any() to check whether a sentence contains a digit.
#   4. Sort a list of words by their last letter.
# ---------------------------------------------------------------------------
