#!/usr/bin/env python3
# Unit 9: Compare dictionaries, tuples, and sets for grouped data.

# A dictionary maps unique keys to values.
book = {"title": "The Python Book", "pages": 120}
book["pages"] += 5  # Update the value associated with the pages key.
print(book["title"], "has", book["pages"], "pages.")

# A tuple is an ordered group that is usually treated as fixed.
coordinates = (4, 7)
print("Coordinates:", coordinates)

# A set stores unique values, so adding an existing value changes nothing.
topics = {"print", "variables", "loops"}
topics.add("loops")
print("Unique topics:", sorted(topics))
