#!/usr/bin/env python3
# Unit 9: Compare dictionaries, tuples, and sets for grouped data.
#
# Big idea: choose the collection that matches your data.
#   list  [ ] ordered, changeable, duplicates allowed       (Unit 8)
#   tuple ( ) ordered, NOT changeable, duplicates allowed
#   set   { } unordered, changeable, NO duplicates
#   dict  {k: v} look up a value by a unique key

# --- 1. Dictionaries ---------------------------------------------------------------------
## A dictionary maps unique keys ("title", "pages") to values.
book = {"title": "The Python Book", "pages": 120}
## Read the value for "pages", add 5, and store it back.
book["pages"] += 5
## Look values up by their key.
print(book["title"], "has", book["pages"], "pages.")
## Assigning to a new key adds it to the dictionary.
book["author"] = "A. Coder"
## get() returns a default instead of raising KeyError for a missing key.
print("Year:", book.get("year", "unknown"))

## .items() gives (key, value) pairs; unpack them into two names.
for key, value in book.items():
    ## Print each pair on its own line.
    print(f"  {key}: {value}")

## .keys() gives just the keys; list() turns them into a list.
print("Keys:", list(book.keys()))
## "in" checks the KEYS of a dictionary.
print("Has an author?", "author" in book)
## pop() removes a key and returns its value.
removed_pages = book.pop("pages")
## Show what was removed and what is left.
print("Removed pages value:", removed_pages, "| book is now:", book)
## update() adds or changes several keys at once.
book.update({"year": 2026, "title": "The Python Book, 2nd ed."})
## Shows the updated dictionary.
print("After update:", book)

# --- 2. Counting with a dictionary --------------------------------------------------------------
## Some text whose words we will count.
text = "the cat sat on the mat the end"
## Start with an empty dictionary: word -> count.
word_counts = {}
## Visit each word.
for word in text.split():
    ## get(word, 0) gives the current count (0 if new), then add 1.
    word_counts[word] = word_counts.get(word, 0) + 1
## Shows each word with its count.
print("Word counts:", word_counts)
## max() with key=word_counts.get finds the key with the largest value.
most_common = max(word_counts, key=word_counts.get)
## Shows "the".
print("Most common word:", most_common)

# --- 3. Nested data ---------------------------------------------------------------------------------
## A list of dictionaries, each with a list of scores inside.
students = [
    {"name": "Ana", "scores": [80, 92, 77]},
    {"name": "Ben", "scores": [65, 70, 88]},
]
## Visit each student record.
for student in students:
    ## Average = total of the scores list / number of scores.
    average = sum(student["scores"]) / len(student["scores"])
    ## :.1f shows one decimal place.
    print(f"{student['name']}: average {average:.1f}")

## A dict comprehension builds key: value pairs, here n -> n squared.
squares = {n: n * n for n in range(1, 6)}
## Shows {1: 1, 2: 4, ...}.
print("Squares dict:", squares)

## A dictionary of lists groups related items under one key.
menu = {"drinks": ["tea", "coffee"], "food": ["noodles"]}
## Add an item to the list stored under "food".
menu["food"].append("rice")
## Show each group.
for section, items in menu.items():
    ## join() turns the list into comma-separated text.
    print(f"{section}: {', '.join(items)}")

# --- 4. Tuples ---------------------------------------------------------------------------------------
## A tuple uses round brackets and is usually treated as fixed.
coordinates = (4, 7)
## Show the tuple.
print("Coordinates:", coordinates)
## Unpacking assigns each item to its own variable.
x, y = coordinates
## Shows x = 4 y = 7.
print("x =", x, "y =", y)
## Tuples cannot change, so they can be dictionary keys (lists cannot).
city_at = {(13.75, 100.50): "Bangkok", (51.51, -0.13): "London"}
## Look up a city by its (latitude, longitude) tuple.
print("City at (13.75, 100.50):", city_at[(13.75, 100.50)])
## (5,) with a comma is a tuple; (5) is just the number 5 in brackets.
print(type((5,)).__name__, type((5)).__name__)

# --- 5. Sets -----------------------------------------------------------------------------------------
## A set stores unique values.
topics = {"print", "variables", "loops"}
## Adding a value that is already there changes nothing.
topics.add("loops")
## Sets have no order, so sorted() gives a predictable list to print.
print("Unique topics:", sorted(topics))
## A list with repeated names.
visitors = ["ana", "ben", "ana", "cy", "ben"]
## set() removes the duplicates.
print("Unique visitors:", sorted(set(visitors)))
## Two groups of members.
python_club = {"ana", "ben", "cy"}
## Another group.
art_club = {"ben", "dee"}
## & (intersection) keeps members in BOTH sets.
print("In both clubs:", python_club & art_club)
## | (union) keeps members in EITHER set.
print("In either club:", sorted(python_club | art_club))
## - (difference) keeps members only in the first set.
print("Python club only:", sorted(python_club - art_club))

# --- 6. Choosing the right collection -----------------------------------------------------------------
## A list keeps an ordered history, duplicates allowed.
history = ["login", "view", "view", "logout"]
## A set answers "have we seen this?" quickly.
seen_pages = set(history)
## A dict looks something up by name.
page_titles = {"login": "Sign in", "view": "Article", "logout": "Goodbye"}
## Combine them: titles of the unique pages, in a fixed order.
print("Unique page titles:", sorted(page_titles[p] for p in seen_pages))

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Build a phone book dict, then look up a name that may not exist.
#   2. Count how many times each letter appears in "mississippi".
#   3. Given two lists of friends, print the friends you have in common.
#   4. Store (name, age) tuples in a list and print the oldest person.
# ---------------------------------------------------------------------------
