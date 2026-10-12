#!/usr/bin/env python3
# Unit 9: Compare dictionaries, tuples, and sets for grouped data.
#
# Big idea: choose the collection that matches your data.
#   list  [ ] ordered, changeable, duplicates allowed       (Unit 8)
#   tuple ( ) ordered, NOT changeable, duplicates allowed
#   set   { } unordered, changeable, NO duplicates
#   dict  {k: v} look up a value by a unique key

# --- 1. Dictionaries ---------------------------------------------------------------------
# A dictionary maps unique keys to values.
book = {"title": "The Python Book", "pages": 120}
book["pages"] += 5  # Update the value associated with the pages key.
print(book["title"], "has", book["pages"], "pages.")

# Add a new key simply by assigning to it.
book["author"] = "A. Coder"

# get() returns a default instead of raising KeyError when a key is missing.
print("Year:", book.get("year", "unknown"))

# Loop through keys and values together with .items().
for key, value in book.items():
    print(f"  {key}: {value}")

print("Keys:", list(book.keys()))
print("Has an author?", "author" in book)   # "in" checks keys

# Remove a key with del or pop().
removed_pages = book.pop("pages")
print("Removed pages value:", removed_pages, "| book is now:", book)

# --- 2. Counting with a dictionary --------------------------------------------------------------
# A classic pattern: count how often each word appears.
text = "the cat sat on the mat the end"
word_counts = {}
for word in text.split():
    word_counts[word] = word_counts.get(word, 0) + 1
print("Word counts:", word_counts)

# Find the most common word: max() with a key function.
most_common = max(word_counts, key=word_counts.get)
print("Most common word:", most_common)

# --- 3. Nested data ---------------------------------------------------------------------------------
# Dictionaries and lists combine to describe real-world records.
students = [
    {"name": "Ana", "scores": [80, 92, 77]},
    {"name": "Ben", "scores": [65, 70, 88]},
]
for student in students:
    average = sum(student["scores"]) / len(student["scores"])
    print(f"{student['name']}: average {average:.1f}")

# Dictionary comprehension, like a list comprehension but with key: value.
squares = {n: n * n for n in range(1, 6)}
print("Squares dict:", squares)

# --- 4. Tuples ---------------------------------------------------------------------------------------
# A tuple is an ordered group that is usually treated as fixed.
coordinates = (4, 7)
print("Coordinates:", coordinates)

# Unpacking assigns each item to its own variable.
x, y = coordinates
print("x =", x, "y =", y)

# Tuples cannot be changed: coordinates[0] = 5 would raise a TypeError.
# Because they are fixed, tuples can be used as dictionary keys.
city_at = {(13.75, 100.50): "Bangkok", (51.51, -0.13): "London"}
print("City at (13.75, 100.50):", city_at[(13.75, 100.50)])

# A one-item tuple needs a trailing comma: (5,) is a tuple, (5) is just 5.
print(type((5,)).__name__, type((5)).__name__)

# --- 5. Sets -----------------------------------------------------------------------------------------
# A set stores unique values, so adding an existing value changes nothing.
topics = {"print", "variables", "loops"}
topics.add("loops")
print("Unique topics:", sorted(topics))

# Remove duplicates from a list by turning it into a set.
visitors = ["ana", "ben", "ana", "cy", "ben"]
print("Unique visitors:", sorted(set(visitors)))

# Set maths compares groups quickly.
python_club = {"ana", "ben", "cy"}
art_club = {"ben", "dee"}
print("In both clubs:", python_club & art_club)          # intersection
print("In either club:", sorted(python_club | art_club))  # union
print("Python club only:", sorted(python_club - art_club))  # difference

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Build a phone book dict, then look up a name that may not exist.
#   2. Count how many times each letter appears in "mississippi".
#   3. Given two lists of friends, print the friends you have in common.
#   4. Store (name, age) tuples in a list and print the oldest person.
# ---------------------------------------------------------------------------
