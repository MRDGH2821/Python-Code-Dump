"""Smallest Divisor Finder."""

a = int(input("Enter a number:"))
for x in range(2, a + 1):
    if a % x != 0:
        continue
    else:
        print("Smallest divisor is:", x)
        break
