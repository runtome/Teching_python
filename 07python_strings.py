#!/usr/bin/env python3
# Unit 7: Work with text using string operations and methods.

sentence = "  Python makes ideas useful.  "

# strip() removes surrounding whitespace; upper() changes letter case.
clean_sentence = sentence.strip()
print(clean_sentence.upper())

# Strings can be indexed (first character is index 0) and sliced.
print("First character:", clean_sentence[0])
print("First six characters:", clean_sentence[:6])

# replace() returns a new string; the original remains unchanged.
updated_sentence = clean_sentence.replace("useful", "fun")
print(updated_sentence)

# An f-string inserts values directly into readable text.
word_count = len(clean_sentence.split())
print(f"The sentence has {word_count} words.")
