"""Detailed Vowels Counter.

Counts vowels with their respective case.
"""

string = str(input("Enter a string:\n"))
count = 0
vowels = "aeiou"
for letter in string:
    if letter in vowels or letter in vowels.upper():
        count = count + 1
print("Total vowels = ", count)
print("a = ", string.count("a", 0, len(string)))
print("e = ", string.count("e", 0, len(string)))
print("i = ", string.count("i", 0, len(string)))
print("o = ", string.count("o", 0, len(string)))
print("u = ", string.count("u", 0, len(string)))
print("A = ", string.count("A", 0, len(string)))
print("E = ", string.count("E", 0, len(string)))
print("I = ", string.count("I", 0, len(string)))
print("O = ", string.count("O", 0, len(string)))
print("U = ", string.count("U", 0, len(string)))
