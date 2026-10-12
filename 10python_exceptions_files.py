#!/usr/bin/env python3
# Unit 10: Handle common errors and safely read and write a text file.
#
# Big idea: when something goes wrong, Python "raises" an exception. If no
# code handles it, the program stops with a traceback. try/except lets you
# handle expected problems gracefully.

## Path (from pathlib) represents a file or folder location.
from pathlib import Path
## NamedTemporaryFile creates a uniquely named file we can safely delete.
from tempfile import NamedTemporaryFile

# --- 1. try / except / else ---------------------------------------------------------
## Text that we hope is a whole number.
text_number = "12"
## Put the code that might fail inside try.
try:
    ## int() raises ValueError for text like "hello".
    number = int(text_number)
## except runs only if that specific error happened.
except ValueError:
    ## Explain the problem instead of crashing.
    print("That text is not a whole number.")
## else runs only when the try block raised no exception.
else:
    ## Safe to use number here.
    print("Twice the number is", number * 2)


# --- 2. Handling different errors differently ------------------------------------------
## A function that explains problems instead of crashing.
def safe_divide(a, b):
    """Divide a by b, explaining any problem instead of crashing."""
    ## Try the division.
    try:
        ## Return the answer if it works.
        return a / b
    ## Dividing by zero is impossible.
    except ZeroDivisionError:
        ## Explain the problem.
        print(f"  Cannot divide {a} by zero.")
    ## "as error" stores the exception object, which holds a message.
    except TypeError as error:
        ## Show Python's message.
        print(f"  Wrong types: {error}")
    ## Reached only when an exception was handled.
    return None


## Works: 2.5.
print("10 / 4 =", safe_divide(10, 4))
## Handled ZeroDivisionError: None.
print("10 / 0 =", safe_divide(10, 0))
## Handled TypeError: None.
print("10 / 'two' =", safe_divide(10, "two"))

## Common built-in exceptions you will meet:
##   ValueError        right type, bad value       int("hello")
##   TypeError         wrong type                  "a" + 1
##   KeyError          missing dictionary key      {}["x"]
##   IndexError        list position out of range  [1, 2][5]
##   ZeroDivisionError dividing by zero            1 / 0
##   FileNotFoundError opening a missing file      open("nope.txt")
## Two small lambdas that each raise a different error when called.
for risky in (lambda: {}["x"], lambda: [1, 2][5]):
    ## Call each one inside try.
    try:
        ## Calling it raises the error.
        risky()
    ## A tuple of exception types catches either kind.
    except (KeyError, IndexError) as error:
        ## type(error).__name__ shows which error it was.
        print("Caught", type(error).__name__, "->", error)


# --- 3. Raising your own exceptions ----------------------------------------------------
## raise signals a problem that the caller should deal with.
def set_age(age):
    ## Reject impossible values.
    if age < 0:
        ## Stop the function and raise a ValueError with a clear message.
        raise ValueError("age cannot be negative")
    ## Otherwise accept the value.
    return age


## Call it with a bad value inside try.
try:
    ## This raises ValueError.
    set_age(-3)
## Catch it.
except ValueError as error:
    ## Show the message we wrote in raise.
    print("Rejected:", error)

# --- 4. finally: code that always runs ----------------------------------------------------
## Try something that fails.
try:
    ## Raises ZeroDivisionError.
    result = 1 / 0
## Handle it.
except ZeroDivisionError:
    ## Explain.
    print("Division failed.")
## finally runs whether or not an error happened — ideal for clean-up.
finally:
    ## Always printed.
    print("finally always runs.")

# --- 5. Writing and reading a file -----------------------------------------------------
## None means "no file created yet"; the finally block below checks this.
demo_path = None
## try/finally makes sure the file is deleted even if something fails.
try:
    ## "w" opens for writing; delete=False lets us reopen it afterwards.
    with NamedTemporaryFile(
        mode="w", encoding="utf-8", dir=Path(__file__).parent,
        prefix="python_lesson_", suffix=".txt", delete=False
    ) as demo_file:
        ## Remember where the file is.
        demo_path = Path(demo_file.name)
        ## write() stores text; "\n" ends the line.
        demo_file.write("Files can store text for later.\n")

    ## Mode "r" opens the file for reading.
    with demo_path.open("r", encoding="utf-8") as demo_file:
        ## read() returns the whole file as one string.
        print("File says:", demo_file.read().strip())

    ## Mode "a" (append) adds to the end instead of replacing the content.
    with demo_path.open("a", encoding="utf-8") as demo_file:
        ## Write three more lines.
        for line_number in range(2, 5):
            ## Each line ends with a new line character.
            demo_file.write(f"This is line {line_number}.\n")

    ## Open again to read line by line.
    with demo_path.open("r", encoding="utf-8") as demo_file:
        ## Looping over a file gives one line at a time (memory friendly).
        for index, line in enumerate(demo_file, start=1):
            ## rstrip() removes the "\n" at the end of each line.
            print(f"  {index}: {line.rstrip()}")

    ## read_text() is a one-line helper for reading small files.
    print("Total characters:", len(demo_path.read_text(encoding="utf-8")))
## Cleanup runs even if reading or writing raised an exception.
finally:
    ## Only delete if the file was actually created.
    if demo_path is not None:
        ## unlink() deletes the file; missing_ok avoids an error if it is gone.
        demo_path.unlink(missing_ok=True)

## File modes summary:
##   "r" read (default)  "w" write (replaces!)  "a" append  "x" create new only

# --- 6. Handling a missing file ----------------------------------------------------------
## The / operator joins folder and file names into one Path.
missing = Path(__file__).parent / "this_file_does_not_exist.txt"
## Try to read the missing file.
try:
    ## Raises FileNotFoundError.
    missing.read_text(encoding="utf-8")
## Handle that specific error.
except FileNotFoundError:
    ## .name is just the file name without its folder.
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
