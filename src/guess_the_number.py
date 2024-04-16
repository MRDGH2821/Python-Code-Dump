"""Guess the number."""

from random import randint

x = randint(1, 10)
a = 0
b = 0
while a != x:
    a = int(input("Enter a no "))
    b += 1
print("The no is", x, ". Guessed in ", b, "tries")
