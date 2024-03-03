# Div-C Roll no.42
# This program counts the number of vowels
fg = str(input("Enter a string:"))
ct = 0
for x in fg:  # for loop iterating in sring
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U':  # checking character equal to vowel or not
        ct += 1  # storing the count of vowels
print(ct)
