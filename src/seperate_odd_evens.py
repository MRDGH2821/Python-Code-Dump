"""Odd-Even Seperator."""

from __future__ import annotations

from random import randint

even: list[int] = []
odd: list[int] = []
random_numbers = [randint(1, 10) for _ in range(5)]  # noqa: S311
for x in random_numbers:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)
print(even)
print(odd)
