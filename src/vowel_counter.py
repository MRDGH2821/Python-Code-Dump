"""Vowel counter.

This program counts the number of vowels.
"""

string = str(input("Enter a string:"))
count = 0
# for loop iterating in string
for x in string:
    # checking character equal to vowel or not
    if x.lower() in "aeiou":
        count += 1  # storing the count of vowels
print(count)
