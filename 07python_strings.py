#!/usr/bin/env python3
# Unit 7: Work with text using string operations and methods.
#
# Big idea: a string is an ordered sequence of characters. Strings are
# "immutable": methods never change the original, they return a new string.

sentence = "  Python makes ideas useful.  "

# --- 1. Cleaning and changing case ------------------------------------------------
# strip() removes surrounding whitespace; upper() changes letter case.
clean_sentence = sentence.strip()
print(clean_sentence.upper())
print(clean_sentence.lower())
print("python is great".title())
print("python is great".capitalize())

# --- 2. Indexing and slicing ----------------------------------------------------------
# Strings can be indexed (first character is index 0) and sliced.
print("First character:", clean_sentence[0])
print("Last character:", clean_sentence[-1])      # negative = count from end
print("First six characters:", clean_sentence[:6])
print("Characters 7 to 11:", clean_sentence[7:12])
print("Every second character:", clean_sentence[::2])
print("Reversed:", clean_sentence[::-1])

#   P  y  t  h  o  n
#   0  1  2  3  4  5      <- positive indexes
#  -6 -5 -4 -3 -2 -1      <- negative indexes

# --- 3. Searching -------------------------------------------------------------------------
print("Contains 'ideas'?", "ideas" in clean_sentence)
print("Starts with 'Py'?", clean_sentence.startswith("Py"))
print("Ends with '.'?", clean_sentence.endswith("."))
print("Position of 'makes':", clean_sentence.find("makes"))   # -1 if missing
print("How many 's'?", clean_sentence.count("s"))

# --- 4. Replacing, splitting and joining -----------------------------------------------------
# replace() returns a new string; the original remains unchanged.
updated_sentence = clean_sentence.replace("useful", "fun")
print(updated_sentence)
print("Original is unchanged:", clean_sentence)

# split() breaks text into a list of words; join() glues a list back together.
words = clean_sentence.split()
print("Words:", words)
print("Joined with dashes:", "-".join(words))

csv_line = "Ada,36,London"
name, age, city = csv_line.split(",")
print(f"{name} is {age} and lives in {city}.")

# --- 5. f-strings and formatting ---------------------------------------------------------------
# An f-string inserts values directly into readable text.
word_count = len(clean_sentence.split())
print(f"The sentence has {word_count} words.")

price = 1234.5
print(f"Price: {price:,.2f} baht")       # thousands separator, 2 decimals
print(f"Percent: {0.875:.1%}")           # as a percentage
print(f"[{'left':<10}]")                 # pad to 10 characters, align left
print(f"[{'right':>10}]")                # align right
print(f"[{'centre':^10}]")               # centre
print(f"{7:03}")                         # pad numbers with zeros: 007

# --- 6. Checking what a string contains -----------------------------------------------------------
for text in ["123", "abc", "abc123", "   "]:
    print(f"{text!r:9} digits={text.isdigit()} letters={text.isalpha()} "
          f"alnum={text.isalnum()} spaces={text.isspace()}")

# --- 7. Looping over characters -------------------------------------------------------------------
# Count vowels by visiting each character.
vowel_count = 0
for character in clean_sentence.lower():
    if character in "aeiou":
        vowel_count += 1
print("Vowels in the sentence:", vowel_count)

# --- 8. Strings are immutable --------------------------------------------------------------------
# clean_sentence[0] = "J" would raise a TypeError. Build a new string instead:
jython = "J" + clean_sentence[1:]
print(jython)

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Check whether a word is a palindrome (same forwards and backwards).
#   2. Turn "hello world from python" into "Hello World From Python".
#   3. Count how many words in a sentence are longer than 4 letters.
#   4. Make an "initials" function: "Grace Brewster Hopper" -> "G.B.H."
# ---------------------------------------------------------------------------
