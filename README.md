# Beginner Python Learning Curriculum

This curriculum contains small, runnable examples that build from basic output
to object-oriented programming. Each script uses only the Python standard
library and includes comments explaining its purpose and key lines.

## Units

1. [Basics and `print()`](01python_basics.py) — display text and simple results.
2. [Variables and types](02python_variables.py) — name values and inspect common types.
3. [Operators and input](03python_operators_input.py) — calculate, compare, and read a response with a safe default.
4. [Conditionals](04python_conditionals.py) — choose a path with `if`, `elif`, and `else`.
5. [Loops](05python_loops.py) — repeat actions with `for` and `while`.
6. [Functions](06python_functions.py) — reuse steps with parameters and return values.
7. [Strings](07python_strings.py) — clean, inspect, and format text.
8. [Lists](08python_lists.py) — keep and process an ordered sequence.
9. [Collections](09python_collections.py) — use dictionaries, tuples, and sets.
10. [Exceptions and files](10python_exceptions_files.py) — handle conversion errors and read/write a temporary text file.
11. [Classes](11python_classes.py) — define a class and create an object, methods, special methods, properties.
12. [Inheritance](12python_inheritance.py) — child classes, `super()`, polymorphism, and composition.
13. [Modules and the standard library](13python_modules_stdlib.py) — `import`, `math`, `random`, `datetime`, `collections`, `json`, and `__name__ == "__main__"`.
14. [Iterators and generators](14python_iterators_generators.py) — `zip`, `any`/`all`, `sorted(key=...)`, `map`/`filter`, `yield`, and generator expressions.
15. [Mini project: grade book](15python_mini_project.py) — combine every unit into one small, tested program.

## How each unit is organised

Every script is split into numbered sections. Each section starts with a
comment explaining the idea, followed by short code you can run and change.
Many units also include a **Common mistakes** note, and every unit ends with
**Try it yourself** exercises. Suggested way to study:

1. Read the comments in a section and predict what the code will print.
2. Run the script and compare the output with your prediction.
3. Change a value, run it again, and see what happens.
4. Finish with the exercises at the bottom of the file.

## Run a unit

Install Python 3.10 or newer (Unit 4 uses `match`), open a terminal in this directory, and run any unit with:

```sh
python3 01python_basics.py
```

Replace the filename with another unit from the list to run that lesson. Unit 3
prompts for a favorite color; pressing Enter (or running without interactive
input) uses the example value `blue`.

To run every unit in order and check that they all work:

```sh
for f in [0-9]*python_*.py; do echo "== $f"; python3 "$f" < /dev/null || break; done
```
