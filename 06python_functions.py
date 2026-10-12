#!/usr/bin/env python3
# Unit 6: Package reusable steps in functions.

# Parameters receive information, and return sends a result back to the caller.
def greet(name):
    """Return a friendly greeting for one learner."""
    return f"Hello, {name}! Welcome to Python."


# A default parameter is used when the caller leaves that argument out.
def rectangle_area(width, height=1):
    """Calculate the area of a rectangle."""
    return width * height


print(greet("Riley"))
print("Area:", rectangle_area(4, 3))
print("Area of a 4 by 1 rectangle:", rectangle_area(4))
