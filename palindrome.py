# Div-C Roll no.42
# This program checks whether given string is palindrome or not
fg = str(input("Enter a string:"))
flag = 0
for x in range(len(fg)):
    # checks if xth element is equal to (-1-x)th element of the list
    if fg[x] == fg[-1 - x]:
        flag = 1
        continue  # if equal then skip the cycle
    else:
        flag = 0
        break  # if unequal get out of loop
if flag == 1:  # flag is used to check if it is palindrome or not
    print("Given string is palindrome")
else:
    print("Given string is not palindrome")
