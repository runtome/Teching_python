#!/usr/bin/env python3
# Unit 8: Store an ordered, changeable group of values in a list.
#
# Big idea: a list keeps items in order and can grow, shrink and change.
# Lists use square brackets [ ] and can hold any type of value.

## Create a list of three strings.
shopping_list = ["apples", "bread", "tea"]

# --- 1. Adding and reading items ---------------------------------------------------
## append() adds one item to the end.
shopping_list.append("rice")
## [0] reads the first item.
print("First item:", shopping_list[0])
## [-1] reads the last item.
print("Last item:", shopping_list[-1])
## len() counts the items.
print("Number of items:", len(shopping_list))
## insert(1, ...) puts "milk" at position 1, pushing the rest along.
shopping_list.insert(1, "milk")
## extend() adds every item from another list.
shopping_list.extend(["eggs", "soap"])
## Show the whole list.
print("After insert and extend:", shopping_list)

# --- 2. Changing and removing items ------------------------------------------------------
## Lists are mutable: assign to an index to replace that item.
shopping_list[0] = "green apples"
## remove() deletes the first item equal to "soap".
shopping_list.remove("soap")
## pop() removes AND returns the last item.
last = shopping_list.pop()
## pop(1) removes and returns the item at index 1.
second = shopping_list.pop(1)
## Show what was removed.
print("Popped:", last, "and", second)
## Show what is left.
print("Now:", shopping_list)

## remove() raises ValueError for a missing item, so check with "in" first.
if "chocolate" in shopping_list:
    ## Only runs if chocolate is there.
    shopping_list.remove("chocolate")
## Otherwise explain.
else:
    ## Runs here because there is no chocolate.
    print("No chocolate to remove.")

# --- 3. Looping ---------------------------------------------------------------------------
## A for loop visits each item in order.
for item in shopping_list:
    ## Runs once per item.
    print("Buy:", item)

## enumerate() adds a counter so we can number the list.
for number, item in enumerate(shopping_list, start=1):
    ## Shows "1. green apples" and so on.
    print(f"{number}. {item}")

# --- 4. Slicing ---------------------------------------------------------------------------
## A list of numbers to slice.
numbers = [10, 20, 30, 40, 50, 60]
## [:3] gives the first three items as a NEW list.
print("First three:", numbers[:3])
## [-2:] gives the last two items.
print("Last two:", numbers[-2:])
## [::-1] gives a reversed copy.
print("Reversed copy:", numbers[::-1])

# --- 5. Sorting and useful built-ins -------------------------------------------------------
## Some test scores.
scores = [72, 95, 58, 88, 95]
## max(), min() and sum() work on lists of numbers.
print("Highest:", max(scores), "| Lowest:", min(scores), "| Total:", sum(scores))
## Average = total divided by how many.
print("Average:", sum(scores) / len(scores))
## count() counts matching items.
print("How many 95s?", scores.count(95))
## index() finds the position of the first match.
print("Index of 58:", scores.index(58))
## sorted() returns a NEW sorted list.
print("sorted() copy:", sorted(scores))
## ...so the original order is kept.
print("Original kept:", scores)
## .sort() changes the list itself; reverse=True sorts largest first.
scores.sort(reverse=True)
## The list is now in descending order.
print("After .sort(reverse=True):", scores)

# --- 6. List comprehensions -----------------------------------------------------------------
## Read as: "len(item) for every item in shopping_list".
name_lengths = [len(item) for item in shopping_list]
## Shows a list of lengths.
print("Item name lengths:", name_lengths)
## The if at the end filters: keep only even n, then square them.
squares_of_evens = [n * n for n in range(10) if n % 2 == 0]
## Shows [0, 4, 16, 36, 64].
print("Squares of even numbers:", squares_of_evens)

## The same thing written as a normal loop, for comparison.
squares_loop = []
## Visit 0..9.
for n in range(10):
    ## Keep only even numbers.
    if n % 2 == 0:
        ## Add the square to the list.
        squares_loop.append(n * n)
## Same result as the comprehension.
print("Same result with a loop:", squares_loop)

# --- 7. Lists inside lists ---------------------------------------------------------------------
## A list of lists represents a 3x3 grid (rows of columns).
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
## grid[1] is the middle row; [1] again picks its middle value, 5.
print("Middle value:", grid[1][1])
## Visit each row.
for row in grid:
    ## Turn each number into text and join them with spaces.
    print(" ".join(str(value) for value in row))
## sum(row) for each row gives the row totals.
print("Row totals:", [sum(row) for row in grid])

# --- 8. Copying: a common surprise ----------------------------------------------------------------
## Create a list.
original = [1, 2, 3]
## Assignment does NOT copy: alias is another name for the SAME list.
alias = original
## Changing alias...
alias.append(4)
## ...also changes original, because they are one list.
print("original after changing alias:", original)
## .copy() makes a separate list with the same items.
independent = original.copy()
## Changing the copy...
independent.append(5)
## ...leaves the original alone.
print("original:", original, "| independent:", independent)

# --- 9. A worked example: a to-do list -------------------------------------------------------------
## Tasks as [name, done] pairs.
todo = [["write notes", True], ["practise loops", False], ["read Unit 9", False]]
## Mark the second task as done by changing its inner list.
todo[1][1] = True
## Visit each task and unpack the pair.
for task, done in todo:
    ## Show a tick box: [x] for done, [ ] for not done.
    print(f"[{'x' if done else ' '}] {task}")
## Count finished tasks with a comprehension and sum().
print("Finished:", sum(1 for task, done in todo if done), "of", len(todo))

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Make a list of 5 favourite films and print them in alphabetical order.
#   2. Remove every negative number from [3, -1, 4, -5, 9] using a
#      list comprehension.
#   3. Find the second-largest value in a list of numbers.
#   4. Print the sum of each column of the 3x3 grid.
# ---------------------------------------------------------------------------
