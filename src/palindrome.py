"""Palindrome checker.

This program checks whether given string is palindrome or not
"""

string = str(input("Enter a string:"))

# flag is used to check if it is palindrome or not
flag = 0

for x in range(len(string)):
    # checks if xth element is equal to (-1-x)th element of the list
    if string[x] == string[-1 - x]:
        flag = 1
        # if equal then skip the cycle
        continue
    else:
        flag = 0
        # if unequal get out of loop
        break


if flag == 1:
    print("Given string is palindrome.")
else:
    print("Given string is not palindrome.")
