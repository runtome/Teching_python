#!/usr/bin/env python3
# Unit 10: Handle common errors and safely read and write a text file.

from pathlib import Path
from tempfile import NamedTemporaryFile

# try/except keeps a bad conversion from stopping the whole program.
text_number = "12"
try:
    number = int(text_number)
except ValueError:
    print("That text is not a whole number.")
else:
    print("Twice the number is", number * 2)

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
finally:
    # Cleanup runs even if reading or writing raises an exception.
    if demo_path is not None:
        demo_path.unlink(missing_ok=True)
