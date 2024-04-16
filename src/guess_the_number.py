"""Guess the number."""

from secrets import randbelow

print("Guess the number!")
secret_number = randbelow(10)
guessed = 0
tries = 0
while guessed != secret_number:
    guessed = int(input("Enter a no: "))
    tries += 1
print("The no is", secret_number, ". Guessed in", tries, "tries")
