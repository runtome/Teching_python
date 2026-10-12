#!/usr/bin/env python3
# Unit 8: Store an ordered, changeable group of values in a list.
#
# Big idea: a list keeps items in order and can grow, shrink and change.
# Lists use square brackets [ ] and can hold any type of value.

shopping_list = ["apples", "bread", "tea"]

# --- 1. Adding and reading items ---------------------------------------------------
# append() adds an item; indexing reads an item by its position.
shopping_list.append("rice")
print("First item:", shopping_list[0])
print("Last item:", shopping_list[-1])
print("Number of items:", len(shopping_list))

# insert() puts an item at a chosen position; extend() adds many items.
shopping_list.insert(1, "milk")
shopping_list.extend(["eggs", "soap"])
print("After insert and extend:", shopping_list)

# --- 2. Changing and removing items ------------------------------------------------------
# Unlike strings, lists are mutable: you can change items in place.
shopping_list[0] = "green apples"

shopping_list.remove("soap")          # remove by value (first match)
last = shopping_list.pop()            # remove and return the last item
second = shopping_list.pop(1)         # remove and return item at index 1
print("Popped:", last, "and", second)
print("Now:", shopping_list)

# Use "in" before removing to avoid a ValueError when the item is missing.
if "chocolate" in shopping_list:
    shopping_list.remove("chocolate")
else:
    print("No chocolate to remove.")

# --- 3. Looping ---------------------------------------------------------------------------
# A for loop visits each item in order.
for item in shopping_list:
    print("Buy:", item)

for number, item in enumerate(shopping_list, start=1):
    print(f"{number}. {item}")

# --- 4. Slicing ---------------------------------------------------------------------------
# Slices work just like strings and return a NEW list.
numbers = [10, 20, 30, 40, 50, 60]
print("First three:", numbers[:3])
print("Last two:", numbers[-2:])
print("Reversed copy:", numbers[::-1])

# --- 5. Sorting and useful built-ins -------------------------------------------------------
scores = [72, 95, 58, 88, 95]
print("Highest:", max(scores), "| Lowest:", min(scores), "| Total:", sum(scores))
print("Average:", sum(scores) / len(scores))
print("How many 95s?", scores.count(95))
print("Index of 58:", scores.index(58))

# sorted() returns a new sorted list; .sort() changes the list itself.
print("sorted() copy:", sorted(scores))
print("Original kept:", scores)
scores.sort(reverse=True)
print("After .sort(reverse=True):", scores)

# --- 6. List comprehensions -----------------------------------------------------------------
# List comprehensions build a new list from an existing sequence.
name_lengths = [len(item) for item in shopping_list]
print("Item name lengths:", name_lengths)

# Add an if at the end to filter items.
squares_of_evens = [n * n for n in range(10) if n % 2 == 0]
print("Squares of even numbers:", squares_of_evens)

# The same thing written as a normal loop, for comparison:
squares_loop = []
for n in range(10):
    if n % 2 == 0:
        squares_loop.append(n * n)
print("Same result with a loop:", squares_loop)

# --- 7. Lists inside lists ---------------------------------------------------------------------
# A list of lists can represent a grid or table.
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print("Middle value:", grid[1][1])     # row 1, column 1
for row in grid:
    print(" ".join(str(value) for value in row))

# --- 8. Copying: a common surprise ----------------------------------------------------------------
# Assignment does NOT copy a list; both names point to the same list object.
original = [1, 2, 3]
alias = original
alias.append(4)
print("original after changing alias:", original)   # [1, 2, 3, 4]!

# .copy() (or list(original), or original[:]) makes an independent copy.
independent = original.copy()
independent.append(5)
print("original:", original, "| independent:", independent)

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Make a list of 5 favourite films and print them in alphabetical order.
#   2. Remove every negative number from [3, -1, 4, -5, 9] using a
#      list comprehension.
#   3. Find the second-largest value in a list of numbers.
#   4. Given a 3x3 grid, print the sum of each row.
# ---------------------------------------------------------------------------
