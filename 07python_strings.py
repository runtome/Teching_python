#!/usr/bin/env python3
# Unit 7: Work with text using string operations and methods.
#
# Big idea: a string is an ordered sequence of characters. Strings are
# "immutable": methods never change the original, they return a new string.

## A sentence with extra spaces at both ends.
sentence = "  Python makes ideas useful.  "

# --- 1. Cleaning and changing case ------------------------------------------------
## strip() returns a copy without the spaces at the start and end.
clean_sentence = sentence.strip()
## upper() makes every letter a capital.
print(clean_sentence.upper())
## lower() makes every letter small.
print(clean_sentence.lower())
## title() capitalises the first letter of every word.
print("python is great".title())
## capitalize() capitalises only the very first letter.
print("python is great".capitalize())
## lstrip()/rstrip() remove spaces from only the left or right side.
print("[" + sentence.rstrip() + "]")

# --- 2. Indexing and slicing ----------------------------------------------------------
##   P  y  t  h  o  n          <- characters
##   0  1  2  3  4  5          <- positive indexes (count from the start)
##  -6 -5 -4 -3 -2 -1          <- negative indexes (count from the end)
## [0] is the first character.
print("First character:", clean_sentence[0])
## [-1] is the last character.
print("Last character:", clean_sentence[-1])
## [:6] means "from the start up to (not including) index 6".
print("First six characters:", clean_sentence[:6])
## [7:12] gives indexes 7, 8, 9, 10, 11.
print("Characters 7 to 11:", clean_sentence[7:12])
## [::2] means "every second character".
print("Every second character:", clean_sentence[::2])
## A step of -1 walks backwards, which reverses the string.
print("Reversed:", clean_sentence[::-1])
## len() counts the characters (spaces and punctuation count too).
print("Length:", len(clean_sentence))

# --- 3. Searching -------------------------------------------------------------------------
## "in" asks whether one string appears inside another.
print("Contains 'ideas'?", "ideas" in clean_sentence)
## startswith() checks the beginning.
print("Starts with 'Py'?", clean_sentence.startswith("Py"))
## endswith() checks the end.
print("Ends with '.'?", clean_sentence.endswith("."))
## find() gives the index where a match starts, or -1 if it is missing.
print("Position of 'makes':", clean_sentence.find("makes"))
## count() counts how many times a piece of text appears.
print("How many 's'?", clean_sentence.count("s"))

# --- 4. Replacing, splitting and joining -----------------------------------------------------
## replace() returns a NEW string with "useful" swapped for "fun".
updated_sentence = clean_sentence.replace("useful", "fun")
## Shows the new string.
print(updated_sentence)
## The original is unchanged because strings are immutable.
print("Original is unchanged:", clean_sentence)

## split() with no argument breaks text on spaces into a list of words.
words = clean_sentence.split()
## Shows the list.
print("Words:", words)
## join() glues a list of strings together with "-" between them.
print("Joined with dashes:", "-".join(words))

## A line from a CSV (comma-separated values) file.
csv_line = "Ada,36,London"
## split(",") cuts on commas; the three parts go into three variables.
name, age, city = csv_line.split(",")
## Build a sentence from the parts.
print(f"{name} is {age} and lives in {city}.")

# --- 5. f-strings and formatting ---------------------------------------------------------------
## len(...split()) counts words: split into a list, then count the items.
word_count = len(clean_sentence.split())
## An f-string puts the value of {word_count} directly into the text.
print(f"The sentence has {word_count} words.")
## A price to format.
price = 1234.5
## :, adds thousands separators and .2f shows two decimal places.
print(f"Price: {price:,.2f} baht")
## :.1% multiplies by 100 and adds a % sign.
print(f"Percent: {0.875:.1%}")
## :<10 pads to 10 characters with the text on the left.
print(f"[{'left':<10}]")
## :>10 aligns right.
print(f"[{'right':>10}]")
## :^10 centres.
print(f"[{'centre':^10}]")
## :03 pads a number with zeros to 3 digits.
print(f"{7:03}")
## An expression can go inside the braces too.
print(f"2 to the power of 10 is {2 ** 10}")

# --- 6. Checking what a string contains -----------------------------------------------------------
## Test four sample strings.
for text in ["123", "abc", "abc123", "   "]:
    ## !r shows quotes; isdigit/isalpha/isalnum/isspace test the characters.
    print(f"{text!r:9} digits={text.isdigit()} letters={text.isalpha()} "
          f"alnum={text.isalnum()} spaces={text.isspace()}")

# --- 7. Looping over characters -------------------------------------------------------------------
## Start the vowel counter at zero.
vowel_count = 0
## Visit each character of the lower-case sentence.
for character in clean_sentence.lower():
    ## Is this character one of the five vowels?
    if character in "aeiou":
        ## Count it.
        vowel_count += 1
## Shows 9.
print("Vowels in the sentence:", vowel_count)

# --- 8. Strings are immutable --------------------------------------------------------------------
## clean_sentence[0] = "J" would raise a TypeError, so build a new string.
jython = "J" + clean_sentence[1:]
## Shows "Jython makes ideas useful."
print(jython)

# --- 9. A worked example: palindromes ------------------------------------------------------------
## Test a few phrases.
for phrase in ["Level", "Never odd or even", "Python"]:
    ## Keep only letters, lower-cased, so spaces and capitals do not matter.
    letters_only = "".join(ch.lower() for ch in phrase if ch.isalpha())
    ## A palindrome reads the same reversed.
    is_palindrome = letters_only == letters_only[::-1]
    ## Report the result.
    print(f"{phrase!r} palindrome? {is_palindrome}")

# ---------------------------------------------------------------------------
# Try it yourself:
#   1. Turn "hello world from python" into "Hello World From Python".
#   2. Count how many words in a sentence are longer than 4 letters.
#   3. Make an "initials" function: "Grace Brewster Hopper" -> "G.B.H."
#   4. Replace every vowel in a sentence with "*".
# ---------------------------------------------------------------------------
