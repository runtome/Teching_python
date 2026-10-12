#!/usr/bin/env python3
# Unit 15: Mini project — a grade book that combines everything so far.
#
# Big idea: real programs are built from small pieces. This project uses
# variables, conditionals, loops, functions, strings, lists, dictionaries,
# exceptions, files (JSON), classes and the standard library together.
#
# Read it from top to bottom, run it, then try the extension ideas at the end.

## json saves and loads our data as text (Unit 13).
import json
## Path represents file locations (Unit 10).
from pathlib import Path
## mean() calculates an average (Unit 13).
from statistics import mean
## TemporaryDirectory gives us a folder that deletes itself afterwards.
from tempfile import TemporaryDirectory


## A plain function that turns a score into a letter (Units 4 and 6).
def letter_grade(score):
    """Turn a number score into a letter grade."""
    ## 80 and above is an A.
    if score >= 80:
        ## return leaves the function immediately, so no elif is needed.
        return "A"
    ## 70-79.
    if score >= 70:
        ## B grade.
        return "B"
    ## 60-69.
    if score >= 60:
        ## C grade.
        return "C"
    ## 50-59.
    if score >= 50:
        ## D grade.
        return "D"
    ## Anything below 50.
    return "F"


## One student and their list of scores (Unit 11).
class Student:
    """One student and their list of scores."""

    ## scores=None is safer than scores=[] (see the note below).
    def __init__(self, name, scores=None):
        ## The student's name.
        self.name = name
        ## A default of [] would be SHARED by every Student — a classic
        ## Python surprise — so make a fresh list for each student instead.
        self.scores = list(scores) if scores else []

    ## Add one score after checking it.
    def add_score(self, score):
        ## Scores must be between 0 and 100.
        if not 0 <= score <= 100:
            ## Raise an error the caller can catch (Unit 10).
            raise ValueError(f"score must be 0-100, got {score}")
        ## Store the valid score.
        self.scores.append(score)

    ## The student's average score.
    def average(self):
        ## mean() fails on an empty list, so return 0 when there are no scores.
        return mean(self.scores) if self.scores else 0

    ## The best score.
    def highest(self):
        ## max() of an empty list fails too, so guard it the same way.
        return max(self.scores) if self.scores else 0

    ## Convert to a plain dictionary so json can save it.
    def to_dict(self):
        ## Only plain types (str, list, numbers) can go into JSON.
        return {"name": self.name, "scores": self.scores}


## A collection of students with reports and saving (Units 8-10).
class GradeBook:
    """A collection of students with reports and saving."""

    ## Start empty.
    def __init__(self):
        ## A dictionary: cleaned name -> Student object.
        self.students = {}

    ## Find a student, creating them if needed.
    def add_student(self, name):
        ## Clean the text so "  ana " and "Ana" are the same person (Unit 7).
        key = name.strip().title()
        ## Only create a new Student if we have not seen this name.
        if key not in self.students:
            ## Store a new Student under the clean name.
            self.students[key] = Student(key)
        ## Give back the Student object.
        return self.students[key]

    ## Record a score that arrives as text, e.g. from a form.
    def record(self, name, score_text):
        """Record a score given as text, reporting bad input instead of crashing."""
        ## Converting or adding may fail, so use try.
        try:
            ## float() raises ValueError for text like "seventy".
            score = float(score_text)
            ## add_score() raises ValueError for numbers outside 0-100.
            self.add_student(name).add_score(score)
        ## Both kinds of problem are ValueErrors.
        except ValueError as error:
            ## !r shows the exact text received, including quotes and spaces.
            print(f"  Skipped {name!r} / {score_text!r}: {error}")

    ## Students sorted from best to worst average.
    def ranking(self):
        ## key=Student.average sorts by each student's average (Unit 14).
        return sorted(self.students.values(), key=Student.average, reverse=True)

    ## Print a neat table.
    def report(self):
        ## Column headings, padded to fixed widths with f-string alignment.
        print(f"{'Rank':<5}{'Name':<10}{'Average':>8}{'Best':>6}  Grade")
        ## A separator line.
        print("-" * 36)
        ## Number the students from 1.
        for rank, student in enumerate(self.ranking(), start=1):
            ## Calculate once and reuse.
            average = student.average()
            ## :>8.1f right-aligns in 8 characters with 1 decimal place.
            print(f"{rank:<5}{student.name:<10}{average:>8.1f}"
                  f"{student.highest():>6.0f}  {letter_grade(average)}")

    ## The average of all the students' averages.
    def class_average(self):
        ## A list comprehension of each student's average.
        averages = [s.average() for s in self.students.values()]
        ## Guard against an empty grade book.
        return mean(averages) if averages else 0

    ## Save every student to a JSON file.
    def save(self, path):
        ## Turn each Student into a dictionary.
        data = [student.to_dict() for student in self.students.values()]
        ## Write the JSON text to the file.
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    ## A classmethod is called on the class itself: GradeBook.load(path).
    @classmethod
    def load(cls, path):
        """Create a GradeBook from a JSON file made by save()."""
        ## cls is GradeBook, so cls() makes a new empty grade book.
        book = cls()
        ## Read the file and turn the JSON text back into a list of dicts.
        for item in json.loads(path.read_text(encoding="utf-8")):
            ## Rebuild each Student object.
            book.students[item["name"]] = Student(item["name"], item["scores"])
        ## Give back the filled grade book.
        return book


## The main program.
def main():
    ## Raw data as it might arrive from a form: messy names, some bad values.
    raw_entries = [
        ("ana", "85"), ("Ben", "62"), ("  cy ", "91"),
        ("ana", "78"), ("ben", "seventy"), ("Cy", "88"),
        ("dee", "45"), ("Dee", "150"), ("dee", "58"),
    ]

    ## A heading.
    print("Recording scores...")
    ## Create an empty grade book.
    book = GradeBook()
    ## Unpack each (name, score) tuple.
    for name, score_text in raw_entries:
        ## Record it; bad entries are reported and skipped.
        book.record(name, score_text)

    ## A blank line for spacing.
    print()
    ## Print the ranked table.
    book.report()
    ## \n starts with a blank line; :.1f shows one decimal place.
    print(f"\nClass average: {book.class_average():.1f}")

    ## A comprehension picks students whose average is below 60.
    needs_help = [s.name for s in book.students.values() if s.average() < 60]
    ## join() makes a comma list; "or" gives "none" when the list is empty.
    print("Students who may need extra help:", ", ".join(needs_help) or "none")

    ## Save to a temporary folder that is deleted at the end of the with block.
    with TemporaryDirectory() as folder:
        ## Build the file path inside the temporary folder.
        path = Path(folder) / "grades.json"
        ## Write the file.
        book.save(path)
        ## Read it back into a brand-new GradeBook.
        reloaded = GradeBook.load(path)
        ## Confirm everyone came back.
        print("\nSaved and reloaded", len(reloaded.students), "students.")

    ## assert stops the program if something is not True: a tiny built-in test.
    assert letter_grade(80) == "A" and letter_grade(49.9) == "F"
    ## Check the saved data survived the round trip.
    assert reloaded.students["Ana"].scores == [85.0, 78.0]
    ## A student with no scores should not crash.
    assert Student("Empty").average() == 0
    ## Only reached if every assert passed.
    print("All checks passed.")


## Run main() only when this file is run directly (Unit 13).
if __name__ == "__main__":
    ## Start the program.
    main()

# ---------------------------------------------------------------------------
# Extension ideas:
#   1. Ask the user for names and scores with input() until they type "done".
#   2. Let each score have a subject: store a dict like {"maths": [80, 90]}.
#   3. Save the report as a .txt file as well as JSON.
#   4. Draw a bar chart of the averages with matplotlib (see Unit 17).
# ---------------------------------------------------------------------------
