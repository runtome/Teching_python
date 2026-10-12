#!/usr/bin/env python3
# Unit 15: Mini project — a grade book that combines everything so far.
#
# Big idea: real programs are built from small pieces. This project uses
# variables, conditionals, loops, functions, strings, lists, dictionaries,
# exceptions, files (JSON), classes and the standard library together.
#
# Read it from top to bottom, run it, then try the extension ideas at the end.

import json
from pathlib import Path
from statistics import mean
from tempfile import TemporaryDirectory


def letter_grade(score):
    """Turn a number score into a letter grade (Unit 4)."""
    if score >= 80:
        return "A"
    if score >= 70:
        return "B"
    if score >= 60:
        return "C"
    if score >= 50:
        return "D"
    return "F"


class Student:
    """One student and their list of scores (Unit 11)."""

    def __init__(self, name, scores=None):
        self.name = name
        # Use None as the default, then make a new list. A default of [] would
        # be shared by every Student — a classic Python surprise.
        self.scores = list(scores) if scores else []

    def add_score(self, score):
        if not 0 <= score <= 100:
            raise ValueError(f"score must be 0-100, got {score}")
        self.scores.append(score)

    def average(self):
        return mean(self.scores) if self.scores else 0

    def to_dict(self):
        return {"name": self.name, "scores": self.scores}


class GradeBook:
    """A collection of students with reports and saving (Units 8-10)."""

    def __init__(self):
        self.students = {}          # name -> Student

    def add_student(self, name):
        key = name.strip().title()  # clean the text (Unit 7)
        if key not in self.students:
            self.students[key] = Student(key)
        return self.students[key]

    def record(self, name, score_text):
        """Record a score given as text, reporting bad input instead of crashing."""
        try:
            score = float(score_text)
            self.add_student(name).add_score(score)
        except ValueError as error:
            print(f"  Skipped {name!r} / {score_text!r}: {error}")

    def ranking(self):
        return sorted(self.students.values(), key=Student.average, reverse=True)

    def report(self):
        print(f"{'Rank':<5}{'Name':<10}{'Average':>8}  Grade")
        print("-" * 30)
        for rank, student in enumerate(self.ranking(), start=1):
            average = student.average()
            print(f"{rank:<5}{student.name:<10}{average:>8.1f}  {letter_grade(average)}")

    def class_average(self):
        averages = [s.average() for s in self.students.values()]
        return mean(averages) if averages else 0

    def save(self, path):
        data = [student.to_dict() for student in self.students.values()]
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    @classmethod
    def load(cls, path):
        """Create a GradeBook from a JSON file made by save()."""
        book = cls()
        for item in json.loads(path.read_text(encoding="utf-8")):
            book.students[item["name"]] = Student(item["name"], item["scores"])
        return book


def main():
    # Raw data as it might arrive from a form: messy names, some bad values.
    raw_entries = [
        ("ana", "85"), ("Ben", "62"), ("  cy ", "91"),
        ("ana", "78"), ("ben", "seventy"), ("Cy", "88"),
        ("dee", "45"), ("Dee", "150"), ("dee", "58"),
    ]

    print("Recording scores...")
    book = GradeBook()
    for name, score_text in raw_entries:
        book.record(name, score_text)

    print()
    book.report()
    print(f"\nClass average: {book.class_average():.1f}")

    needs_help = [s.name for s in book.students.values() if s.average() < 60]
    print("Students who may need extra help:", ", ".join(needs_help) or "none")

    # Save to a temporary folder, load it back, and check nothing was lost.
    with TemporaryDirectory() as folder:
        path = Path(folder) / "grades.json"
        book.save(path)
        reloaded = GradeBook.load(path)
        print("\nSaved and reloaded", len(reloaded.students), "students.")

    # assert stops the program if something is not true: a tiny built-in test.
    assert letter_grade(80) == "A" and letter_grade(49.9) == "F"
    assert reloaded.students["Ana"].scores == [85.0, 78.0]
    print("All checks passed.")


if __name__ == "__main__":
    main()

# ---------------------------------------------------------------------------
# Extension ideas:
#   1. Ask the user for names and scores with input() until they type "done".
#   2. Add a highest_score() method and show it in the report.
#   3. Let each score have a subject: store a dict like {"maths": [80, 90]}.
#   4. Save the report as a .txt file as well as JSON.
#   5. Write a few more assert checks for edge cases (a student with no scores?).
# ---------------------------------------------------------------------------
