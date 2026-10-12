#!/usr/bin/env python3
# Unit 3: Use arithmetic/comparison operators and read a value from the user.

# Arithmetic operators calculate with numbers.
first_number = 8
second_number = 3
print("Sum:", first_number + second_number)
print("Integer division:", first_number // second_number)
print("Remainder:", first_number % second_number)

# Comparison operators produce True or False.
print("Is the first number larger?", first_number > second_number)

# input() clearly prompts the learner; EOFError gives a safe default in
# non-interactive runs where no keyboard input is available.
try:
    favorite_color = input("Type a favorite color (press Enter for none): ").strip()
except EOFError:
    favorite_color = ""

# The default also makes an empty response useful and predictable.
if not favorite_color:
    favorite_color = "blue"
print("Your example color is", favorite_color + ".")
