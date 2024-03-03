"""
This program counts the number of vowels
"""

fg = str(input("Enter a string:"))
ct = 0
# for loop iterating in string
for x in fg:
    # checking character equal to vowel or not
    if x.lower() in "aeiou":
        ct += 1  # storing the count of vowels
print(ct)
