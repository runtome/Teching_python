#!/usr/bin/env python3
# Unit 10: Handle common errors and safely read and write a text file.
#
# Big idea: when something goes wrong, Python "raises" an exception. If no
# code handles it, the program stops with a traceback. try/except lets you
# handle expected problems gracefully.

from pathlib import Path
from tempfile import NamedTemporaryFile

# --- 1. try / except / else ---------------------------------------------------------
# try/except keeps a bad conversion from stopping the whole program.
text_number = "12"
try:
    number = int(text_number)
except ValueError:
    print("That text is not a whole number.")
else:
    # else runs only when the try block raised no exception.
    print("Twice the number is", number * 2)

# --- 2. Handling different errors differently ------------------------------------------
def safe_divide(a, b):
    """Divide a by b, explaining any problem instead of crashing."""
    try:
        return a / b
    except ZeroDivisionError:
        print(f"  Cannot divide {a} by zero.")
    except TypeError as error:
        # "as error" gives access to the exception object and its message.
        print(f"  Wrong types: {error}")
    return None


print("10 / 4 =", safe_divide(10, 4))
print("10 / 0 =", safe_divide(10, 0))
print("10 / 'two' =", safe_divide(10, "two"))

# Common built-in exceptions you will meet:
#   ValueError        right type, bad value       int("hello")
#   TypeError         wrong type                  "a" + 1
#   KeyError          missing dictionary key      {}["x"]
#   IndexError        list position out of range  [1, 2][5]
#   ZeroDivisionError dividing by zero            1 / 0
#   FileNotFoundError opening a missing file      open("nope.txt")
for risky in (lambda: {}["x"], lambda: [1, 2][5]):
    try:
        risky()
    except (KeyError, IndexError) as error:
        print("Caught", type(error).__name__, "->", error)

# --- 3. Raising your own exceptions ----------------------------------------------------
# raise signals a problem that the caller should deal with.
def set_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age


try:
    set_age(-3)
except ValueError as error:
    print("Rejected:", error)

# --- 4. Writing and reading a file -----------------------------------------------------
# NamedTemporaryFile creates a temporary example file beside this script.
# The context manager closes it automatically, and finally removes it.
demo_path = None
try:
    with NamedTemporaryFile(
        mode="w", encoding="utf-8", dir=Path(__file__).parent,
        prefix="python_lesson_", suffix=".txt", delete=False
    ) as demo_file:
        demo_path = Path(demo_file.name)
        demo_file.write("Files can store text for later.\n")

    # Opening in read mode retrieves the text that was just written.
    with demo_path.open("r", encoding="utf-8") as demo_file:
        print("File says:", demo_file.read().strip())

    # Mode "a" (append) adds to the end instead of replacing the content.
    with demo_path.open("a", encoding="utf-8") as demo_file:
        for line_number in range(2, 5):
            demo_file.write(f"This is line {line_number}.\n")

    # Looping over a file object gives one line at a time — memory friendly
    # even for very large files.
    with demo_path.open("r", encoding="utf-8") as demo_file:
        for index, line in enumerate(demo_file, start=1):
            print(f"  {index}: {line.rstrip()}")

    # pathlib also offers one-line helpers for small files.
    print("Total characters:", len(demo_path.read_text(encoding="utf-8")))
finally:
    # Cleanup runs even if reading or writing raises an exception.
    if demo_path is not None:
        demo_path.unlink(missing_ok=True)

# File modes summary:
#   "r" read (default)  "w" write (replaces!)  "a" append  "x" create new only

# --- 5. Handling a missing file ----------------------------------------------------------
missing = Path(__file__).parent / "this_file_does_not_exist.txt"
try:
    missing.read_text(encoding="utf-8")
except FileNotFoundError:
    print("No file called", missing.name, "- using an empty default.")

# --- Good habits ---------------------------------------------------------------------------
# * Catch specific exceptions (ValueError), not everything (a bare except:).
#   Catching everything can hide real bugs.
# * Keep the try block small, so you know which line can fail.
# * Always use "with" to open files: it closes them even when errors happen.

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Keep asking for a number with input() until the user types a valid one.
#   2. Write a list of names to a file, one per line, then read it back.
#   3. Count the number of lines and words in a text file.
#   4. Write get_item(items, index) that returns None instead of crashing.
# ---------------------------------------------------------------------------
