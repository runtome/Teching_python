#!/usr/bin/env python3
# Unit 2: Give values names and explore common built-in data types.

# Variables let us reuse values by referring to a descriptive name.
learner_name = "Sam"
lesson_number = 2
is_ready = True
temperature = 21.5

# type() shows the kind of value stored in each variable.
print("Name:", learner_name, "—", type(learner_name).__name__)
print("Lesson:", lesson_number, "—", type(lesson_number).__name__)
print("Ready:", is_ready, "—", type(is_ready).__name__)
print("Temperature:", temperature, "—", type(temperature).__name__)

# Converting a number to text makes it easy to build a sentence.
message = learner_name + " is studying lesson " + str(lesson_number) + "."
print(message)
