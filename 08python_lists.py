#!/usr/bin/env python3
# Unit 8: Store an ordered, changeable group of values in a list.

shopping_list = ["apples", "bread", "tea"]

# append() adds an item; indexing reads an item by its position.
shopping_list.append("rice")
print("First item:", shopping_list[0])

# A for loop visits each item in order.
for item in shopping_list:
    print("Buy:", item)

# List comprehensions build a new list from an existing sequence.
name_lengths = [len(item) for item in shopping_list]
print("Item name lengths:", name_lengths)
